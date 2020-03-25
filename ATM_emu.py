from User_verification import user_input
from user_accnt import atm

uv = 0
print("WELCOME TO CREDIT REPUBLICAN ATM")
cn = int(input("ENTER YOUR CARD NO: "))
pin = int(input("ENTER YOUR PIN: "))
uv = user_input(cn, pin)
if uv == 1:
    atm()
else:
    print("INVALID CARD DETAILS")
