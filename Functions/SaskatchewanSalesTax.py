def gstSaskatchewan(amount):
    return round(amount * 0.05, 2);

def pstSaskatchewan(amount):
    return round(amount * 0.06, 2);

def totalSaskatchewan(amount):
    return round(amount + gstSaskatchewan(amount) + pstSaskatchewan(amount),2);

def calculateSaskatchewan():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstSaskatchewan(amount)) + "\nPST: " + str(pstSaskatchewan(amount)) + "\nAmount with sales tax: " + str(totalSaskatchewan(amount)));
            break;