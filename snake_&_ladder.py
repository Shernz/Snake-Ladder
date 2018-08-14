n=int(input())#No of players
players={}
for i in range(n):
    players[input()]=0#player name and score
snakes={42:16,78:45,98:65,75:6,67:26,70:30}
ladders={20:39,13:47,53:91,44:65,58:83,43:90}
die=0
finish = False

while not finish:
    for player in players:
        print("{0} turn ".format(player))
        die=int(input())
        while die>7:
            print("Incorrect die roll")
            die = int(input())
        players[player]+=die
        if players[player]in snakes:
            print("Ouch! Snake alert {0} to {1}".format(players[player],snakes[players[player]]))
            players[player]=snakes[players[player]]
        elif players[player]in ladders:
            print("Right up the ladder {0} to {1}".format(players[player],ladders[players[player]]))
            players[player]=ladders[players[player]]
        elif (players[player]>=100):
            print(player," wins")
            finish = True
            break
        print("{0} is at {1}".format(player,players[player]))



        
    
