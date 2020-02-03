def hstPEI(amount):
    return round(amount * 0.15, 2);

def totalPEI(amount):
    return round(amount + hstPEI(amount),2);

def calculatePEI():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nHST: " + str(hstPEI(amount)) + "\nAmount with sales tax: " + str(totalPEI(amount)));
            break;