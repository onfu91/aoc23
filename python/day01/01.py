from pathlib import Path

dummy_table = {
   'one': '1',   'two': '2', 'three': '3',
   'eno': '1',   'owt': '2', 'eerht': '3',
   'four': '4', 'five': '5', 'six': '6',
   'ruof': '4', 'evif': '5', 'xis': '6',
   'seven': '7', 'eight': '8', 'nine': '9',
   'neves': '7', 'thgie': '8', 'enin': '9'
}


def replace_lowest(line: str, replacements: list):
    indexes = [line.find(r) for r in replacements]
    tmp_list = [index for index in indexes if index > -1]
    if tmp_list:
        lowest_substring = replacements[indexes.index(min(tmp_list))]
        line = line.replace(lowest_substring, dummy_table[lowest_substring])
    return line

# input = Path('input.txt').read_text().splitlines()
# input = Path('input2.txt').read_text().splitlines()
input = Path('puzzle_input.txt').read_text().splitlines()

calibration_values = list()
for line in input:
    pair = list()

    line_l = line
    line_r = line[::-1]

    repl_l = ['one', 'two', 'three', 'four','five','six','seven','eight','nine']
    repl_r = [i[::-1]for i in repl_l]
    
    line_l = replace_lowest(line_l, repl_l)
    for i, c in enumerate(line_l):
        if c.isdigit():
            pair.append(c)
            break
    line_r = replace_lowest(line_r, repl_r)
    for i, c in enumerate(line_r):
        if c.isdigit():
            pair.append(c)
            break
    calibration_values.append(int(''.join(pair)))
print(sum(calibration_values))
    