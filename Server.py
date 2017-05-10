#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('', 46669))
serverSocket.listen(1)

#data structures to help with processing winning, losing, current game, and current players
class Player:
	def __init__(self, status, username, address, socket):
		self.status = status
		self.username = username
		self.address = address
		self.socket = socket

class Game:
	def __init__(self, player1, player2, gameStatus):
		self.player1 = player1
		self.player2 = player2
		self.gameStatus = gameStatus

numberOfPlayers = 0
turn = 0
playerList = []
gameList = []
over = 0

#some functions to help with the game.
#this function turns a list into a string, meant for sending strings through protocols
def turnIntoString(list):
	x = ""
	for i in range(len(list)):
		x += str(list[i])
	return x

#this function determines if a game is over by checking each combination.
#a 0 means no player has placed there yet; 1 means an X, 2 means an O.
#determines a tie if there are no 0's in the string.
def calculateAlgorithm(status):
	#rows
	if(status[0] == status[1] and status[1]==status[2]):
		if(status[0] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[0] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1
	if(status[3] == status[4] and status[4]==status[5]):
		if(status[3] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[3] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1
	if(status[6] == status[7] and status[7]==status[8]):
		if(status[6] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[6] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1

	#columns
	if(status[0] == status[3] and status[3]==status[6]):
		if(status[0] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[0] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1

	if(status[1] == status[4] and status[4]==status[7]):
		if(status[1] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[1] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1
	if(status[2] == status[5] and status[5]==status[8]):
		if(status[2] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[2] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1

	if(status[0] == status[4] and status[4]==status[8]):
		if(status[0] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[0] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1

	if(status[2] == status[4] and status[4]==status[6]):
		if(status[2] == '1'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			over = 1
		elif(status[2] == '2'):
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			over = 1
	if "0" not in status:
		#send tie
		playerList[0].socket.send(("900 TIE \r\n").encode())
		playerList[1].socket.send(("900 TIE \r\n").encode())
		over = 1

while True:
	print("Waiting...")
	#establish a connection
	connectionSocket, addr = serverSocket.accept()
	try:
		#get the message
		message = connectionSocket.recv(1024).decode()
		command = message.split()[0]

		if command == "LOGIN":
			p = Player("P", message.split()[1], addr, connectionSocket)
			playerList.append(p)
			numberOfPlayers = numberOfPlayers + 1
			if(numberOfPlayers == 1):
				#first player
				connectionSocket.send(("200 OK \r\n").encode())
				print ("Waiting for 1 more person")
			else:
				#second player came, start the game and send protocols, make  agame object.
				playerList[0].socket.send(("300 FOUND " + playerList[1].username + " \r\n").encode())
				playerList[1].socket.send(("300 FOUND " + playerList[0].username + " \r\n").encode())
				g = Game(playerList[0], playerList[1], [0,0,0,0,0,0,0,0,0])
				gameList.append(g)
				break
	except IOError:
		connectionSocket.close()

while True:
	#if its game over
	if over == 1:
		break
	#this turn stuff determines who goes on what turn, and if it's not your turn, you dont do anything but read.
	if turn==0:
		message = playerList[0].socket.recv(1024).decode()
		command = message.split()[0]
	else:
		message = playerList[1].socket.recv(1024).decode()
		command = message.split()[0]
	#exit protocol: end the game with the player who didn't call EXIT being the winner
	if command == "EXIT":
		if turn==0:
			playerList[0].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[1].username + " \r\n").encode())
		else:
			playerList[0].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
			playerList[1].socket.send(("800 GAME_OVER " + playerList[0].username + " \r\n").encode())
		break
	#error protocol: there was an error with input, try again. send back a 400 ERROR
	elif command == "ERROR":
		#bad
		playerList[0].socket.send(("400 ERROR \r\n").encode())
		playerList[1].socket.send(("400 ERROR \r\n").encode())
	#the crux of the program: determines the board status to see if its GG. send appropriate protocols.
	elif command == "PLACE":
		if turn == 0:
			#update gamestate with 1.
			gameList[0].gameStatus[int(message.split()[1])] = 1
			turn = 1
		else:
			gameList[0].gameStatus[int(message.split()[1])] = 2
			turn = 0
		#calculate algorithms
		formatString = turnIntoString(gameList[0].gameStatus)
		calculateAlgorithm(formatString)
		playerList[0].socket.send(("150 STATE " + formatString + " \r\n").encode())
		playerList[1].socket.send(("150 STATE " + formatString + " \r\n").encode())

#close all sockets.
playerList[0].socket.close()
playerList[1].socket.close()
serverSocket.close() 
