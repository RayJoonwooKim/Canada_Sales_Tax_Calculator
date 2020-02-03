def gstNunavut(amount):
    return round(amount * 0.05, 2);

def totalNunavut(amount):
    return round(amount + gstNunavut(amount),2);

def calculateNunavut():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstNunavut(amount)) + "\nAmount with sales tax: " + str(totalNunavut(amount)));
            break;