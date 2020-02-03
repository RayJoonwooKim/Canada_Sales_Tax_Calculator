def hstNovaScotia(amount):
    return round(amount * 0.15, 2);

def totalNovaScotia(amount):
    return round(amount + hstNovaScotia(amount),2);

def calculateNovaScotia():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nHST: " + str(hstNovaScotia(amount)) + "\nAmount with sales tax: " + str(totalNovaScotia(amount)));
            break;