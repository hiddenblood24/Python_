# mohsen marandy  ----> mohsenmarandy@gmail.com
# you can search diffrent suduku on internet and use it here
board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7],]

def solve(bo):
    find=find_empty(bo)

    if find is None:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo,num,pos):

#     check row satr
    row = pos[0]

    col = pos[1]

    for i in range(len(bo[0])):
        if bo[row][i] == num :
            return False
#     check column  soton
    for i in range(len(bo)):
        if bo[i][col] == num :
            return False
#     check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo):
    for k in range(0,9):
        print()
        if (k)%3==0 and k:
            print(7*"---")
        for i in range(0,9):
            print(bo[k][i],end=' ')
            for j in range(1):
                if (i+1) % 3 == 0 and i !=8 :
                    print('|', end=' ')



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return i,j # row , col

    return None






print_board(board)
print()

solve(board)
print()
print("Answer is : ")
print_board(board)
print()

