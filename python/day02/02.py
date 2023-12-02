from pathlib import Path


def load_game(line):
    game_info, game_sets = line.split(':')

    game_info = int(game_info.split(' ')[1].strip())
    game_sets = game_sets.split(';')
    game_sets = [game_set.strip() for game_set in game_sets]
    tmp_data = {
        'red': list(),
        'green': list(),
        'blue': list()
    }
    for game_set in game_sets:
        for cubes in game_set.split(','):
            cubes = cubes.strip()
            n_cubes, cube_color = cubes.split(' ')
            n_cubes = int(n_cubes)
            tmp_data[cube_color].append(n_cubes)
    
    return game_info, tmp_data


def can_play_game(game_data: dict, cubes_info: dict) -> bool:
    can_play_with_red = all([i <= cubes_info['red'] for i in game_data['red']])
    can_play_with_green = all([i <= cubes_info['green'] for i in game_data['green']])
    can_play_with_blue = all([i <= cubes_info['blue'] for i in game_data['blue']])

    return can_play_with_red and can_play_with_green and can_play_with_blue

# input = Path('input.txt').read_text().splitlines()
input = Path('puzzle_input.txt').read_text().splitlines()

cubes_amount = {
    'red': 12,
    'green': 13,
    'blue': 14
}

game_stats = list()
for line in input:
    game_stats.append(load_game(line=line))

final_sum = 0
for game in game_stats:
    if can_play_game(game[1], cubes_info=cubes_amount):
        final_sum += game[0]

print(final_sum)

game_powers = list()
for game in game_stats:
    game_data = game[1]
    red = max(game_data['red'])
    green =  max(game_data['green'])
    blue =  max(game_data['blue'])
    game_powers.append(red*green*blue)

print(sum(game_powers))