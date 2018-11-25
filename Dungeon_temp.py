import os
import random

SMALL_CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),
(0,1),(1,1),(2,1),(3,1),(4,1),
(0,2),(1,2),(2,2),(3,2),(4,2),
(0,3),(1,3),(2,3),(3,3),(4,3),
(0,4),(1,4),(2,4),(3,4),(4,4)
]

MEDIUM_CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),
(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),
(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),
(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),
(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),
(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),
(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),
]

LARGE_CELLS = [
(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(12,0),
(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),
(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),(12,2),
(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(12,3),
(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(12,4),
(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5),(7,5),(8,5),(9,5),(10,5),(11,5),(12,5),
(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6),(10,6),(11,6),(12,6),
(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),(12,7),
(0,8),(1,8),(2,8),(3,8),(4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),(11,8),(12,8),
(0,9),(1,9),(2,9),(3,9),(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),
(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10),(11,10),(12,10),
(0,11),(1,11),(2,11),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11),(11,11),(12,11),
(0,12),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(10,12),(11,12),(12,12)
]

ALL_MONSTERS = []
ALL_MOVES = []
ALL_VALID_MONSTER_MOVES = []
MOVES = ['A', 'D', 'W', 'S']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_location():
    map_size = input("Pick your map size [Small|Medium|Large] \u261E ")
    custom_cells = []
    k = 3
    if map_size.lower() == "small":
        custom_cells = SMALL_CELLS
    if map_size.lower() == "medium":
        custom_cells = MEDIUM_CELLS
    if map_size.lower() == "large":
        custom_cells = LARGE_CELLS
    return random.sample(custom_cells, k), custom_cells

def move_player(player, move):
    x, y = player
    if move == "A":
        x -= 1
    if move == "D":
        x += 1
    if move == "W":
        y -= 1
    if move == "S":
        y += 1
    return x, y

def move_monster(monster, move):
    x, y = monster
    if move[0] == "A":
        x -= 1
    if move[0] == "D":
        x += 1
    if move[0] == "W":
        y -= 1
    if move[0] == "S":
        y += 1
    return x, y

def get_moves_monster(monster, custom_cells):
    moves_monster = ['A', 'D', 'W', 'S']
    x, y = monster
    if custom_cells == SMALL_CELLS:
        right_limit = 4
        if x == 0:
            moves_monster.remove("A")
        elif x == right_limit:
            moves_monster.remove("D")
        if y == 0:
            moves_monster.remove("W")
        elif y == right_limit:
            moves_monster.remove("S")
        return moves_monster
    if custom_cells == MEDIUM_CELLS:
        right_limit = 8
        if x == 0:
            moves_monster.remove("A")
        elif x == right_limit:
            moves_monster.remove("D")
        if y == 0:
            moves_monster.remove("W")
        elif y == right_limit:
            moves_monster.remove("S")
        return moves_monster
    if custom_cells == LARGE_CELLS:
        right_limit = 12
        if x == 0:
            moves_monster.remove("A")
        elif x == right_limit:
            moves_monster.remove("D")
        if y == 0:
            moves_monster.remove("W")
        elif y == right_limit:
            moves_monster.remove("S")
        return moves_monster

def get_moves_player(player, custom_cells):
    moves_player = ['A', 'D', 'W', 'S']
    x, y = player
    if custom_cells == SMALL_CELLS:
        right_limit = 4
        if x == 0:
            moves_player.remove("A")
        elif x == right_limit:
            moves_player.remove("D")
        elif y == 0:
            moves_player.remove("W")
        elif y == right_limit:
            moves_player.remove("S")
        return moves_player
    if custom_cells == MEDIUM_CELLS:
        right_limit = 8
        if x == 0:
            moves_player.remove("A")
        elif x == right_limit:
            moves_player.remove("D")
        elif y == 0:
            moves_player.remove("W")
        elif y == right_limit:
            moves_player.remove("S")
        return moves_player
    if custom_cells == LARGE_CELLS:
        right_limit = 12
        if x == 0:
            moves_player.remove("A")
        elif x == right_limit:
            moves_player.remove("D")
        elif y == 0:
            moves_player.remove("W")
        elif y == right_limit:
            moves_player.remove("S")
        return moves_player

def draw_map(player, custom_cells):
    global ALL_MONSTERS
    if custom_cells == SMALL_CELLS:
        tile = "{} "
        for cell in custom_cells:
            x, y = cell
            if x < 4:
                line_end = ""
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            else:
                line_end = "\n"
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            print(output, end=line_end)
    if custom_cells == MEDIUM_CELLS:
        tile = "{} "
        for cell in custom_cells:
            x, y = cell
            if x < 8:
                line_end = ""
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            else:
                line_end = "\n"
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            print(output, end=line_end)
    if custom_cells == LARGE_CELLS:
        tile = "{} "
        for cell in custom_cells:
            x, y = cell
            if x < 12:
                line_end = ""
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            else:
                line_end = "\n"
                if cell == player:
                    output = tile.format("\U0001F3C3")
                elif cell in ALL_MONSTERS:
                    output = tile.format("\U0001F47F")
                else:
                    output = tile.format("\u2589")
            print(output, end=line_end)

def new_monster(custom_cells, player):
    global ALL_MOVES, ALL_MONSTERS
    if custom_cells == SMALL_CELLS:
        if len(ALL_MOVES) == 0:
            print("** New monster will appear in 3 moves **")
        elif len(ALL_MOVES) % 3 == 1:
            print("** New monster will appear in 2 moves **")
        elif len(ALL_MOVES) % 3 == 2:
            print("** New monster will appear in 1 moves **")
        elif len(ALL_MOVES) % 3 == 0:
            print("** New monster will appear in 3 moves **")
            seq = custom_cells.copy()
            seq.remove(player)
            random_monster = random.choice(seq)
            ALL_MONSTERS.append(random_monster)
        return ALL_MONSTERS
    if custom_cells == MEDIUM_CELLS:
        if len(ALL_MOVES) == 0:
            print("** New monster will appear in 5 moves **")
        elif len(ALL_MOVES) % 5 == 1:
            print("** New monster will appear in 4 moves **")
        elif len(ALL_MOVES) % 5 == 2:
            print("** New monster will appear in 3 moves **")
        elif len(ALL_MOVES) % 5 == 3:
            print("** New monster will appear in 2 moves **")
        elif len(ALL_MOVES) % 5 == 4:
            print("** New monster will appear in 1 moves **")
        elif len(ALL_MOVES) % 5 == 0:
            print("** New monster will appear in 5 moves **")
            seq = custom_cells.copy()
            seq.remove(player)
            random_monster = random.choice(seq)
            ALL_MONSTERS.append(random_monster)
        return ALL_MONSTERS
    if custom_cells == LARGE_CELLS:
        if len(ALL_MOVES) == 0:
            print("** New monster will appear in 7 moves **")
        elif len(ALL_MOVES) % 7 == 1:
            print("** New monster will appear in 6 moves **")
        elif len(ALL_MOVES) % 7 == 2:
            print("** New monster will appear in 5 moves **")
        elif len(ALL_MOVES) % 7 == 3:
            print("** New monster will appear in 4 moves **")
        elif len(ALL_MOVES) % 7 == 4:
            print("** New monster will appear in 3 moves **")
        elif len(ALL_MOVES) % 7 == 5:
            print("** New monster will appear in 2 moves **")
        elif len(ALL_MOVES) % 7 == 6:
            print("** New monster will appear in 1 moves **")
        elif len(ALL_MOVES) % 7 == 0:
            print("** New monster will appear in 7 moves **")
            seq = custom_cells.copy()
            seq.remove(player)
            random_monster = random.choice(seq)
            ALL_MONSTERS.append(random_monster)
        return ALL_MONSTERS

def monster_moves_update(custom_cells):
    global ALL_VALID_MONSTER_MOVES
    for monster in ALL_MONSTERS:
        valid_moves = get_moves_monster(monster, custom_cells)
        ALL_VALID_MONSTER_MOVES.append(valid_moves)
    return ALL_VALID_MONSTER_MOVES

def monsters_location_update():
    global ALL_MONSTERS, ALL_VALID_MONSTER_MOVES
    i = 0
    for monster in ALL_MONSTERS:
        monster_move = random.choice(ALL_VALID_MONSTER_MOVES[i])
        monster = move_monster(monster, monster_move)
        ALL_MONSTERS[i] = monster
        i += 1
        return ALL_MONSTERS

def game_loop():
    global ALL_MOVES, ALL_MONSTERS, ALL_VALID_MONSTER_MOVES
    location, custom_cells = get_location()
    monster, door, player = location
    playing = True
    ALL_MONSTERS.append(monster)
    while playing:
        draw_map(player, custom_cells)
        valid_player_moves = get_moves_player(player, custom_cells)
        valid_monster_moves = get_moves_monster(monster, custom_cells)

        print("You're currently in room {}".format(player))
        print("You can move {} by entering {}".format(", ".join(["Right", "Left", "Up", "Down"]),", ".join(["A", "D", "W", "S"])))
        print("Enter Q to quit")

        player_move = input(">> ")
        player_move = player_move.upper()
        ALL_MOVES.append(player_move)
        clear_screen()

        # Check for input
        for move in valid_player_moves:
            valid_moves = set()
            valid_moves.add(move)
        if player_move in valid_player_moves:
            player = move_player(player, player_move)
            new_monster(custom_cells, player)
            monster_moves_update(custom_cells)
            monsters_location_update()

            if player in ALL_MONSTERS:
                print("** The monster got you!")
                play_again = input("Play again? [Y/N]")
                if play_again.lower() != "n":
                    ALL_MONSTERS.clear()
                    ALL_MOVES.clear()
                    ALL_VALID_MONSTER_MOVES.clear()
                    game_loop()
                else:
                    playing = False
                    clear_screen()
            if player == door:
                print("** You escaped! Congratualation!")
                play_again = input("Play again? [Y/N]")
                if play_again.lower() != "n":
                    ALL_MONSTERS.clear()
                    ALL_MOVES.clear()
                    ALL_VALID_MONSTER_MOVES.clear()
                    game_loop()
                else:
                    playing = False
                    clear_screen()
        elif player_move in {'A', 'D', 'W', 'S'} - valid_moves:
             player_move = input("** Don't run to the wall!!")
        elif player_move.upper() == 'Q':
            print("** See you next time!**")
            playing = False
        elif player_move.upper() not in ['A', 'D', 'W', 'S', 'Q']:
            print("** Please enter a valid move!")
        else:
            if input("Play again? [Y/N] >> ").lower() != "n":
                game_loop()
            else:
                playing = False

clear_screen()
print("Welcome to the Dungeon!")
input("Press Enter to start >>")
clear_screen()
game_loop()