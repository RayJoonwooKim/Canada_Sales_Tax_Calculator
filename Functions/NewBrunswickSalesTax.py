def hstNB(amount):
    return round(amount * 0.15, 2);

def totalNB(amount):
    return round(amount + hstNB(amount),2);

def calculateNB():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nHST: " + str(hstNB(amount)) + "\nAmount with sales tax: " + str(totalNB(amount)));
            break;