import random 

while True: 
   print("|ROCK PAPER SCISSORS|\n1.Rock\n2.Paper\n3.Scissor\n4.Quit")
    
    user_input = input("Enter your choice: ").lower().strip().title()

    if user_input not in ["1","2","3","4"]:
        print(f"{user_input} is an invalid choice.")
        continue
    elif user_input == "1":
        user_input = "Rock"
    elif user_input == "2":
            user_input = "Paper"
    elif user_input == "3":
            user_input = "Scissor"

    system_input = random.choice(["Rock", "Paper" , "Scissor"])

    if user_input == "4":
         print("Thanks for playing!")
         break

    elif user_input == system_input:
        print("It's a TIE!")
        print(f"You chose {user_input}, Oppenent chose {system_input}\n")
        continue

    elif (user_input == "Rock" and system_input == "Scissor") or \
        (user_input == "Scissor" and system_input == "Paper") or \
        (user_input == "Paper" and system_input == "Rock"):
        print ("You WIN!")
        print(f"You chose {user_input}, Oppenent chose {system_input}\n")
        continue
    
    else:
        print("You LOSE!")
        print(f"You chose {user_input}, Oppenent chose {system_input}\n")
        continue