print('Welcome To The Quiz')

playing = input('Do You Want To Play ')

if playing != "yes":
    quit()

print("Let's Start Then!!! ")

score  = 0

answer = input('Who is the father of Software Engineering? ')
if answer.lower() == 'watts s humphrey':
    print('Correct!!! ')
    score += 1
else:
        print('Incorrect!! ')

answer = input('CASE stands for ')
if answer.lower() == 'computer aided software engineering':
    print('Correct!!! ')
    score += 1
else:
        print('Incorrect!! ')

answer = input('What does SDLC stands for? ')
if answer.lower() == 'software development life cycle':
    print('Correct!!! ')
    score += 1
else:
        print('Incorrect!! ')

answer = input('Which one is system software? ')
if answer.lower() == 'computer program':
    print('Correct!!! ')
    score += 1
else:
        print('Incorrect!! ')

answer = input('Software Debugging is known as  ')
if answer.lower() == 'finding and correcting errors in the program code':
    print('Correct!!! ')
    score += 1
else:
        print('Incorrect!! ')

print("Your Got " + str(score) + " Questions Correct!!!")
print("Your Got " + str((score / 5) * 100) + "%.")