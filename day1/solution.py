#!/usr/bin/env python3

from os import path

def main():

    number_dict = {        
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    sum_partI = 0
    sum_partII = 0

    for line in get_input():

        number_partI = ''
        number_partII = ''

        for idx, character in enumerate(line):

            if character.isnumeric():
                number_partI += character
                number_partII += character
                
            for string_number in number_dict:
                if line[idx:].startswith(string_number):
                    number_partII += number_dict[string_number]
        
        sum_partI += int(number_partI[0] + number_partI[len(number_partI)-1])
        sum_partII += int(number_partII[0] + number_partII[len(number_partII)-1])
 
    print(f'Part I - Sum: {sum_partI}')
    print(f'Part II - Sum: {sum_partII}')

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()