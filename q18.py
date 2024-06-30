print("username=admin\npassword=1234")
username="admin"
password=1234
name=input("enter username - ")
pas=int(input("enter password - "))
if name==username:
    if pas==password:
        print("you have been logged in successfully")
else:
    print("the username and password is incorrect")