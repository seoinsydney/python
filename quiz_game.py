print("Welcome to my computer quiz!")

playing = input("Do you want to play quiz game? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play!")

score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 # socore = score + 1
else:
    print('Incorrect answer, try again!')


answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect answer, try again!')


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/2) * 100) + " %. ")


