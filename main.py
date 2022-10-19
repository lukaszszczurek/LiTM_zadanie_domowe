import json

import requests

chessTypetext = ''
raitingprediction = -1

name = input("What's your name?")
haveLichessAccount = input("Have you Lichess Account y-yes, n-no")
if haveLichessAccount == 'y':
    usernameLichess = input("What is your username on Lichess?")


elif haveLichessAccount == 'n':
    inputRaiting = input("What should be your rating in your opinion?(only numbers between 0-3000")
    raitingprediction = float(inputRaiting)
else:
    print("incorrect input")

favouriteTypeofChess = input("What is your favourite type of chess?"
                             "if blitz type:B if bullet type:U and finally if rapid type:R")
if favouriteTypeofChess == 'B':
    chessTypetext = "blitz"
elif favouriteTypeofChess == 'U':
    chessTypetext = "bullet"
elif favouriteTypeofChess == 'R':
    chessTypetext = "rapid"

response = requests.get("https://lichess.org/api/player")

data = response.json()
bestplayerdata = data[chessTypetext][0]['perfs'][chessTypetext]['rating']
bestraiting = float(bestplayerdata)

Points = 1700
responsePlayer = requests.get(f"https://lichess.org/api/user/{usernameLichess}")
userdata = responsePlayer.json()
playerActualraiting = userdata['perfs'][chessTypetext]['rating']
playerraitingfloat = float(playerActualraiting)
if haveLichessAccount == 'y' and not playerraitingfloat + Points < bestraiting:

    print(f"Congratulation {name} your chess skills are incredible your lichess "
          f"rating plus 1700 ({playerraitingfloat} + {Points} > {bestraiting}) points is more than the best chess player in category")
elif haveLichessAccount == 'y':
    print("Ranking is to weak")
elif haveLichessAccount == 'n':
    if raitingprediction + Points > bestraiting:
        print(f"Congratulation {name} your chess skills are incredible your lichess "
              "rating plus 1700 points is more than the best chess player in category")
    else:
        print("Your score is to weak")
