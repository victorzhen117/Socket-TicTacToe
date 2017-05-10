#importing stuff
import socket
HOST = '172.25.83.205'
PORT = 46669
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)
#to determine who's turn
turn = 0

#the start of the program: enter a username.
print("Enter your username:   ")
while True:
    #places the person in the login queue.
    #if there is only one person waiting, then he/she waits until one more
    #if there are two people waiting, they go into a game and it begins.s
    name = input()
    if name == "help":
        print("This game is the same as Tic Tac Toe, except the goal of the game "
                                  "is to not get 3 in a row.")
    else:
        sock.send(("LOGIN " + name + " \r\n").encode()) 
    data = sock.recv(1024)
    txt = data.decode()
        # print '--%s--' % txt
    #if txt.startswith('300'):
    #    txt.strip('300')
    #    print("Playing with " + txt)
    #    turn = 1
    #    break;
    #if txt.startswith('200'):
    #    print("Waiting for one more!")
    #    data = sock.recv(1024)
    #    print("Playing with"+ data.decode())
    #    break;
    values = txt.split()
    if values[0] == "300":
        print("Playing with " + values[2])
        turn = 1
        break
    if values[0] == "200":
        print("Waiting for one more!")
        print("Playing with: " + sock.recv(1024).decode().split()[2])
        break

#the game started!
print("Game Start:")
while True:
    #if the turn is 0, then that means it is the first person to log in's turn.
    if turn == 0:
        print("It's your turn!")
        x = input()
        #depending on input, does certain things like EXIT, PLACE, or ERROR
        if x.upper() == "EXIT":
            sock.send(("EXIT \r\n").encode()) 
            break
        elif int(x)>=0 and int(x)<=8:
            turn = 1
            sock.send(("PLACE " + x + " \r\n").encode()) 
            data = sock.recv(1024)
            txt = data.decode()
            values = txt.split()
            if values[0] == "150":
                txt = values[2]
                #prints the current board.
                print("Current Board: ")
                print("")
                for i in range(1,10):
                    if txt[i-1]=="0":
                        print(' - ', end = '')
                    elif txt[i-1]=="1":
                        print(' X ', end = '')
                    elif txt[i-1]=="2":
                        print(' O ', end = '')

                    if (i % 3) == 0:
                        print('')
            if values[0] == "800":
                print (values[2] + " won!");
                break;
            if values[0] == "900":
                print("Tie! No one wins")
                break;
        else:
            sock.send(("ERROR \r\n").encode()) 
            sock.recv(1024)
            print("There was an error. Please enter a valid response.")

    else:
        #other persons turn; does nothing but read.
        print("It's not your turn :(")
        data = sock.recv(1024)
        txt = data.decode()
        values = txt.split()
        if values[0] == "150":
            #prints the board.
            turn = 0
            txt = values[2]
            print("Current Board: ")
            for i in range(1,10):
                if txt[i-1]=="0":
                    print(' - ', end = '')
                elif txt[i-1]=="1":
                     print(' X ', end = '')
                elif txt[i-1]=="2":
                    print(' O ', end = '')

                if (i % 3) == 0:
                    print('')
        #these protocols are for winning/losing/ties/errors.
        if values[0] == "800":
            print (values[2] + " won!");
            break;
        if values[0] == "900":
            print("Tie! No one wins")
            break;
        if values[0] == "400":
            print("There was an error in your opponents move. Please wait. ")
