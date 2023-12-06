from pathlib import Path


def can_win_race(hold_time: int, time: int, distance: int) -> bool:
    return (time - hold_time) * hold_time > distance


def main():
    # puzzle_input = Path('input.txt').read_text().splitlines()
    puzzle_input = Path('puzzle_input.txt').read_text().splitlines()
    times = [int(time) for time in puzzle_input[0].split(':')[1].split(' ') if time.strip()]
    race_records = [int(record) for record in puzzle_input[1].split(':')[1].split(' ') if record.strip()]
    race_info = list(zip(times, race_records))

    print('Part1')
    result = 1
    for time, distance in race_info:
        possible_win_counts = [can_win_race(hold_time, time, distance) for hold_time in list(range(time))].count(True)
        result *= possible_win_counts
    print(result)

    print('Part2')
    time = 60808676
    distance = 601116315591300
    possible_win_counts = [can_win_race(hold_time, time, distance) for hold_time in list(range(time))].count(True)
    print(possible_win_counts)


if __name__ == '__main__':
    main()
