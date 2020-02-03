def gstQuebec(amount):
    return round(amount * 0.05, 2);

def qstQuebec(amount):
    return round(amount * 0.09975,2);

def totalQuebec(amount):
    return round(amount + gstQuebec(amount) + qstQuebec(amount),2);

def calculateQuebec():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstQuebec(amount)) + "\nQST: " + str(qstQuebec(amount)) + "\nAmount with sales tax: " + str(totalQuebec(amount)));
            break;