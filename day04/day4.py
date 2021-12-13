import pprint

pp = pprint.PrettyPrinter(indent=6)
with open('day4list.txt', 'r') as fp:
    bingo_list = [int(x) for x in fp.readline().split(",")]

bingo_boards = [[]]
with open('day4boards.txt', 'r') as fp:
    i = 0
    for line in fp:
        if line =="\n":
            i += 1
            bingo_boards.append([])
        else:
            bingo_boards[i].append([int(x) for x in line.split()])

pp.pprint(bingo_boards)

for b in bingo_list:
    BINGO = False
    BINGO_BOARD = None
    CALLED = b
    for i in range(len(bingo_boards)):
        for j in range(0,5):
            for k in range(0,5):
                if bingo_boards[i][j][k] == b:
                    bingo_boards[i][j][k] = "X"
                    v_check = True
                    h_check = True 
                    for l in range(0,5):
                        if not (v_check and bingo_boards[i][l][k] == "X"):
                            v_check = False
                        if not (h_check and bingo_boards[i][j][l] == "X"):
                            h_check = False

                    if h_check or v_check:
                        BINGO = True
                        BINGO_BOARD = i
    if BINGO:
        break

pp.pprint(bingo_boards[BINGO_BOARD])
sums = 0
for i in range(0,5):
    sums += sum([x for x in bingo_boards[BINGO_BOARD][i] if  isinstance(x,int)])

print(sums * CALLED)
