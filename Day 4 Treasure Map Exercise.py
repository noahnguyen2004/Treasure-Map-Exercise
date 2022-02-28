# Treasure Map
# column 2, row 3 would be entered as: 23
#Example Output 1
#['⬜️', '⬜️', '⬜️']
#['⬜️', '⬜️', '⬜️']
#['⬜️', 'X', '⬜️']

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# using subscript inside a string
column = position[0]         # column
row = position[1]            # row

treasure_put = map[int(row)-1][int(column)-1] = "X"
print(f"{row1}\n{row2}\n{row3}")









