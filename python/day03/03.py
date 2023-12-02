import re
from pathlib import Path


def check_chunk(chunk):
    if chunk:
        chunk = re.sub('[.]', '', chunk)
        chunk = re.sub('\d', '', chunk)
        return len(chunk) != 0
    return False


def process_line(l, pl, nl):
    l = l.strip()
    local_sum = 0
    possible_numbers = re.finditer('\d+', l)
    for n in possible_numbers:
        chunk_start, chunk_end = n.span()
        if chunk_start != 0:
            chunk_start -= 1
        if chunk_end != len(l):
            chunk_end += 1    
        if pl and check_chunk(pl[chunk_start:chunk_end]):
            local_sum += int(n.group())
            continue
        if nl and check_chunk(nl[chunk_start:chunk_end]):
            local_sum += int(n.group())
            continue
        if chunk_start > 0 and check_chunk(l[chunk_start]):
            local_sum += int(n.group())
            continue
        if chunk_end-1 != len(l) and check_chunk(l[chunk_end-1]):
            local_sum += int(n.group())
            continue
    return local_sum



def part_1(input_file):
    current_sum = 0

    prev_line = None
    current_line = None
    next_line = None
    with open(input_file) as mf:
        prev_line = next(mf).strip()
        current_line = next(mf).strip()
        current_sum += process_line(prev_line, '', current_line)
        next_line = next(mf).strip()
        current_sum += process_line(current_line, prev_line, next_line)

        for line in mf:
            prev_line = current_line
            current_line = next_line
            next_line = line
            current_sum += process_line(current_line, prev_line, next_line)
        current_sum += process_line(line, current_line, '')
        
    print(current_sum)


def solve_starts_adjectnancy(l, pl, nl):
    l = l.strip()
    pl = pl.strip()
    nl = nl.strip()
    local_sum = 0
    stars = [m.start() for m in re.finditer('[*]', l)]

    for star in stars:
        nums = list()
        
        if pl:
            print(f'check prev line: {pl}')
            possible_numbers = re.finditer('\d+', pl)
            for possible_number in possible_numbers:
                num_start, num_end = possible_number.span()
                if star != len(l)-1:
                    num_end += 1
                if star != 0:
                    num_start -= 1
                if star in range(num_start, num_end):
                    print(f'found: {possible_number.group()}')
                    nums.append(int(possible_number.group()))
        if nl:
            print(f'check next line: {nl}')
            possible_numbers = re.finditer('\d+', nl)
            for possible_number in possible_numbers:
                num_start, num_end = possible_number.span()
                if star != len(l)-1:
                    num_end += 1
                if star != 0:
                    num_start -= 1
                if star in range(num_start, num_end):
                    print(f'found: {possible_number.group()}')
                    nums.append(int(possible_number.group()))
        print(f'check current line: {l}')
        possible_numbers = re.finditer('\d+', l)
        for possible_number in possible_numbers:
            num_start, num_end = possible_number.span()
            if star == 0:
                if num_start == 1:
                    print(f'found: {possible_number.group()}')
                    nums.append(int(possible_number.group()))
            elif star == len(l)-1:
                if num_end == star:
                    print(f'found: {possible_number.group()}')
                    nums.append(int(possible_number.group()))   
            else:
                if num_end == star or num_start == star +1:
                    print(f'found: {possible_number.group()}')
                    nums.append(int(possible_number.group()))   
        if len(nums)> 1:
            local_sum += nums[0]*nums[1]
    return local_sum


def part_2(input_file):
    current_sum = 0
    prev_line = None
    current_line = None
    next_line = None
    with open(input_file) as mf:
        prev_line = next(mf).strip()
        current_line = next(mf).strip()
        current_sum += solve_starts_adjectnancy(prev_line, '', current_line)
        next_line = next(mf).strip()
        current_sum += solve_starts_adjectnancy(current_line, prev_line, next_line)

        for line in mf:
            prev_line = current_line
            current_line = next_line
            next_line = line
            current_sum += solve_starts_adjectnancy(current_line, prev_line, next_line)
        current_sum += solve_starts_adjectnancy(line, current_line, '')
    print(current_sum)


# input = Path('input.txt')
input = Path('puzzle_input.txt')

# part_1(input)
part_2(input)

