#Program to create a Kanban Board
x=input('To view your Kanban Board press \'R\' or to change the contents press \'W\': ')
board={}
if x.lower()=='r':
    f=open("board.txt","r")
    f1=f.readlines()
    for i in f1:
        i=i.strip('\n')
        l=i.split(',')
        if l[1] in board:
            board[l[1]].append(l[0])
        else:
            board[l[1]]=[l[0]]
elif x.lower()=='w':
    f=open("board.txt","a")
    Task=input('Enter name of task: ')
    Category=input('Enter item category: ')
    f.write(Task+','+Category+'\n')
    f.close()
else:
  print('Incorrect Input')
for i in board:
    print(i,':', end=' ')
    for j in board[i]:
        print(j,end=', ')
    print()
f.close()
