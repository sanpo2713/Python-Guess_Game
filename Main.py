import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    a = int(input("Enter a Number : "))
    if(a > n):
        print("Lower the Number please!")
        guesses +=1
    elif(a < n):
        print("Higher the Number please!")
        guesses +=1

print(f"You have Gueassed correct Number {n} in {guesses} attempts!!!")