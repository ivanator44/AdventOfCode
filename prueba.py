import re

with open('inputDay2.txt', 'r') as file:

    max_red = 12
    max_green = 13
    max_blue = 14

    valid_games_ids_sum = 0

    for line in file:

        # Pattern to match game ID and color-number pairs
        pattern_game = r'Game (\d+):((?: \d+ [a-zA-Z]+[,;])+)'

        match_game = re.match(pattern_game, line.strip())

        if match_game:
            game_id, color_number_pairs = match_game.groups()
            color_number_pairs = re.findall(r'(\d+) ([a-zA-Z]+)[,;]', color_number_pairs)

            valid_game = True

            for number, color in color_number_pairs:
                if color == 'red' and int(number) > max_red:
                    valid_game = False
                elif color == 'green' and int(number) > max_green:
                    valid_game = False
                elif color == 'blue' and int(number) > max_blue:
                    valid_game = False

            if valid_game:
                valid_games_ids_sum += int(game_id)

    print("Sum of IDs of valid games:", valid_games_ids_sum)

    
