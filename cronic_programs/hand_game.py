# Stone , Paper , Scissor Game
# User v/s computer
# Combination
# stone + paper
import random

use_items = {
    "S":"Stone","P":"Paper","C":"Scissor",
    "s":"Stone","p":"Paper","c":"Scissor"
}
lst = ["s","p","c"]
star = "*"*10
life = 5

def play_game(m_draw,u_points,c_points):
    i = 1
    while(i<=life):
        user = input("Enter Your Choice: ")
        comp = random.choice(lst)
        print("You Choose: ",use_items[user])
        print("Computer Choose: ",use_items[comp])
        if(user == comp):
            m_draw += 1
        elif(user == "s" and comp == "p"):
            c_points += 1
        elif(user == "s" and comp == "c"):
            u_points += 1
        elif(user == "p" and comp == "s"):
            u_points += 1
        elif(user == "p" and comp == "c"):
            c_points += 1
        elif(user == "c" and comp == "s"):
            c_points += 1
        elif(user == "c" and comp == "p"):
            u_points += 1
        i += 1
    # print(m_draw,u_points,c_points)
    print("Total Match Draw: ",m_draw)
    print("You Scored: ",u_points)
    print("Computer Scored: ",c_points)
    if(u_points == c_points):
        print(f"\n{star}Match Draw{star}")
    elif(u_points > c_points):
        print(f"\n{star}You Win{star}")
    else:
        print(f"\n{star}Computer Win{star}")


print("Welcome To Hand-Game")
print("S-> Stone, P-> Paper, C-> Scissor")
print("Life Count: ",life)
print("*"*30)
while (True):
    play_game(0,0,0)
    if((input("Do you want to play more?(Y/N)\n")).capitalize()=='Y'):
        continue
    else:
        print("Thank You for playing")
        break