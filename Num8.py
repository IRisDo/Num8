from os import remove,rename,system
from msvcrt import getch
from random import randint
from time import sleep

DS = [1,2,3,8,' ',4,7,6,5]
Lw = [1,2,3,8,' ',4,7,6,5]

def getUserScore(userName):
    try:
        with open('UserScore.txt','r') as f:
            for line in f:
                List = line.split(',')
                if List[0] == userName:
                    return List[1]
            else:
                return '-1'
    except IOError:
        print('\nFile userScore.txt not found. A new file will be created.')
        sleep(2)
        with open('UserScore.txt','w') as f:
            return '-1'

def updateUserScore(newUser,userName,Score):
    if newUser:
        with open('UserScore.txt','w') as f:
            f.write('\n' + userName + ',' + str(Score))
        return Score
    else:
        with open('UserScore.txt','r') as f1:
            with open('UserScore.tmp','w') as f2:
                for line in f1:
                    List = line.split(',')
                    if List[0] == userName:
                        List[1] = int(List[1]) + Score
                        line = List[0] + ',' + str(List[1]) + '\n'
                    f2.write(line)
        remove('UserScore.txt')
        rename('UserScore.tmp','UserScore.txt')
        return int(List[1])

def BestScore():
    try:
        with open('UserScore.txt','r') as f:
            L =[]
            for line in f:
                List = line.split(',')
                L.append(List[-1][0])
            L.sort()
            return L[-1]
    except FileNotFoundError:
        return ''

def BestPlayer(best):
    try:
        with open('UserScore.txt','r') as f:
            for line in f:
                List = line.split(',')
                if List[-1][0] == best:
                    return List[0]
        return 'No Member'
    except FileNotFoundError:
        return ''

def BestMember():
    if BestScore() == '' and BestPlayer(BestScore()) == '':
        return 'You are first player'
    else:
        return('Best Score = ' + BestScore() + ' by ' + BestPlayer(BestScore()))


def SearchEmtry():
    for m in range(0,9):
        if DS[m] == ' ':
            return m

def move(a,b,c,d,s,i):
    if DS[i] == ' ' and i!=a and i!= b and i!=c:
        DS[i],DS[i+d] = DS[i+d],DS[i]
    else:
        print("We can\'t move %s! \n" %(s))
    return show()

def move0(a,b,c,d,s,i):
    if DS[i] == ' ' and i!=a and i!= b and i!=c:
        DS[i],DS[i+d] = DS[i+d],DS[i]
        return None
    else:
        return None

def show():
    k=-1
    for i in range(0,3):
        print('+---+---+---+')
        h='| '
        for j in range(0,3):
            k+=1
            h=h+str(DS[k]) +' | '
        print(h)
    print('+---+---+---+')
    return None

def Disorder():
    for i in range(0,5001):
        r = randint(1,5)
        if r == 1:
            move0(0,1,2,-3,'up',SearchEmtry())
            move0(2,5,8,1,'right',SearchEmtry())
            move0(0,3,6,-1,'left',SearchEmtry())
        elif r == 2:
            move0(6,7,8,3,'down',SearchEmtry())
            move0(2,5,8,1,'right',SearchEmtry())
            move0(0,1,2,-3,'up',SearchEmtry())
        elif r == 3:
            move0(2,5,8,1,'right',SearchEmtry())
            move0(6,7,8,3,'down',SearchEmtry())
            move0(0,3,6,-1,'left',SearchEmtry())
        else:
            move0(6,7,8,3,'down',SearchEmtry())
            move0(0,3,6,-1,'left',SearchEmtry())
            move0(0,1,2,-3,'up',SearchEmtry())
    if DS == Lw:
        Disorder()
    else:
        return DS

def start():
    print('''\nRule: Using sign-arrow to move |empty|.  If You have:\n''')
    show()
    print('\nYOU WILL WIN !!!')
    sleep(3)
    system('cls')
    print('\nNow, Start ! \n')
    system('cls')
    Disorder()
    print(show())
    while DS != Lw:
        input_move = ord(getch())
        if input_move == 224:
            input_move = ord(getch())
            if input_move == 72:
                system('cls')
                move(0,1,2,-3,'up',SearchEmtry())
            elif input_move == 77:
                system('cls')
                move(2,5,8,1,'right',SearchEmtry())
            elif input_move == 75:
                system('cls')
                move(0,3,6,-1,'left',SearchEmtry())
            elif input_move == 80:
                system('cls')
                move(6,7,8,3,'down',SearchEmtry())
            else:
                system('cls')
                show()
                print('\nUsing sign-arrow to move |empty|, please! \n')
        else:
            system('cls')
            show()
            print('\nUsing sign-arrow to move |empty|, please! \n')
    else:
        print('\n CONGRATULATE ! YOU WON ..... <3 \n')
        system('cls')
        return 1

if __name__ == '__main__':
    print('Hello! This is game create by IRisDo =)) \n')
    sleep(2)
    try:
        print(BestMember())
        sleep(1)
        userName = input('''\nPlease enter your user name or create a new-name If this is the first time
you are running the program: ''')
        userScore = getUserScore(userName)
        if userScore == '-1':
            newUser = True
        else:
            newUser = False
        end_or_continue = 'Y'
        Score = 0
        while end_or_continue == 'Y' or end_or_continue == 'y':
            Score += start()
            Scores = updateUserScore(newUser,userName,Score)
            print ('Current Score = ', Scores, '\n')
            end_or_continue = input('Enter Y if you want continue and other keyword if you want end game:')
    except Exception as e:
        print ("An unexpected error occurred. Program will be exited.")
        getch()
