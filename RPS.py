import random
list_items=["Rock","Paper","Scissor"]

user_choice = input("Enter your choice(Rock,Paper,Scissor)= ")
comp_choice = random.choice(list_items)

print(f"User_choice = {user_choice}\nComp_choice = {comp_choice}")

if user_choice == comp_choice:
    print("Match TIE")

elif user_choice == "Rock":
    if comp_choice == "Scissor":
        print("You WIN")
    else :
        print("Comp WIN")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("You WIN")
    else :
        print("Comp WIN")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Comp WIN")
    else :    
        print("You WIN")


         