user_1=input("user_1 favourite game :")
user_11=int(input("rating for your favourite game out of 5:"))
user_2=input("user_2 favourite game :")
user_22=int(input("rating for your favourite game out of 5:"))
if user_1==user_2 and user_11==user_22:
    print("the user_1 and user_2 chosen the same game and ratings")
if user_1!=user_2 and user_11!=user_22:
    print("the user_1 and user_2 not chosen the same game and ratings")
if user_1!=user_2 and user_11==user_22:
    print("user_1 and user_2 chosen different game but same ratings")
else:
    print("user_1 and user_2 chosen same game but different ratings")