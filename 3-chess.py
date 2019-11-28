chess_status = list((0,) * 9)
print(type(chess_status))
      
for count in range(0,3):
    for count1 in range(0,3):
        print (chess_status[count*3+count1],end='')
    print ()

win = 0
role = 0
x=0
y=0


while win == 0:
    v=0
    role +=1
    if role == 3:
        role = 1
    while v==0:

        x=int(input(str(role)+'输入行(1-3):'))
        y=int(input(str(role)+'输入列(1-3):'))
        print(x,' ',y)
        if chess_status[(x-1)*3+y-1]==0:
            v=1
        else:
            print('该位置已有。重新选择')
        chess_status[(x-1)*3+y-1]=int(role)
        for count in range(0,3):
            for count1 in range(0,3):
                print (chess_status[count*3+count1],end='')
            print ()
    
#判断是否有人胜出
    c=chess_status
    if c[0]==c[1]==c[2]==1 or c[3]==c[4]==c[5]==1 or c[6]==c[7]==c[8]==1 or\
       c[0]==c[3]==c[6]==1 or c[1]==c[4]==c[7]==1 or c[2]==c[5]==c[8]==1 or\
       c[0]==c[4]==c[8]==1 or c[2]==c[4]==c[6]==1:
        win = 1
    if c[0]==c[1]==c[2]==2 or c[3]==c[4]==c[5]==2 or c[6]==c[7]==c[8]==2 or\
       c[0]==c[3]==c[6]==2 or c[1]==c[4]==c[7]==2 or c[2]==c[5]==c[8]==2 or\
       c[0]==c[4]==c[8]==2 or c[2]==c[4]==c[6]==2:
        win = 2


print ('the winner is: player ',win)
    
