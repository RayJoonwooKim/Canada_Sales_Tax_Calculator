def hstNL(amount):
    return round(amount * 0.15, 2);

def totalNL(amount):
    return round(amount + hstNL(amount),2);

def calculateNL():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nHST: " + str(hstNL(amount)) + "\nAmount with sales tax: " + str(totalNL(amount)));
            break;