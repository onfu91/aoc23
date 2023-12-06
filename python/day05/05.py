import re
from pathlib import Path


debug = False


def convert_to_lists(section):
    converted_section = list()
    for line in section.splitlines():
        converted_section.append([int(chunk.strip()) for chunk in line.split(' ')])
    return converted_section


def use_mapping(seed, seed_to_soil):
    # r[0] target
    # r[1] source
    # r[2] distance
    for r in seed_to_soil:
        if seed in range(r[1], r[1] + r[2]):
            return abs(r[1]-seed)+r[0]
    else:
        return seed


def main():

    # puzzle_input = Path('input.txt').read_text()
    puzzle_input = Path('puzzle_input.txt').read_text()

    # seeds = [int(n.strip()) for n in puzzle_input[0].split(':')[1].strip().split(' ')]
    pattern = (r'seeds:(?P<seeds>.*)\n\n'
               r'seed-to-soil map:\n(?P<soil>(?:(?:\d| )+\n)+)\n'
               r'soil-to-fertilizer map:\n(?P<fertilizer>(?:(?:\d| )+\n)+)\n'
               r'fertilizer-to-water map:\n(?P<water>(?:(?:\d| )+\n)+)\n'
               r'water-to-light map:\n(?P<light>(?:(?:\d| )+\n)+)\n'
               r'light-to-temperature map:\n(?P<temperature>(?:(?:\d| )+\n)+)\n'
               r'temperature-to-humidity map:\n(?P<humidity>(?:(?:\d| )+\n)+)\n'
               r'humidity-to-location map:\n(?P<location>(?:(?:\d| )+\n?)+)')
    matches = re.finditer(pattern, puzzle_input, re.MULTILINE)
    if matches:
        match = next(matches)
        seed_to_soil_map = match.group('soil')
        seed_to_fertilizer_map = match.group('fertilizer')
        seed_to_water_map = match.group('water')
        seed_to_light_map = match.group('light')
        seed_to_temperature_map = match.group('temperature')
        seed_to_humidity_map = match.group('humidity')
        seed_to_location_map = match.group('location')

        if debug:
            print(f'soil:\n{seed_to_soil_map}')
            print(f'fertilizer:\n{seed_to_fertilizer_map}')
            print(f'water:\n{seed_to_water_map}')
            print(f'light:\n{seed_to_light_map}')
            print(f'temperature:\n{seed_to_temperature_map}')
            print(f'humidity:\n{seed_to_humidity_map}')
            print(f'location:\n{seed_to_location_map}')

        location_numbers = list()

        # PART1
        seeds = [int(seed) for seed in match.group('seeds').strip().split(' ')]

        for seed in seeds:
            seed_to_soil = convert_to_lists(seed_to_soil_map)
            seed_to_fertilizer = convert_to_lists(seed_to_fertilizer_map)
            seed_to_water = convert_to_lists(seed_to_water_map)
            seed_to_light = convert_to_lists(seed_to_light_map)
            seed_to_temperature = convert_to_lists(seed_to_temperature_map)
            seed_to_humidity = convert_to_lists(seed_to_humidity_map)
            seed_to_location = convert_to_lists(seed_to_location_map)

            soil_number = use_mapping(seed, seed_to_soil)
            fertilizer_number = use_mapping(soil_number, seed_to_fertilizer)
            water_number = use_mapping(fertilizer_number, seed_to_water)
            light_number = use_mapping(water_number, seed_to_light)
            temperature_number = use_mapping(light_number, seed_to_temperature)
            humidity_number = use_mapping(temperature_number, seed_to_humidity)
            location_number = use_mapping(humidity_number, seed_to_location)

            location_numbers.append(location_number)
            print(f'Seed {seed}, soil {soil_number}, fertilizer {fertilizer_number},'
                  f'water {water_number}, light {light_number}, temperature {temperature_number},'
                  f'humidity {humidity_number}, location {location_number}')

            if debug:
                print(seed)
                print(soil_number)
                print(fertilizer_number)
                print(water_number)
                print(light_number)
                print(temperature_number)
                print(humidity_number)
                print(location_number)
        print(min(location_numbers))

        # PART2
        location_numbers = list()
        seed_pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
        for s, range_len in seed_pairs:
            seed_range = range(s, s + range_len)
            seed_iter = iter(seed_range)
            while (seed := next(seed_iter, None)) is not None:
                seed_to_soil = convert_to_lists(seed_to_soil_map)
                seed_to_fertilizer = convert_to_lists(seed_to_fertilizer_map)
                seed_to_water = convert_to_lists(seed_to_water_map)
                seed_to_light = convert_to_lists(seed_to_light_map)
                seed_to_temperature = convert_to_lists(seed_to_temperature_map)
                seed_to_humidity = convert_to_lists(seed_to_humidity_map)
                seed_to_location = convert_to_lists(seed_to_location_map)

                soil_number = use_mapping(seed, seed_to_soil)
                fertilizer_number = use_mapping(soil_number, seed_to_fertilizer)
                water_number = use_mapping(fertilizer_number, seed_to_water)
                light_number = use_mapping(water_number, seed_to_light)
                temperature_number = use_mapping(light_number, seed_to_temperature)
                humidity_number = use_mapping(temperature_number, seed_to_humidity)
                location_number = use_mapping(humidity_number, seed_to_location)

                location_numbers.append(location_number)
                # print(f'Seed {seed}, soil {soil_number}, fertilizer {fertilizer_number},'
                #       f'water {water_number}, light {light_number}, temperature {temperature_number},'
                #       f'humidity {humidity_number}, location {location_number}')
        print(min(location_numbers))


if __name__ == '__main__':
    main()
