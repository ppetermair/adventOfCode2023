#!/usr/bin/env python3

from os import path

def main():

    matrix = []
    part_numbers = []
    for line in get_input():
        matrix.append([char for char in line])
    
    for y, line in enumerate(matrix):
        number = "";
        is_number_adjacent = False
        for x, char in enumerate(line):
            if char.isdigit():
                number += char
                if is_adjacent_to_symbol(matrix, x, y):
                    is_number_adjacent = True
            else:
                if is_number_adjacent:
                    part_numbers.append(int(number))
                number = ""
                is_number_adjacent = False
        if is_number_adjacent:
                    part_numbers.append(int(number))
    
    print(f'Part I {sum(part_numbers)}')

def is_adjacent_to_symbol(matrix, x, y):
    return (
        is_symbol(matrix, x-1, y+1) or
        is_symbol(matrix, x, y+1) or 
        is_symbol(matrix, x+1, y+1) or 
        is_symbol(matrix, x-1, y) or 
        is_symbol(matrix, x+1, y) or 
        is_symbol(matrix, x-1, y-1) or 
        is_symbol(matrix, x, y-1) or 
        is_symbol(matrix, x+1, y-1))
    
def is_symbol(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
        return False
    if matrix[y][x].isdigit() or matrix[y][x] == ".":
        return False
    return True

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()