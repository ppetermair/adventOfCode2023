#!/usr/bin/env python3

from os import path

def main():

    red_count = 12
    green_count = 13
    blue_count = 14
    possible_game_ids = []
    game_powers = []

    for line in get_input():
        game_info = line.split(": ")[1].split("; ")
        game_id = int(line.split(":")[0].split()[1])
        if is_possible(game_info, red_count, green_count, blue_count):
            possible_game_ids.append(game_id)
        game_powers.append(get_power(game_info))

    print(f'Part I {sum(possible_game_ids)}')
    print(f'Part II {sum(game_powers)}')

def is_possible(game, red_count, green_count, blue_count):
    for subset in game:
        current_red, current_green, current_blue = 0, 0, 0
        count_and_colors = subset.split(", ")
        for count_and_color in count_and_colors:
            count, color = count_and_color.split(' ')
            if color == "red":
                current_red += int(count)
            elif color == "green":
                current_green += int(count)
            elif color == "blue":
                current_blue += int(count)
        if current_red > red_count or current_green > green_count or current_blue > blue_count:
            return False
    return True

def get_power(game):
    min_red, min_green, min_blue = 1, 1, 1
    for subset in game:
        count_and_colors = subset.split(", ")
        for count_and_color in count_and_colors:
            count, color = count_and_color.split(' ')
            if color == "red" and int(count) > min_red:
                min_red = int(count)
            elif color == "green" and int(count) > min_green:
                min_green = int(count)
            elif color == "blue" and int(count) > min_blue:
                min_blue = int(count)
    return min_red * min_green * min_blue

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()