def gstNT(amount):
    return round(amount * 0.05, 2);

def totalNT(amount):
    return round(amount + gstNT(amount),2);

def calculateNT():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstNT(amount)) + "\nAmount with sales tax: " + str(totalNT(amount)));
            break;