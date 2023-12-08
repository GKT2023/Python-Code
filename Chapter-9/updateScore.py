def game():
    return 90

score = game()

with open('HiScore.txt','r') as f:
    currentScore = f.read()

if currentScore == '':
    with open ('HiScore.txt','w') as f:
        f.write(str(score))    

elif int(currentScore) < score:
    with open ('HiScore.txt','w') as f:
        f.write(str(score))