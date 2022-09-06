treasure_map = ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}\n")

treasure_pos = input("Where would you like to put the treasure chest? (Input as XY): ")

treasure_map[int(treasure_pos[1]) - 1][int(treasure_pos[0]) - 1] = 'X'

print(f"{treasure_map[0]}\n{treasure_map[1]}\n{treasure_map[2]}\n")