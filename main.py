import random 

while True: 
    choice = print("1.Rock\n2.Paper\n3.Scissor\n4.Quit")
    
    user_input = input("Enter your choice: ").lower().strip()
    if user_input not in ["1","2","3","4"]:
        print(f"{user_input} is an invalid choice.")
        continue

    system_input = random.choice(["rock", "paper" , "scissor"])

    print(f"You chose {user_input}, Oppenent chose {system_input}")

    if user_input == system_input:
        print("It's a TIE!")
        break

    elif (user_input == "rock" and system_input == "scissor") or \
        (user_input == "scissor" and system_input == "paper") or \
        (user_input == "paper" and system_input == "rock"):
        print ("You WIN!")
        break

    else:
        print("You LOSE!")
        break