def gstYukon(amount):
    return round(amount * 0.05, 2);

def totalYukon(amount):
    return round(amount + gstYukon(amount),2);

def calculateYukon():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstYukon(amount)) + "\nAmount with sales tax: " + str(totalYukon(amount)));
            break;