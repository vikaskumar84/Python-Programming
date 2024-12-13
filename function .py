
def account_no():
    account_num=int(input("enter your account number "))
    if account_num==8445703620:
        print("account_holder : vikas yadav\n address: tuamai akrabad\n mob_no=8445703620 \n pincode=202121")
    elif account_num==7505843958:
        print("account_holder : ankit yadav\n address: tuamai akrabad\n mob_no=7505843958 \n pincode=202121")
    else:
        print("account holder not found")
def ask():
    balance=1000
    while balance>0:
        print("what you want ?")
        print(" 1: debited\n 2: crebideted\n 3: check_balance")
        x=int(input("select your choice "))
        if x == 1:
            while balance > 0:
                n = int(input("how many rupees ? "))
                if n > balance :
                    print("insufficient balance")
                else:
                    balance = balance - n
                    print("take your amount", n)
                    print("due account balance ", balance)
                    break
        elif x == 2:
            a = int(input("how many rupees ? "))
            balance = balance + a
            print("successfully deposited", a)
            print("total account balance", balance)
            break
        elif x == 3:
            print("your account balance is ", balance)
            break
        else:
            print("wrong choice")
        print("**********************************************************\n")
account_no()
ask()








