import random
import numpy as np

# blocks: ◈ is stone
Time_Spent = 0
game_size = 21


def login():
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


def lottery():
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


def convert_emoji(words):
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


def spawn_tree(x, y):
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
    if place + (game_size - 1) >= 1:
        game[place + (game_size - 1)] = '0'
    if place + (game_size + 1) >= 1:
        game[place + (game_size + 1)] = '0'
    if place - game_size >= 1:
        game[place - game_size] = '0'
    if place - (game_size + 1) >= 1:
        game[place - (game_size + 1)] = '0'
    if place - (game_size - 1) >= 1:
        game[place - (game_size - 1)] = '0'
    if place - 2*game_size >= 1:
        game[place - 2*game_size] = '0'


def ban_user():
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
username = user_domain + str(user_id)
user = input(f'Your username is {username}. Do you want to change it? (Y/N) ')
if user.upper() == 'Y' or user.upper() == 'YES':
    username = input("What's your new username? ")
login()
print(f'Hello {username}!')
Server = int(np.round(10 ** random.uniform(0, 10)))
gamemode = input('Do u want 2 play peaceful or skywars or parkour or make a server (mas) or bedwars? ')
if gamemode.upper() == 'MAS' or gamemode.upper() == 'MAKE A SERVER':
    Your_Server = True
    gamemode = 'peaceful'
    Server = input('What do you want your server name to be? ')
else:
    Your_Server = False
chat = [f'Welcome to server {Server} in {gamemode}!', f'{username} joined', 'Tip: ▪ = grass, | = wood, 0 = leaves, ◈ = stone, ∥ = planks']
i = 1
up_speed = 0
last_tree = -5
Lotteries = 1
Saplings = 0
y_terrain = 10
Server_Views = 0
block_types = ['▪', '|', '0', '◈', '∥', '⊠']
block_names = ['GRASS', 'WOOD', 'LEAVES', 'STONE', 'PLANKS', 'CHESTS']
block_count = [0, 0, 0, 0, 0, 0]
Enemy_Bed = None
Your_Bed = None
G1 = 0
G2 = 0
if gamemode == 'skywars' or gamemode == 'bedwars':
    block_count[0:2] = 1000000
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
    chat.append(f'{enemy_name}: I will win!!!')
game = []
while i <= 441:
    game.append(' ')
    i += 1
i = 0
if gamemode == 'peaceful':
    game_size = int(input('How big do u want ur world 2 b??? '))
    y_terrain = int(np.floor(game_size/2))
    game = []
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
            else:
                game[place] = '▪'
            place += game_size
            j -= 1
        tree = random.randint(1, 12 - (i - last_tree))
        if tree == 1 and i != np.floor(game_size/2):
            last_tree = i
            spawn_tree(i - (int(np.floor(game_size/2))), y_terrain)
        if i == np.floor(game_size/2):
            ytm = y_terrain
        i += 1
    game[(game_size**2 - int(np.ceil(game_size/2))) - (ytm + 1) * game_size] = '🙂'
    place = (game_size**2 - int(np.ceil(game_size/2))) - (ytm + 1) * game_size
