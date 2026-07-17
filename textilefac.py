print("Welcom to my Textile factory")
shirts = int(input("Enter your produced shirts"))
sh = 0
Bonus =0
if(shirts>1000):
    print("Congrats! you r eligible for Bonus")
    Bonus = shirts*20
    
    print("Your Bonus is:", Bonus)
    print("You r Qualified.. Hurrah!")
else:
    print("You are not qualified for bonus.. Good luck for next time")
    
