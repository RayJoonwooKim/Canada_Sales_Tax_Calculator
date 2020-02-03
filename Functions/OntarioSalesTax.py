def hstOntario(amount):
    return round(amount * 0.13, 2);

def totalOntario(amount):
    return round(amount + hstOntario(amount),2);

def calculateOntario():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nHST: " + str(hstOntario(amount)) + "\nAmount with sales tax: " + str(totalOntario(amount)));
            break;