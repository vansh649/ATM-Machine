account_pin = "2410"
account_number = "0206241008"
bank_balance = 20000
bank_name = "UBI"

ATTEMPTS = 3

while ATTEMPTS>0:
    enter_pin =input("enter your pin: ")

    if enter_pin == account_pin:
        print("WELCOME USER")

        break

    else:
        ATTEMPTS -= 1
        print("WRONG PIN")

        if ATTEMPTS == 0:
            print("YOUR CARD HAS BEEN BLOCKED")


while True:

    choices = int(input("enter a number between 1 to 4: "))

    if choices == 1:
        print(account_number)

    elif choices == 2:
        bank_balance += int(input("enter bank deposite amount: "))
        print ("Your new bank balance is: " ,bank_balance)

    elif choices == 3:
        bank_balance -= int(input("enter back withdrawl amount: "))
        if bank_balance <= bank_balance:
            print("insufficient balance")
            break
        else:
             print ("Your remaining bank balance is: ", bank_balance)

    elif choices == 4:
        print(bank_balance)

    else:
        print("YOU ENTERED A WRONG PIN")
        break






