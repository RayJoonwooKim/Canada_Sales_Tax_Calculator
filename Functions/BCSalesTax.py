def gstBC(amount):
    return round(amount * 0.05, 2);

def pstBC(amount):
    return round(amount * 0.07, 2);

def totalBC(amount):
    return round(amount + gstBC(amount) + pstBC(amount),2);

def calculateBC():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstBC(amount)) + "\nPST: " + str(pstBC(amount)) + "\nAmount with sales tax: " + str(totalBC(amount)));
            break;