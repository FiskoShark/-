from Student import Student
name = input("Enter ur name: ")
nick = Student("name")
print("-----------Starting game-----------")
print("-----------------------------------")
print("--------for tips write help--------")
while nick.isAlive:
    answer = input("write command: ")
    if answer.lower().startswith("hel"):
        print("""Command for game:
            1. Skip
            2. Study
            3. Eat
            4. Sleep
            5. Walk
            6. Travel
            7. Hobby""")
    elif answer.lower().startswith("skip"):
        nick.to_skip()
    elif answer.lower().startswith("stud"):
        nick.to_study()
    elif answer.lower().startswith("eat"):
        nick.to_eat()
    elif answer.lower().startswith("sleep"):
        nick.to_sleep()
    elif answer.lower().startswith("work"):
        nick.to_work()
    elif answer.lower().startswith("walk"):
        nick.to_walk()
    elif answer.lower().startswith("travel"):
        nick.to_travel()
    elif answer.lower().startswith("hobby"):
        nick.to_hobby()

    else:
        print("Command not found. Enter 'help' for tips")

    nick.info()
    nick.check_life()
