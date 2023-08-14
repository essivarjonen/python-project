COLOR_RED = '\x1b[31m'
COLOR_GREEN = '\x1b[32m'
COLOR_RESET = '\x1b[0m'

print("Welcome to Quiz Game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit("ok, byee!")

print("Let's play the Quiz Game!")

userName = input("First enter your username ")
print("Hello " + userName + "! Let's play then!")
score = 0

answer = input("What is Python? ")
if answer.lower() == "programming language":
    print(COLOR_GREEN + "Correct!" + COLOR_RESET)
    score += 1
else:
    print(COLOR_RED + "Incorrect!" + COLOR_RESET)

answer = input("How do you check the data type of a variable? ")
if answer.lower() == "using type()":
    print(COLOR_GREEN + "Correct!" + COLOR_RESET)
    score += 1
else:
    print(COLOR_RED + "Incorrect!" + COLOR_RESET)

answer = input("How do you define a function in Python? ")
if answer.lower() == "using def":
    print(COLOR_GREEN + "Correct!" + COLOR_RESET)
    score += 1
else:
    print(COLOR_RED + "Incorrect!" + COLOR_RESET)

answer = input("How can you bring other modules in Python file? ")
if answer.lower() == "using import":
    print(COLOR_GREEN + "Correct!" + COLOR_RESET)
    score += 1
else:
    print(COLOR_RED + "Incorrect!" + COLOR_RESET)

if score == 1:
    print("You got only " + str(score) +
          "/4 questions correct. Better luck next time!")
else:
    print("Fantastic! you got " + str(score) + "/4 questiongs correct!")
