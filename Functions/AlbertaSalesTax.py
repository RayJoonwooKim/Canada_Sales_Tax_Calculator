def gstAlberta(amount):
    return round(amount * 0.05, 2);

def totalAlberta(amount):
    return round(amount + gstAlberta(amount),2);

def calculateAlberta():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstAlberta(amount)) + "\nAmount with sales tax: " + str(totalAlberta(amount)));
            break;