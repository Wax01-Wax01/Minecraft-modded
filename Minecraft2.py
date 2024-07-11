import random
import numpy as np
# Liyong Wang want to join in this project (6/24/2024)
# blocks: ◈ is stone
# Character Length test (1): aaaaaaaaaa
# Character Length test (2):


# Entire game function
def entire_game(player_name):
    Time_Spent = 0
    game_size = 21
    vill_houses = {}  # List of villages

    # Text engine for rock paper scissors
    binary_capital_letter_codes_rps = {
        'A': '010101111101101',
        'C': '011100100100011',
        'E': '111100111100111',
        'I': '111010010010111',
        'K': '101101110101101',
        'O': '010101101101010',
        'P': '110101110100100',
        'R': '110101110101101',
        'S': '011100010001110'
    }

    # Village house model
    vill_house = [
        ' ', ' ', ' ', '∥', ' ', ' ', ' ',
        ' ', ' ', '∥', ' ', '∥', ' ', ' ',
        ' ', '∥', ' ', ' ', ' ', '∥', ' ',
        '|', ' ', ' ', ' ', ' ', ' ', '|',
        '|', ' ', ' ', ' ', ' ', ' ', '|',
        '|', ' ', ' ', ' ', ' ', ' ', '|',
        '|', ' ', ' ', ' ', ' ', ' ', '|',
        ' ', ' ', '⊠', '◈', '◈', ' ', ' ',
        '∥', '∥', '∥', '∥', '∥', '∥', '∥',
    ]


    def clear_range(start, end):  # Clears a range of blocks in the game
        game_index = start
        while game_index < end:
            game[game_index] = ' '
            game_index += 1


    def display_char(left_corner_place, character_display):  # Display a character for rock paper scissors
        x_display = 0
        y_display = 0
        index_display = 0
        for y_axis_change in range(5):
            for x_axis_change in range(3):
                if list(binary_capital_letter_codes_rps[character_display])[index_display] == '1':
                    game[left_corner_place + x_display + y_display * 51] = '◆'
                x_display += 1
                index_display += 1
            x_display = 0
            y_display += 1


    def display_rps(player, rps_run):  # If real player, set player to 0, else set player to 1. This also displays the text of rock paper scissors gamemode.
        index_char_displaying = 0
        for character_to_display in list(rps_run):
            display_char(410 + player * 612 + index_char_displaying * 4, character_to_display)
            index_char_displaying += 1


    def login():  # Login vertification test
        user_credentials = {'Wax01': 'TheSST!!!!!', 'max': "i am stupid"}
        if user_credentials.keys().__contains__(username):
            # Get username and password from the user
            password = input("Enter your password: ")

            # Check if the entered username exists and the password matches
            if username in user_credentials and user_credentials[username] == password:
                print("Login successful!")
            else:
                print("Login failed. Please check your username and password.")
                exit(0)


    def lottery():  # Lottery game
        """
        lottery.
        getting 3 A's on any line is a 1.385% chance or 1 in 72.2 chance.
        """
        import random

        MAX_LINES = 3
        MAX_BET = 100
        MIN_BET = 1

        ROWS = 3
        COLS = 3
        symbol_count = {
            'A': 3,
            'B': 4,
            'C': 5,
            'D': 6
        }

        symbol_value = {
            'A': 100,
            'B': 50,
            'C': 25,
            'D': 12
        }

        def check_winnings(columns, lines, bet, values):
            winnings = 0
            winning_lines = []
            for line in range(lines):
                symbol = columns[0][line]
                for column in columns:
                    symbol_to_check = column[line]
                    if symbol != symbol_to_check:
                        break
                else:
                    winnings += values[symbol] * bet
                    winning_lines.append(line + 1)
            return winnings, winning_lines

        def get_slot_machine_spin(rows, cols, symbols):
            all_symbols = []
            for symbol, symbol_count in symbols.items():
                for _ in range(symbol_count):
                    all_symbols.append(symbol)

            columns = []
            for _ in range(cols):
                column = []
                current_symbols = all_symbols[:]
                for _ in range(rows):
                    value = random.choice(current_symbols)
                    #current_symbols.remove(value) <- dont do dis
                    column.append(value)

                columns.append(column)

            return columns

        def print_slot_machine(columns):
            for row in range(len(columns[0])):
                for i, column in enumerate(columns):
                    if i != len(columns) - 1:
                        print(column[row], end=' | ')
                    else:
                        print(column[row], end='')
                print()

        def deposit():
            while True:
                amount = input('how much money do u want 2 deposit? $')
                if amount.isdigit():
                    amount = int(amount)
                    if amount > 0:
                        break
                    else:
                        print('invalid value! number must be above 0')
                else:
                    print('pls enter a number')
            return amount

        def get_lines():
            while True:
                lines = input(f'enter da number of lines 2 bet on (1 - {MAX_LINES}) ')
                if lines.isdigit():
                    lines = int(lines)
                    if 1 <= lines <= MAX_LINES:
                        break
                    else:
                        print(f'invalid value! number must be between 1 and {MAX_LINES} inclusive ')
                else:
                    print('pls enter a number')
            return lines

        def get_bet():
            while True:
                amount = input(f'how much money do u want 2 bet? ({MIN_BET} - {MAX_BET}) $')
                if amount.isdigit():
                    amount = int(amount)
                    if MIN_BET <= amount <= MAX_BET:
                        break
                    else:
                        print(f'invalid value! number must be between {MIN_BET} and {MAX_BET} inclusive')
                else:
                    print('pls enter a number')
            return amount

        def game(balance):
            lines = get_lines()
            while True:
                bet = get_bet()
                total_bet = bet * lines
                if total_bet > balance:
                    print('u dont have enough money')
                else:
                    break
            print(f'u r betting ${bet} on {lines} lines. total bet is equal 2 ${total_bet}')

            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
            print(f'u won ${winnings}')
            print(f'u won on', *winning_lines)
            return winnings - total_bet

        def main():
            balance = deposit()
            while True:
                print(f'current balance is ${balance}')
                spin = input('press enter 2 spin (q to quit) ')
                if spin.lower() == 'q' or spin.lower() == 'quit':
                    break
                balance += game(balance)
            print(f'u left with ${balance}')

        main()


    def convert_emoji(words):  # Converts text to face emojis
        text_split = words.split(' ')
        output = ''
        emojis = {
            ':)': '🙂', ':(': '☹️', ":\\": '😐',
            ":|": '😐', ":/": '😐', "O_O": '😮',
            ":D": '😃', "XD": '😆', ":'(": '😢',
            ":')": '🥲', ":P": '😛', ":3": '😗',
            ">:(": '🤬', ">:)": '😈', "-_-": '😑',
            "D:": '😦'
        }
        for emoji in text_split:
            output += emojis.get(emoji.upper(), emoji) + ' '
        return output


    def spawn_tree(x, y):  # Spawns a tree.
        place = (game_size**2-int(np.ceil(game_size/2))) + x - y * game_size
        k = 0
        height = random.randint(3, 7)
        while k < height:
            place -= game_size
            if place > 0:
                game[place] = '|'
            k += 1
        if place - 1 >= 1:
            game[place - 1] = '0'
        if place + 1 >= 1:
            game[place + 1] = '0'
        if place + (game_size - 1) >= 0:
            game[place + (game_size - 1)] = '0'
        if place + (game_size + 1) >= 0:
            game[place + (game_size + 1)] = '0'
        if place - game_size >= 0:
            game[place - game_size] = '0'
        if place - (game_size + 1) >= 0:
            game[place - (game_size + 1)] = '0'
        if place - (game_size - 1) >= 0:
            game[place - (game_size - 1)] = '0'
        if place - 2*game_size >= 0:
            game[place - 2*game_size] = '0'


    def spawn_village_house(x, y):  # Spawns a house
        place = (game_size**2-int(np.ceil(game_size/2))) + x - y * game_size
        increase_place = game_size * -8 - 3
        increment_block = 0
        for y_change in range(9):
            for x_change in range(7):
                if game_size ** 2 > place + increase_place >= 0:
                    game[place + increase_place] = vill_house[increment_block]
                increment_block += 1
                increase_place += 1
            increase_place += game_size - 7
        chest_items[place - game_size - 1] = []
        for i in range(len(block_count)):
            chest_items[place - game_size - 1].append(0)
        chest_items[place - game_size - 1].append(0)  # Saplings
        chest_items[place - game_size - 1].append(0)  # Flint
        chest_items[place - game_size - 1].append(0)  # Flint and Steel
        chest_items[place - game_size - 1].append(0)  # Explosive Pickaxes
        chest_items[place - game_size - 1][1] = random.randint(2, 7)
        chest_items[place - game_size - 1][2] = random.randint(5, 13)
        chest_items[place - game_size - 1][3] = random.randint(1, 4)
        chest_items[place - game_size - 1][4] = random.randint(5, 11)
        chest_items[place - game_size - 1][6] = random.randint(0, 3)
        chest_items[place - game_size - 1][7] = random.randint(0, 4)
        chest_items[place - game_size - 1][8] = random.randint(0, 2)
        chest_items[place - game_size - 1][9] = random.randint(0, 2)
        x_block_place = -3
        for block_col in range(7):
            block_place = place + x_block_place + game_size
            while True:
                if block_place < game_size ** 2:
                    if game[block_place] == ' ':
                        game[block_place] = '▪'
                    else:
                        break
                else:
                    break
                block_place += game_size
            x_block_place += 1
        x_block_place = -3
        for block_col in range(7):
            block_place = place + x_block_place - 9 * game_size
            while True:
                if block_place >= 0:
                    if game[block_place] != ' ':
                        game[block_place] = ' '
                    else:
                        break
                else:
                    break
                block_place -= game_size
            x_block_place += 1
        for x_offset in [-4, 4]:
            block_place = place + x_offset - game_size
            if game[block_place] != ' ':
                while True:
                    if block_place >= 0:
                        if game[block_place] != ' ':
                            game[block_place] = ' '
                        else:
                            break
                    else:
                        break
                    block_place -= game_size
            else:
                block_place += game_size
                while True:
                    if block_place < game_size ** 2:
                        if game[block_place] == ' ':
                            game[block_place] = '▪'
                        else:
                            break
                    else:
                        break
                    block_place += game_size


    def ban_user():  # Banning system
        hit_user = input('who do u want to ban ')
        while True:
            ban_time = input(f'how long do u ban {hit_user} (hrs) ')
            if ban_time.isdigit():
                break
            else:
                print('invalid')
        reason = input(f'y do u want 2 ban {hit_user} ')
        print(f'Ban Successful! {hit_user} has been banned for {ban_time} hours because {hit_user} {reason}')
        exit(0)


    last_move = ''
    if player_name == 0:
        user_domain = random.randint(1, 7)  # Username generator
        if user_domain == 1:
            user_domain = "01'er"
        if user_domain == 2:
            user_domain = "Wax01_g0t_"
        if user_domain == 3:
            user_domain = "1n54n1t4-"
        if user_domain == 4:
            user_domain = "G0d_play3r"
        if user_domain == 5:
            user_domain = "1nsane_gmr"
        if user_domain == 6:
            user_domain = "L0L_C4P-S"
        if user_domain == 7:
            user_domain = "Anti09'er"
        user_id = random.randint(1000, 9999)
        username = user_domain + str(user_id)
    else:
        username = player_name
    user = input(f'Your username is {username}. Do you want to change it? (Y/N) ')
    if user.upper() == 'Y' or user.upper() == 'YES':
        username = input("What's your new username? ")
    login()
    print(f'Hello {username}!')
    Server = int(np.round(10 ** random.uniform(0, 10)))
    gamemode = input('Do u want 2 play peaceful or skywars or parkour or make a server (mas) or bedwars or rock paper scissors (rps) or creative or explosion survival or \nsurvival? ')  # Gamemode to play
    if gamemode.upper() == 'MAS' or gamemode.upper() == 'MAKE A SERVER':
        Your_Server = True
        gamemode = 'peaceful'
        Server = input('What do you want your server name to be? ')
    else:
        Your_Server = False
    gamemode = gamemode.lower()
    if gamemode == 'rps':
        gamemode = 'rock paper scissors'
    chat = [f'Welcome to server {Server} in {gamemode}!', f'{username} joined', f"Tip: {random.choice(['You can do a 3 block vertical jump!', "Breaking a village house's chest can give you up to 2 diamonds!", "Craft a chest with 8 planks.", 'Explode a TNT with flint and steel!', "You won't get the items in a chest if you explode them with TNT."])}"]
    i = 1
    up_speed = 0
    last_tree = -5
    last_vill_house = -15
    Lotteries = 1  # Adds the items list
    Saplings = 0
    y_terrain = 10
    Server_Views = 0
    Flint = 0
    FlintAndSteel = 0
    ExplosivePickaxes = 0
    block_types = ['▪', '|', '0', '◈', '∥', '⊠', '∷', '⍠', '⌘', '◆', '▟', '▙', '▜', '▛', '⚠']
    block_names = ['GRASS', 'WOOD', 'LEAVES', 'STONE', 'PLANKS', 'CHESTS', 'COAL', 'IRON', 'GOLD', 'DIAMONDS', 'UPRIGHT STAIRS', 'UPLEFT STAIRS', 'DOWNRIGHT STAIRS', 'DOWNLEFT STAIRS', 'TNT']
    block_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100]
    Enemy_Bed = None
    Your_Bed = None
    G1 = 0
    G2 = 0
    chest_items = {}
    ExplosivePickEquip = False

    if gamemode.upper() == 'SKYWARS' or gamemode.upper() == 'BEDWARS':
        game_size = 21
        block_count[0:2] = 1000000, 1000000
        user_domain = random.randint(1, 7)  # Enemy name generator
        if user_domain == 1:
            user_domain = "01'er"
        if user_domain == 2:
            user_domain = "Wax01_g0t_"
        if user_domain == 3:
            user_domain = "1n54n1t4-"
        if user_domain == 4:
            user_domain = "G0d_play3r"
        if user_domain == 5:
            user_domain = "1nsane_gmr"
        if user_domain == 6:
            user_domain = "L0L_C4P-S"
        if user_domain == 7:
            user_domain = "Anti09'er"
        user_id = random.randint(1000, 9999)
        enemy_name = user_domain + str(user_id)
        chat.append(f'{enemy_name}: I will win!!!')
    game = []  # Default Game Size
    while i <= 441:
        game.append(' ')
        i += 1
    i = 0
    if gamemode.upper() == 'PEACEFUL' or gamemode.upper() == 'CREATIVE' or gamemode.upper() == 'EXPLOSION SURVIVAL' or gamemode.upper() == 'SURVIVAL':
        if gamemode.upper() == 'EXPLOSION SURVIVAL':
            game_size = 41
        else:
            game_size = int(input('How big do u want ur world 2 b??? '))
        y_terrain = int(np.floor(game_size/2))
        game = []  # World Terrain Generator
        while i <= game_size**2:
            game.append(' ')
            i += 1
        i = 0
        while i < game_size:
            super_slope = random.randint(0, 1)
            if super_slope == 0:
                if y_terrain > int(np.ceil((game_size * 5)/7)):
                    y_terrain += random.randint(-1, 0)
                elif y_terrain < int(np.floor((game_size * 2)/7)-1):
                    y_terrain += random.randint(0, 1)
                else:
                    y_terrain += random.randint(-1, 1)
            else:
                if y_terrain > int(np.ceil((game_size * 5)/7)):
                    y_terrain += random.randint(-2, 0)
                elif y_terrain < int(np.floor((game_size * 2)/7)-1):
                    y_terrain += random.randint(0, 2)
                else:
                    y_terrain += random.randint(-2, 2)
            j = y_terrain
            place = game_size * (game_size-1) + i - y_terrain * game_size
            while j >= 0:
                if y_terrain - j > random.randint(4, 5):
                    game[place] = '◈'
                    if random.randint(1, int(np.round(1.3 ** (float(abs(14 - (y_terrain - j)) + 9))))) == 1:
                        game[place] = '∷'
                    if random.randint(1, int(np.round(1.3 ** (float(abs(16 - (y_terrain - j)) + 9))))) == 1:
                        game[place] = '⍠'
                    if random.randint(1, int(np.round(1.3 ** (float(abs(23 - (y_terrain - j)) + 9))))) == 1:
                        game[place] = '⌘'
                    if random.randint(1, int(np.round(1.3 ** (float(abs(26 - (y_terrain - j)) + 9))))) == 1:
                        game[place] = '◆'
                else:
                    game[place] = '▪'
                place += game_size
                j -= 1
            tree = random.randint(1, 12 - (i - last_tree))
            if tree == 1 and i != np.floor(game_size/2):
                last_tree = i
                spawn_tree(i - (int(np.floor(game_size/2))), y_terrain)
            vill_house_random = random.randint(1, 35 - (i - last_vill_house))
            if vill_house_random == 1 and abs(i - np.floor(game_size/2)) > 3 and i - last_vill_house >= 9:
                last_vill_house = i
                vill_houses[i - (int(np.floor(game_size/2)))] = y_terrain
            if i == np.floor(game_size/2):
                ytm = y_terrain
            i += 1
        for vill_house_x, vill_house_y in vill_houses.items():
            spawn_village_house(vill_house_x, vill_house_y)
        game[(game_size**2 - int(np.ceil(game_size/2))) - (ytm + 1) * game_size] = '🙂'
        place = (game_size**2 - int(np.ceil(game_size/2))) - (ytm + 1) * game_size
    touching_ground = True
    if gamemode.upper() == 'SKYWARS':
        game[420:427] = '▪', '▪', '▪', '▪', '▪', '▪', '▪'
        game[400] = '🙂'
        game[315:319] = '▪', '▪', '▪', '▪'
        game[339] = '▪'
        game[360] = '▪'
        game[119:126] = '▪', '▪', '▪', '▪', '▪', '▪', '▪'
        game[103] = '☹️'
        game[17:21] = '▪', '▪', '▪', '▪'
        game[38] = '▪'
        game[59] = '▪'
        place = 400
    if gamemode.upper() == 'PARKOUR':
        game[399] = '🙂'
        game[420] = '▪'
        game[422] = '▪'
        game[424] = '▪'
        game[406] = '▪'
        game[431] = '▪'
        game[390] = '▪'
        game[348] = '▪'
        game[437] = '▪'
        game[398] = '▪'
        game[285] = '▪'
        game[353] = '▪'
        game[311] = '▪'
        game[269] = '▪'
        game[260] = '▪'
        game[218] = '▪'
        game[176] = '▪'
        game[254] = '▪'
        game[210] = '▪'
        game[170] = '▪'
        game[129] = '▪'
        game[85:88] = '▪', '▪', '▪'
        game[126] = '▪'
        game[91] = '▪'
        game[95] = '▪'
        game[99] = '▪'
        game[103] = '▪'
        game[82] = 'F'
        place = 399
        try:
            Wood = int(input('How much wood do you want? '))
        except ValueError:
            pass
    if gamemode == '837uc41nnc39crn' and username == 'Wax01':
        ban_user()
    if gamemode.upper() == 'BEDWARS':
        block_count[0] = 0
        block_count[1] = 5
        Lotteries = 0
        game[420:430] = '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪'
        game[399] = '|'
        game[378] = '|'
        game[357] = '|'
        game[336] = '|'
        game[315:319] = '|', '|', '|', '|'
        game[340] = '|'
        game[294:299] = '▪', '▪', '▪', '▪', '▪'
        game[319] = '▪'
        game[406] = '◈'
        barrier = []
        m = 0
        while m < 105:
            barrier.append('▪')
            m += 1
        game[168:273] = barrier
        game[437:440] = '|', '|', '|'
        game[415:420] = '▪', '▪', '▪', '▪', '▪'
        game[398] = '|'
        game[394] = '|'
        game[437 - 294:440 - 294] = '|', '|', '|'
        game[415 - 294:420 - 294] = '▪', '▪', '▪', '▪', '▪'
        game[398 - 294] = '|'
        game[394 - 294] = '|'
        game[420 - 294:430 - 294] = '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪', '▪'
        game[399 - 294] = '|'
        game[378 - 294] = '|'
        game[357 - 294] = '|'
        game[336 - 294] = '|'
        game[315 - 294:319 - 294] = '|', '|', '|', '|'
        game[340 - 294] = '|'
        game[294 - 294:299 - 294] = '▪', '▪', '▪', '▪', '▪'
        game[319 - 294] = '▪'
        game[406 - 294] = '◈'
        game[401] = '🙂'
        place = 401
        game[401 - 294] = '☹️'
        Enemy_Bed = True
        Your_Bed = True
        G1 = 0
        G2 = 0
    if gamemode.upper() == 'RPS' or gamemode.upper() == 'ROCK PAPER SCISSORS':
        user_domain = random.randint(1, 7)
        if user_domain == 1:
            user_domain = "01'er"
        if user_domain == 2:
            user_domain = "Wax01_g0t_"
        if user_domain == 3:
            user_domain = "1n54n1t4-"
        if user_domain == 4:
            user_domain = "G0d_play3r"
        if user_domain == 5:
            user_domain = "1nsane_gmr"
        if user_domain == 6:
            user_domain = "L0L_C4P-S"
        if user_domain == 7:
            user_domain = "Anti09'er"
        user_id = random.randint(1000, 9999)
        enemy_name = user_domain + str(user_id)
        chat.append(f"{enemy_name}: I'm good at rock paper scissors!!!")
        game = []
        while i <= 2601:
            game.append(' ')
            i += 1
        i = 0
        game_size = 51
        place = 2504
        game[2503] = '🙂'
        game[2551:2558] = '∥', '∥', '∥', '∥', '∥', '∥', '∥'
        game[2296], game[2302], game[2347], game[2353], game[2398], game[2404], game[2449], game[2455], game[2500] = \
            '|', '|', '|', '|', '|', '|', '|', '|', '|'
        game[2558:2565] = '▪', '▪', '▪', '▪', '▪', '▪', '▪'
        game[2245:2252] = game[2551:2558]
        game[2501:2503] = '◈', '◈'
        game[2504] = '⊠'
        game[2509:2512] = '◆', '◆', '◆'
        game[2459] = '◆'
        game[2456] = '◆'
        game[2354] = '◆'
        game[2196:2200] = '⌘', '⌘', '⌘', '⌘', '⌘'
        game[2146:2149] = '⌘', '⌘', '⌘'
        game[2096] = '⌘'
        game[2592:2599] = game[2552:2559]
        game[2585:2592] = game[2559:2566]
        game[2286:2293] = game[2246:2253]
        game[2236:2241] = game[2196:2201]
        game[2186:2189] = game[2146:2149]
        game[2136] = '⌘'
        game[2337], game[2343], game[2388], game[2394], game[2439], game[2445], game[2490], game[2496], game[2547] = \
            '|', '|', '|', '|', '|', '|', '|', '|', '|'
        game[2545:2547] = '◈', '◈'
        game[2544] = '☹️'
        game[2536:2539] = game[2510:2513]
        game[2543] = '⊠'
        game[2486] = '◆'
        game[2489] = '◆'
        game[2387] = '◆'
        game[104], game[106], game[155], game[157], game[207], game[258], game[309] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆'
        game[109], game[159], game[161], game[210], game[212], game[261], game[263], game[313] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆'
        game[112], game[114], game[163], game[165], game[214], game[216], game[265], game[267], game[316], game[317], game[318] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆'
        game[717], game[718], game[767], game[818], game[869], game[921], game[922] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆'
        game[720], game[721], game[771], game[773], game[822], game[823], game[873], game[924] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆'
        game[724], game[726], game[775], game[777], game[826], game[828], game[877], game[879], game[928], game[929], game[930] = \
            '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆', '◆'
    x_pos = (place % (game_size**2)) % game_size - int(np.floor(game_size/2))  # Coordinate converter
    y_pos = -1 * ((place % (game_size**2)) // game_size) + int(np.floor(game_size/2))

    # Where to explode TNT
    tnt_explosion_range = [-2 * game_size - 1, -2 * game_size, -2 * game_size + 1,
                           -game_size - 2, -game_size - 1, -game_size, -game_size + 1, -game_size + 2,
                           -2, -1, 0, 1, 2,
                           game_size - 2, game_size - 1, game_size, game_size + 1, game_size + 2,
                           2 * game_size - 1, 2 * game_size, 2 * game_size + 1]

    # Explosive pickaxe explosion range:
    explosive_pick_range = [-game_size, -1, 0, 1, game_size]

    def explode_tnt(tnt_x, tnt_y, explosion_range):  # Explodes TNT
        explode_origin = (game_size**2-int(np.ceil(game_size/2))) + tnt_x - tnt_y * game_size
        for explode_index in explosion_range:
            if game_size ** 2 > explode_origin + explode_index >= 0:
                if game[explode_origin + explode_index] != '🙂':
                    for block_test in range(len(block_types)):
                        if game[explode_origin + explode_index] == block_types[block_test]:
                            block_count[block_test] += 1
                    game[explode_origin + explode_index] = ' '


    hp = 20

    # Main Loop
    while i < 999:
        if not block_types.__contains__(game[(place + game_size) % (game_size**2)]) and not place + 2*game_size > game_size**2-1:  # Detects if touching the ground
            touching_ground = False
        else:
            touching_ground = True
            if not block_types.__contains__([place - game_size]) and last_move == '':
                up_speed = 0
        if (gamemode == 'explosion survival' or gamemode == 'survival') and hp < 20:  # Regeneration of health
            hp += 1

        for message in chat:  # Generates Inventory summary message and coordinates
            print(message)
        k = 0
        while k < game_size:
            print(game[k * game_size: (k + 1) * game_size])
            k += 1
        summary = 'Inventory: '
        for index in range(len(block_count)):
            summary += f'{block_count[index]} {block_names[index].lower()}, '
            if index == 1:
                summary += f'{Lotteries} lotteries, '
            if index == 2:
                summary += f'{Saplings} saplings, '
            if index == 14:
                summary += f'{Flint} flint, '
                summary += f'{FlintAndSteel} flint and steel, '
                summary += f'{ExplosivePickaxes} explosive pickaxes, '
            if index % 7 == 6:
                summary += '\n'
        if gamemode == 'explosion survival' or gamemode == 'survival':
            print('❤️' * int(np.ceil(hp / 2)))
        print(summary)
        print(str(x_pos) + ", " + str(y_pos))

        if gamemode == 'rock paper scissors':
            clear_range(408, 665)
            clear_range(1020, 1277)
        if Your_Server is True:
            print(f'Your server has {Server_Views} views!')

        if gamemode == 'bedwars' and -9 <= x_pos <= -6 and (-9 <= y_pos <= -6 or 5 <= y_pos <= 8):  # Asks for what to do.
            move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble or buy something (bs)? ")
        else:
            if gamemode == 'peaceful' or gamemode == 'survival':
                move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble or craft or use a chest (uac) or \nexplode a tnt (eat) or equip/unequip explosive pickaxe (eep)? ")
            elif gamemode == 'parkour':
                move = input("Do u want 2 jump (w), move left (a) or move right (d) or place a block (pab) or chat or gamble? ")
            elif gamemode == 'rock paper scissors':
                move = input("Do u want 2 jump (w), move left (a) or move right (d) or chat or gamble or play rock paper scissors (prps)? ")
            elif gamemode == 'creative':
                move = input(
                    "Do u want 2 move up (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or move down (s) or chat or gamble? ")
            elif gamemode == 'explosion survival':
                move = input(
                    "Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or chat or gamble? ")
            else:
                move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble? ")

        last_move = ''  # Doing the action
        if (move.upper() == 'JUMP' or move.upper() == ' ' or move.upper() == 'W' or move.upper() == 'UP'):
            if gamemode == 'creative':
                if place - game_size >= 0 and not block_types.__contains__(game[place - game_size]):
                    game[place % (game_size ** 2)] = ' '
                    place -= game_size
                    game[place % (game_size ** 2)] = '🙂'
            elif touching_ground is True:
                up_speed = 1
                last_move = 'jump'
        elif (move.upper() == 'LEFT' or move.upper() == 'A') and place % game_size != 0 and not block_types.__contains__(game[place - 1]):
            game[place % (game_size**2)] = ' '
            place -= 1
            game[place % (game_size**2)] = '🙂'
        elif (move.upper() == 'RIGHT' or move.upper() == 'D') and place % game_size != game_size - 1 and not block_types.__contains__(game[place + 1]):
            game[place % (game_size**2)] = ' '
            place += 1
            game[place % (game_size**2)] = '🙂'
        elif (move.upper() == 'S' or move.upper() == 'DOWN') and gamemode == 'creative':
            if place + game_size < game_size ** 2 and not block_types.__contains__(game[place + game_size]):
                game[place % (game_size ** 2)] = ' '
                place += game_size
                game[place % (game_size ** 2)] = '🙂'
        elif (move.upper() == 'BAB' or move.upper() == 'BREAK A BLOCK') and gamemode != 'parkour' and gamemode != 'rock paper scissors':
            x = input('x? ')
            y = input('y? ')
            try:
                place_break = (int(y) - int(np.floor(game_size/2))) * -game_size + int(x) + int(np.floor(game_size/2))
                if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and (block_types.__contains__(game[place_break])):
                    if ExplosivePickEquip:
                        explode_tnt(int(x), int(y) + (int(np.ceil(game_size / 2)) - 1), explosive_pick_range)
                    else:
                        for i in range(len(block_count)):
                            if block_types[i] == game[place_break]:
                                block_count[i] += 1
                                if game[place_break] == '0' and random.randint(1, 6) == 1:
                                    block_count[2] -= 1
                                    Saplings += 1
                                if game[place_break] == '⊠':
                                    for j in range(len(block_count)):
                                        block_count[j] += chest_items[place_break][j]
                                    Saplings += chest_items[place_break][len(block_count) + 0]
                                    Flint += chest_items[place_break][len(block_count) + 1]
                                    FlintAndSteel += chest_items[place_break][len(block_count) + 2]
                                    ExplosivePickaxes += chest_items[place_break][len(block_count) + 3]
                                    del chest_items[place_break]
                                game[place_break] = ' '
                                break
            except ValueError:
                pass
        elif (move.upper() == 'PAB' or move.upper() == 'PLACE A BLOCK') and gamemode != 'rock paper scissors' and gamemode != 'explosion survival':
            x = input('x? ')
            y = input('y? ')
            try:
                place_break = (int(y) - int(np.floor(game_size/2))) * -game_size + int(x) + int(np.floor(game_size/2))
                if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and game[place_break] == ' ':
                    block = input('Do you want to place grass or wood or leaves or saplings or stone or planks or chests or coal or iron or gold or diamonds or upright stairs \nor upleft stairs or downright stairs or downleft stairs or tnt? ')
                    for i in range(len(block_count)):
                        if block.upper() == block_names[i]:
                            if gamemode == 'creative':
                                game[place_break] = block_types[i]
                                if block.upper() == 'CHESTS':
                                    chest_items[place_break] = []
                                    for i in range(len(block_count)):
                                        chest_items[place_break].append(0)
                                    chest_items[place_break].append(0)  # Saplings
                                    chest_items[place_break].append(0)  # Flint
                                    chest_items[place_break].append(0)  # Flint and Steel
                                    chest_items[place_break].append(0)  # Explosive Pickaxes
                            elif block_count[i] > 0:
                                game[place_break] = block_types[i]
                                block_count[i] -= 1
                                if block.upper() == 'CHESTS':
                                    chest_items[place_break] = []
                                    for i in range(len(block_count)):
                                        chest_items[place_break].append(0)
                                    chest_items[place_break].append(0)  # Saplings
                                    chest_items[place_break].append(0)  # Flint
                                    chest_items[place_break].append(0)  # Flint and Steel
                                    chest_items[place_break].append(0)  # Explosive Pickaxes
                    if block.upper() == 'SAPLINGS':
                        if gamemode == 'creative':
                            spawn_tree(int(x), int(y) + (int(np.ceil(game_size/2))-2))
                        elif Saplings > 0:
                            spawn_tree(int(x), int(y) + (int(np.ceil(game_size/2))-2))
                            Saplings -= 1
            except ValueError:
                pass
        elif move.upper() == 'CHAT':
            chat_message = convert_emoji(input('What do you want to say? '))
            chat_message = f'{username}: {chat_message}'
            chat.append(chat_message)
            if chat_message.upper() == f'{username.upper()}: /GAMEMODE ':
                chat.append(f'Current gamemode is {gamemode}')
        elif move.upper() == 'GAMBLE' and Lotteries > 0 and gamemode != 'bedwars':
            lottery()
        elif (move.upper() == 'BS' or move.upper() == 'BUY SOMETHING') and gamemode == 'bedwars' and -9 <= x_pos <= -6 and (-9 <= y_pos <= -6 or 5 <= y_pos <= 8):
            buy = input('Do you want to buy 5 grass and wood for 20 lotteries (A) or 5 leaves for 50 lotteries (B) or 10 grass and wood and 2 leaves for 50 lotteries (C)? ')
            if buy.upper() == 'A' and Lotteries >= 20:
                block_count[0] += 5
                block_count[1] += 5
                Lotteries -= 20
            if buy.upper() == 'B' and Lotteries >= 50:
                block_count[2] += 5
                Lotteries -= 50
            if buy.upper() == 'C' and Lotteries >= 50:
                block_count[0] += 10
                block_count[1] += 10
                block_count[2] += 2
                Lotteries -= 50
        elif move.upper() == 'CRAFT' and (gamemode == 'peaceful' or gamemode == 'survival'):
            print('Crafting Recipes:')
            print('1. 1 wood -> 4 planks \n2. 8 planks -> 1 chest \n3. 3 planks -> 1 stair (any direction) \n4. 2 stone & 1 coal -> 1 flint \n5. 1 flint and 1 iron -> 1 flint and steel \n6. 2 planks and 3 tnt -> 1 explosive pickaxe')
            craft = input('Which recipe you want to craft? (Choose Number) ')
            if craft == '1':
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit():
                    if block_count[1] >= 1 * int(craft_count):
                        block_count[1] -= 1 * int(craft_count)
                        block_count[4] += 4 * int(craft_count)
            if craft == '2':
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit():
                    if block_count[4] >= 8 * int(craft_count):
                        block_count[4] -= 8 * int(craft_count)
                        block_count[5] += 1 * int(craft_count)
            if craft == '3':
                print('Stair types: 1. Upright Stairs, 2. Upleft Stairs, 3. Downright Stairs, 4. Downleft Stairs')
                stair_type = input('Which stair type you want to craft? (Choose Number) ')
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit() and stair_type.isdigit():
                    if 4 >= int(stair_type) >= 1:
                        if block_count[4] >= 3 * int(craft_count):
                            block_count[4] -= 3 * int(craft_count)
                            block_count[9 + int(stair_type)] += 1 * int(craft_count)
            if craft == '4':
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit():
                    if block_count[3] >= 2 * int(craft_count) and block_count[6] >= 1 * int(craft_count):
                        block_count[3] -= 2 * int(craft_count)
                        block_count[6] -= 1 * int(craft_count)
                        Flint += 1 * int(craft_count)
            if craft == '5':
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit():
                    if Flint >= 1 * int(craft_count) and block_count[7] >= 1 * int(craft_count):
                        Flint -= 1 * int(craft_count)
                        block_count[7] -= 1 * int(craft_count)
                        FlintAndSteel += 1 * int(craft_count)
            if craft == '6':
                craft_count = input(f'How many times do you want to craft recipe {craft}? ')
                if craft_count.isdigit():
                    if block_count[4] >= 2 * int(craft_count) and block_count[14] >= 3 * int(craft_count):
                        block_count[4] -= 2 * int(craft_count)
                        block_count[14] -= 3 * int(craft_count)
                        ExplosivePickaxes += 1 * int(craft_count)

        elif (move.upper() == 'USE A CHEST' or move.upper() == 'UAC') and (gamemode == 'peaceful' or gamemode == 'survival'):
            x = input('x? ')
            y = input('y? ')
            try:
                place_break = (int(y) - int(np.floor(game_size/2))) * -game_size + int(x) + int(np.floor(game_size/2))
                if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and chest_items.__contains__(place_break):
                    chest_summary = 'Chest contains: '
                    for i in range(len(block_count)):
                        chest_summary += f'{chest_items[place_break][i]} {block_names[i].lower()}, '
                        if i % 7 == 6:
                            chest_summary += '\n'
                    chest_summary += f'{chest_items[place_break][len(block_count) + 0]} saplings, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 1]} flint, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 2]} flint and steel, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 3]} explosive pickaxes'
                    print(f'Player: {summary}')
                    print(chest_summary)
                    for i in range(len(block_count)):
                        item_count = int(input(f'How much/many {block_names[i].lower()} do you want to put in the chest? '))
                        if item_count <= block_count[i]:
                            block_count[i] -= item_count
                            chest_items[place_break][i] += item_count
                    item_count = int(input(f'How many saplings do you want to put in the chest? '))
                    if item_count <= Saplings:
                        Saplings -= item_count
                        chest_items[place_break][len(block_count) + 0] += item_count
                    item_count = int(input(f'How much flint do you want to put in the chest? '))
                    if item_count <= Flint:
                        Flint -= item_count
                        chest_items[place_break][len(block_count) + 1] += item_count
                    item_count = int(input(f'How much flint and steel do you want to put in the chest? '))
                    if item_count <= FlintAndSteel:
                        FlintAndSteel -= item_count
                        chest_items[place_break][len(block_count) + 2] += item_count
                    item_count = int(input(f'How many explosive pickaxes do you want to put in the chest? '))
                    if item_count <= ExplosivePickaxes:
                        ExplosivePickaxes -= item_count
                        chest_items[place_break][len(block_count) + 3] += item_count
                    chest_summary = 'Chest contains: '
                    for i in range(len(block_count)):
                        chest_summary += f'{chest_items[place_break][i]} {block_names[i].lower()}, '
                        if i % 7 == 6:
                            chest_summary += '\n'
                    chest_summary += f'{chest_items[place_break][len(block_count) + 0]} saplings, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 1]} flint, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 2]} flint and steel, '
                    chest_summary += f'{chest_items[place_break][len(block_count) + 3]} explosive pickaxes'
                    summary = 'Inventory: '
                    for index in range(len(block_count)):
                        summary += f'{block_count[index]} {block_names[index].lower()}, '
                        if index == 1:
                            summary += f'{Lotteries} lotteries, '
                        if index == 2:
                            summary += f'{Saplings} saplings, '
                        if index == 14:
                            summary += f'{Flint} flint, '
                            summary += f'{FlintAndSteel} flint and steel, '
                            summary += f'{ExplosivePickaxes} explosive pickaxes, '
                    print(f'Player: {summary}')
                    print(chest_summary)
                    for i in range(len(block_count)):
                        item_count = int(input(f'How much/many {block_names[i].lower()} do you want to take from the chest? '))
                        if item_count <= chest_items[place_break][i]:
                            block_count[i] += item_count
                            chest_items[place_break][i] -= item_count
                    item_count = int(input(f'How many saplings do you want to take from the chest? '))
                    if item_count <= chest_items[place_break][len(block_count) + 0]:
                        Saplings += item_count
                        chest_items[place_break][len(block_count) + 0] -= item_count
                    item_count = int(input(f'How much flint do you want take from the chest? '))
                    if item_count <= chest_items[place_break][len(block_count) + 1]:
                        Flint += item_count
                        chest_items[place_break][len(block_count) + 1] -= item_count
                    item_count = int(input(f'How much flint and steel do you want take from the chest? '))
                    if item_count <= chest_items[place_break][len(block_count) + 2]:
                        FlintAndSteel += item_count
                        chest_items[place_break][len(block_count) + 2] -= item_count
                    item_count = int(input(f'How many explosive pickaxes do you want take from the chest? '))
                    if item_count <= chest_items[place_break][len(block_count) + 3]:
                        ExplosivePickaxes += item_count
                        chest_items[place_break][len(block_count) + 3] -= item_count
            except ValueError:
                pass
        elif (move.upper() == 'PRPS' or move.upper() == 'PLAY ROCK PAPER SCISSORS') and gamemode == 'rock paper scissors':
            rps_move = input('Do you want to play rock (r), paper (p), or scissors (s)? ')
            if rps_move.upper() == 'R' or rps_move.upper() == 'ROCK':
                rps_move = 'ROCK'
            if rps_move.upper() == 'P' or rps_move.upper() == 'PAPER':
                rps_move = 'PAPER'
            if rps_move.upper() == 'S' or rps_move.upper() == 'SCISSORS':
                rps_move = 'SCISSORS'
            if ['ROCK', 'PAPER', 'SCISSORS'].__contains__(rps_move):
                cpu_rps_move = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
                display_rps(0, rps_move)
                display_rps(1, cpu_rps_move)
                chat.append(f'{username}: {rps_move.lower().capitalize()}!')
                chat.append(f'{enemy_name}: {cpu_rps_move.lower().capitalize()}!')
                if rps_move == cpu_rps_move:
                    chat.append('Server: Tie!')
                elif (rps_move == 'ROCK' and cpu_rps_move == 'SCISSORS') or (rps_move == 'PAPER' and cpu_rps_move == 'ROCK') or (rps_move == 'SCISSORS' and cpu_rps_move == 'PAPER'):
                    chat.append(f'Server: {username} wins!')
                else:
                    chat.append(f'Server: {enemy_name} wins!')
        elif (move.upper() == 'EAT' or move.upper() == 'EXPLODE A TNT') and FlintAndSteel >= 1 and (gamemode == 'peaceful' or gamemode == 'survival'):
            x = input('x? ')
            y = input('y? ')
            try:
                place_break = (int(y) - int(np.floor(game_size / 2))) * -game_size + int(x) + int(np.floor(game_size / 2))
                if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and game[place_break] == '⚠':
                    explode_tnt(int(x), int(y) + (int(np.ceil(game_size / 2)) - 1), tnt_explosion_range)
                    block_count[14] -= 1
            except ValueError:
                pass
        elif move.upper() == 'QUIT':
            break
        elif ['EEP', 'EQUIP EXPLOSIVE PICKAXE', 'UNEQUIP EXPLOSIVE PICKAXE', 'EQUIP/UNEQUIP EXPLOSIVE PICKAXE'].__contains__(move.upper()):
            if ExplosivePickaxes <= 0:
                print('No Explosive Pickaxe found. Craft one with 2 Planks and 3 TNT.')
            else:
                if ExplosivePickEquip:
                    ExplosivePickEquip = False
                    print('Successfully Unequiped Explosive Pickaxe')
                else:
                    ExplosivePickEquip = True
                    print('Successfully Equipped Explosive Pickaxe')

        game[place % (game_size**2)] = ' '  # Adds Gravity
        if up_speed > 0 and gamemode != 'creative':
            i = 0
            while i < up_speed:
                game[place % (game_size**2)] = ' '
                place -= game_size
                if not block_types.__contains__(game[place]) and place - game_size >= 0:
                    game[place] = '🙂'
                else:
                    place += game_size
                i += 1
        if up_speed < 0 and gamemode != 'creative':
            i = 0
            while i < -1 * up_speed:
                game[place % (game_size**2)] = ' '
                place += game_size
                if not block_types.__contains__(game[place]) and place + game_size < game_size**2:
                    game[place] = '🙂'
                else:
                    place -= game_size
                    if gamemode == 'explosion survival' or gamemode == 'survival':
                        hp += np.ceil((int(np.ceil(up_speed + 0.1)) * -(int(np.ceil(up_speed + 0.1)) - 1)) / 2)
                i += 1
            if (gamemode == 'explosion survival' or gamemode == 'survival') and place + game_size < game_size ** 2:
                if block_types.__contains__(game[place + game_size]):
                    hp += np.ceil((int(np.ceil(up_speed + 0.1)) * -(int(np.ceil(up_speed + 0.1)) - 1)) / 2)
        game[place % (game_size**2)] = '🙂'
        if touching_ground is False:
            up_speed -= 1

        x_pos = int((place % (game_size**2)) % game_size - np.floor(game_size/2))  # Coordinate Converter
        y_pos = int(-1 * ((place % (game_size**2)) // game_size) + np.floor(game_size/2))

        if gamemode == 'skywars' and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):  # More gamemode functionality
            print('You Died! You fell into the void!')
            break
        if gamemode == 'parkour' and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
            print('You Died! You fell into the void!')
            break
        if gamemode == 'bedwars' and Your_Bed is False and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
            print('You Died! You fell into the void!')
            break
        if gamemode == 'bedwars' and Your_Bed is True and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
            game[place] = ' '
            place = 401
            game[place] = '🙂'
        if gamemode == 'explosion survival' and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
            print(f'You died! You fell into the void! You survived {Time_Spent} seconds!')
            break
        if game.__contains__('☹️') is False and gamemode == 'skywars':
            print('YOU WIN!!!')
            break
        if game.__contains__('F') is False and gamemode == 'parkour':
            print('YOU WIN!!!')
            break
        if Your_Server is True:
            Server_Views += random.randint(0, Time_Spent)
        Time_Spent += 1
        if gamemode == 'bedwars':
            G1 += 1
            G2 += 1
        if gamemode == 'bedwars' and Your_Bed is True:
            if game[406] != '◈':
                Your_Bed = False
                chat.append('Your bed was destroyed. You will no longer respawn.')
        if gamemode == 'bedwars' and Enemy_Bed is True:
            if game[406-294] != '◈':
                Enemy_Bed = False
                chat.append(f"{enemy_name}'s bed was destroyed. They will no longer respawn.")
        if gamemode == 'bedwars' and Enemy_Bed is True and place != 401-294:
            game[401-294] = '☹️'
        if game.__contains__('☹️') is False and gamemode == 'bedwars' and Enemy_Bed is False:
            print('YOU WIN!!!')
            break
        if place == 396:
            Lotteries += G1
            G1 = 0
        if place == 396-294:
            Lotteries += G2
            G2 = 0
        if Time_Spent == 60 and gamemode == 'bedwars':
            chat.append('Beds will be gone in 3 minutes!')
        if Time_Spent == 120 and gamemode == 'bedwars':
            chat.append('Beds will be gone in 2 minutes!')
        if Time_Spent == 180 and gamemode == 'bedwars':
            chat.append('Beds will be gone in 60 seconds!')
        if Time_Spent == 210 and gamemode == 'bedwars':
            chat.append('Beds will be gone in 30 seconds!')
        if Time_Spent == 230 and gamemode == 'bedwars':
            chat.append('Beds will be gone in 10 seconds!')
        if Time_Spent == 240 and gamemode == 'bedwars':
            chat.append('Beds gone!')
            game[406] = ' '
            Your_Bed = False
            game[406-294] = ' '
            Enemy_Bed = False
        if gamemode == 'rock paper scissors' and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
            game[place] = ' '
            place = 2504
            game[place] = '🙂'
        if gamemode.upper() == 'EXPLOSION SURVIVAL':
            explode_tnt(random.randint(-20, 20), random.randint(0, 40), tnt_explosion_range)
        if (gamemode == 'explosion survival' or gamemode == 'survival') and hp <= 0:
            print(f'You died, you lost all your health! You survived {Time_Spent} seconds!')
            break

        hp = int(hp)

    print('Process finished with exit code 69420')  # Fake ending message
    return username


global_username = entire_game(0)
while True:
    if ['YES', 'Y'].__contains__(input('\nDo you want to play again? (Y/N) ').upper()):
        global_username = entire_game(global_username)
    else:
        break
print('Thanks for playing!')
