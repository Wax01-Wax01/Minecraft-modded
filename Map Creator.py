"""
Hello!
Welcome to the Minecraft Map creator.
In this file, you can design maps for gamemodes!!!
Village House design:
' ', ' ', ' ', '∥', ' ', ' ', ' '
' ', ' ', '∥', ' ', '∥', ' ', ' '
' ', '∥', ' ', ' ', ' ', '∥', ' '
'|', ' ', ' ', ' ', ' ', ' ', '|'
'|', ' ', ' ', ' ', ' ', ' ', '|'
'|', ' ', ' ', ' ', ' ', ' ', '|'
'|', ' ', ' ', ' ', ' ', ' ', '|'
' ', ' ', '⊠', ' ', '◈', '◈', ' '
'∥', '∥', '∥', '∥', '∥', '∥', '∥'
"""
"""
# a, c, e, i, k, o, p, r, s
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


def display_char(left_corner_place, character_display):
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


def display_rps(player, rps_run):  # If real player, set player to 0, else set player to 1.
    index_char_displaying = 0
    for character_to_display in list(rps_run):
        display_char(410 + player * 612 + index_char_displaying * 4, character_to_display)
        index_char_displaying += 1


game = []
for i in range(2601):
    game += [' ']
place = 2503
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
k = 0
while k < 51:
    print(game[k * 51: (k + 1) * 51])
    k += 1
"""

vill_house = [
    [' '], [' '], [' '], ['∥'], [' '], [' '], [' '],  # -03 - game_size * 8 ~ +03 - game_size * 8
    [' '], [' '], ['∥'], [' '], ['∥'], [' '], [' '],  # -03 - game_size * 7 ~ +03 - game_size * 7
    [' '], ['∥'], [' '], [' '], [' '], ['∥'], [' '],  # -03 - game_size * 6 ~ +03 - game_size * 6
    ['|'], [' '], [' '], [' '], [' '], [' '], ['|'],  # -03 - game_size * 5 ~ +03 - game_size * 5
    ['|'], [' '], [' '], [' '], [' '], [' '], ['|'],  # -03 - game_size * 4 ~ +03 - game_size * 4
    ['|'], [' '], [' '], [' '], [' '], [' '], ['|'],  # -03 - game_size * 3 ~ +03 - game_size * 3
    ['|'], [' '], [' '], [' '], [' '], [' '], ['|'],  # -03 - game_size * 2 ~ +03 - game_size * 2
    [' '], [' '], ['⊠'], [' '], ['◈'], ['◈'], [' '],  # -03 - game_size * 1 ~ +03 - game_size * 1
    ['∥'], ['∥'], ['∥'], ['∥'], ['∥'], ['∥'], ['∥'],  # -03 - game_size * 0 ~ +03 - game_size * 0
]

# Evil Tower Gamemode:
# Types: '▪', '⚠'
game = []
for i in range(441):
    game += [' ']
place = 409
game[409] = '🙂'
# Lvl 1 -> Easy
# Poss. #1:
game[408] = '▪'
game[365] = '▪'
game[343] = '▪'
game[324] = '▪'
game[305] = '▪'
game[285] = '▪'
game[264] = '▪'
game[221] = '▪'
game[199] = '▪'
game[177] = '▪'
game[174] = '▪'
game[131] = '▪'
game[130] = '▪'
game[129] = '⚠'
game[128] = '▪'
game[106] = '▪'
game[85] = '▪'
game[45] = '▪'
game[47] = '▪'
game[50] = '▪'
game[30] = '▪'


k = 0
while k < 21:
    print(game[k * 21: (k + 1) * 21])
    k += 1
