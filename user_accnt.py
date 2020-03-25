import pickle


def atm():
    file = "Account_details.pkl"
    file_obj = open(file, "wb")
    savings = int(50000)
    pickle.dump(savings, file_obj)
    user_choice = input("D: DEPOSIT "
                        "W: WITHDRAWAL "
                        "A: ACCOUNT DETAILS ")
    file_obj = open(file, "rb")
    pickle.load(file_obj)
    if user_choice == 'D':
        file_obj = open(file, "wb")
        d_amt = int(input("ENTER AMOUNT TO BE DEPOSITED "))
        savings = d_amt + savings
        print("TOTAL AMOUNT : ", savings)
        pickle.dump(savings, file_obj)
    elif user_choice == 'W':
        file_obj = open(file, "wb")
        w_amt = int(input("ENTER AMOUNT TO BE WITHDRAWN "))
        savings = savings - w_amt
        print("TOTAL AMOUNT :", savings)
        pickle.dump(savings, file_obj)
    elif user_choice == 'A':
        file_obj = open(file, 'rb')
        pickle.load(file_obj)
        print("TOTAL AMOUNT :", savings)
    else:
        print("INVALID INPUT")
    file_obj.close()
