#Nikolaos Laloutsos, A.M. 5266
board=[['  ','1  ','2  ','3  ','4  ','5  ','6  ','7  '],
       ['A ','   ','   ','1  ','1  ','1  ','  ','  '],
       ['B ','   ','   ','1  ','1  ','1  ','  ','  ','  '],
       ['C ','1  ','1  ','1  ','1  ','1  ','1  ','1  ','  ',' '],
       ['D ','1  ','1  ','1  ','0  ','1  ','1  ','1  ','  ',' '],
       ['E ','1  ','1  ','1  ','1  ','1  ','1  ','1  ','  ',' '],
       ['F ','   ','   ','1  ','1  ','1  ',' ','  ','  '],
       ['G ','   ','   ','1  ','1  ','1  ','  ','  ','  '],
       ['  ','   ','   ','   ','   ','   ','  ','  ','  '],
       ['  ','   ','   ','   ','   ','   ','  ','  ','  ']]
voc1={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7}
voc2={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7}
direct=['L','R','U','D','l','r','u','d']
pegs=['1  ','0  ']
lines=['A','B','C','D','E','F','G','a','b','c','d','e','f','g']
column=['1','2','3','4','5','6','7']
def printboard():
    for x in range(0,len(board)):
        s=''
        for y in range(0,len(board[x])):
            s+=board[x][y]
        print(s)
def score():
    score=-1
    for i in range(8):
        for j in range(8):
            if board[i][j]=='1  ':
                score+=1
            else:
                pass
    print('No more moves,the amount of remaining pegs is',score)
def move_again():
    while finish_game()==True:
        s=input('Enter peg position followed by move (L, R, U, or D): ')
        if s=='':
            print('Something went wrong with your input!')
            move_again()
            break
        elif len(s)==1:
            print('Something went wrong with your input!')
            move_again()
            break
        else:
            y=list(s)
            if invalid_input(y[0],y[1],y)==True:
                h=y[0]
                n=voc1[h]
                move(y[0],y[1],y[2],n)
                move_again()
                break
            else:
                print('Something went wrong with your input!')
                move_again()
                break
    else:
        score()
        return
def invalid_input(x,y,s):
    if x in lines and y in column and len(s)==3:
        return True
    else:
        return False
def finish_game():
    for i in range(8):
        for j in range(8):
            num=board[i][j]
            if num=='0  ':
                if board[i+1][j]=='1  ' and board[i+2][j]=='1  ':
                    return True
                elif board[i-1][j]=='1  ' and board[i-2][j]=='1  ':
                    return True
                elif board[i][j+1]=='1  ' and board[i][j+2]=='1  ':
                    return True
                elif board[i][j-1]=='1  ' and board[i][j-2]=='1  ':
                    return True
    return False           
printboard()
def move(x,y,z,k):
        if z in direct:
            pass
        else:
            print('Direction is not L or R or U or D!')
        if board[voc1[x]][voc2[y]]=='0  ':
            print('Given peg position does not have a peg!')
        elif  board[voc1[x]][voc2[y]]!='1  ' and board[voc1[x]][voc2[y]]!='0  ':
            print('Given peg position is out of board!')
        elif board[voc1[x]][voc2[y]]=='1  ':
            if z=='U' or z=='u':
                if board[voc1[x]-1][voc2[y]]=='0  ':
                    print('No peg next position to jump over!')
                elif board[voc1[x]-2][voc2[y]]=='1  ':
                    print('Landing position is occupied!')
                elif board[voc1[x]-2][voc2[y]] in pegs and board[voc1[x]-1][voc2[y]] in pegs:
                    board[voc1[x]][voc2[y]]='0  '
                    board[voc1[x]-1][voc2[y]]='0  '
                    board[voc1[x]-2][voc2[y]]='1  '
                    printboard()
                else:
                    print('Moving peg will fall out of bounds!')
            elif z=='D' or z=='d':
                if board[voc1[x]+1][voc2[y]]=='0  ':
                    print('No peg next position to jump over!')
                elif board[voc1[x]+2][voc2[y]]=='1  ':
                    print('Landing position is occupied!')
                elif board[voc1[x]+2][voc2[y]] in pegs and board[voc1[x]+1][voc2[y]] in pegs:
                    board[voc1[x]][voc2[y]]='0  '
                    board[voc1[x]+1][voc2[y]]='0  '
                    board[voc1[x]+2][voc2[y]]='1  '
                    printboard()
                else:
                    print('Moving peg will fall out of bounds!')
            elif z=='L' or z=='l':
               if board[voc1[x]][voc2[y]-1]=='0  ':
                    print('No peg next position to jump over!')
               elif board[voc1[x]][voc2[y]-2]=='1  ':
                    print('Landing position is occupied!')
               elif board[voc1[x]][voc2[y]-2] in pegs and board[voc1[x]][voc2[y]-1] in pegs:
                    board[voc1[x]][voc2[y]]='0  '
                    board[voc1[x]][voc2[y]-1]='0  '
                    board[voc1[x]][voc2[y]-2]='1  '
                    printboard()
               else:
                    print('Moving peg will fall out of bounds!')
            elif z=='R' or z=='r':
                if board[voc1[x]][voc2[y]+1]=='0  ':
                    print('No peg next position to jump over!')
                elif board[voc1[x]][voc2[y]+2]=='1  ':
                    print('Landing position is occupied!')
                elif board[voc1[x]][voc2[y]+2] in pegs and board[voc1[x]][voc2[y]+2] in pegs:
                    board[voc1[x]][voc2[y]]='0  '
                    board[voc1[x]][voc2[y]+1]='0  '
                    board[voc1[x]][voc2[y]+2]='1  '
                    printboard()
                else:
                    print('Moving peg will fall out of bounds!')                   
move_again()            



          
         
        
    