touching_ground = True
if gamemode == 'skywars':
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
if gamemode == 'parkour':
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
if gamemode == 'bedwars':
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
x_pos = (place % (game_size**2)) % game_size - int(np.floor(game_size/2))
y_pos = -1 * ((place % (game_size**2)) // game_size) + int(np.floor(game_size/2))
while i < 999:
    if not block_types.__contains__(game[(place + game_size) % (game_size**2)]) and not place + 2*game_size > game_size**2-1:
        touching_ground = False
    else:
        touching_ground = True
        if not block_types.__contains__([place - game_size]) and last_move == '':
            up_speed = 0
    for message in chat:
        print(message)
    k = 0
    while k < game_size:
        print(game[k * game_size: (k + 1) * game_size])
        k += 1
    summary = 'Inventory: '
    for index in range(len(block_count)):
        summary += f'{block_count[index]} {block_names[index].lower()}, '
    print(summary)
    print(str(x_pos) + ", " + str(y_pos))
    if Your_Server is True:
        print(f'Your server has {Server_Views} views!')
    if gamemode == 'bedwars' and -9 <= x_pos <= -6 and (-9 <= y_pos <= -6 or 5 <= y_pos <= 8):
        move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble or buy something (bs)? ")
    else:
        if gamemode != 'peaceful':
            move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble? ")
        else:
            move = input("Do u want 2 jump (w), move left (a) or move right (d) or break a block (bab) or place a block (pab) or chat or gamble or craft? ")
    last_move = ''
    if (move.upper() == 'JUMP' or move.upper() == ' ' or move.upper() == 'W') and touching_ground is True:
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
    elif (move.upper() == 'BAB' or move.upper() == 'BREAK A BLOCK') and gamemode != 'parkour':
        x = input('x? ')
        y = input('y? ')
        try:
            place_break = (int(y) - int(np.floor(game_size/2))) * -game_size + int(x) + int(np.floor(game_size/2))
            if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and (block_types.__contains__(game[place_break])):
                for i in range(len(block_count)):
                    if block_types[i] == game[place_break]:
                        block_count[i] += 1
                        if game[place_break] == '0' and random.randint(1, 6) == 1:
                            block_count[2] -= 1
                            Saplings += 1
                        game[place_break] = ' '
                        break
        except ValueError:
            pass
    elif move.upper() == 'PAB' or move.upper() == 'PLACE A BLOCK':
        x = input('x? ')
        y = input('y? ')
        try:
            place_break = (int(y) - int(np.floor(game_size/2))) * -game_size + int(x) + int(np.floor(game_size/2))
            if ((int(x_pos) - int(x)) ** 2 + (int(y_pos) - int(y)) ** 2) ** 0.5 < 2.9 and game[place_break] == ' ':
                block = input('Do you want to place grass or wood or leaves or saplings or stone or planks or chests? ')
                for i in range(len(block_count)):
                    if block.upper() == block_names[i]:
                        if block_count[i] > 0:
                            game[place_break] = block_types[i]
                            block_count[i] -= 1
                if block.upper() == 'SAPLINGS' and Saplings > 0:
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
    elif move.upper() == 'CRAFT' and gamemode == 'peaceful':
        print('Crafting Recipes:')
        print('1. 1 wood -> 4 planks')
        craft = input('Which recipe you want to craft? (Choose Number) ')
        if craft == '1':
            craft_count = input(f'How many times do you want to craft recipe {craft}? ')
            if craft_count.isdigit():
                if block_count[1] >= 1 * int(craft_count):
                    block_count[1] -= 1 * int(craft_count)
                    block_count[4] += 4 * int(craft_count)
    game[place % (game_size**2)] = ' '
    if up_speed > 0:
        i = 0
        while i < up_speed:
            game[place % (game_size**2)] = ' '
            place -= game_size
            if not block_types.__contains__(game[place]) and place - game_size >= 0:
                game[place] = '🙂'
            else:
                place += game_size
            i += 1
    if up_speed < 0:
        i = 0
        while i < -1 * up_speed:
            game[place % (game_size**2)] = ' '
            place += game_size
            if not block_types.__contains__(game[place]) and place + game_size < game_size**2:
                game[place] = '🙂'
            else:
                place -= game_size
            i += 1
    game[place % (game_size**2)] = '🙂'
    if touching_ground is False:
        up_speed -= 1
    x_pos = int((place % (game_size**2)) % game_size - np.floor(game_size/2))
    y_pos = int(-1 * ((place % (game_size**2)) // game_size) + np.floor(game_size/2))
    if gamemode == 'skywars' and place + 2*game_size > game_size**2-1 and not block_types.__contains__(game[(place + game_size) % (game_size**2)]):
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
print('Process finished with exit code 69421')
exit("RED TEXT >:)")
