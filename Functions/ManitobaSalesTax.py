def gstManitoba(amount):
    return round(amount * 0.05, 2);

def pstManitoba(amount):
    return round(amount * 0.07, 2);

def totalManitoba(amount):
    return round(amount + gstManitoba(amount) + pstManitoba(amount),2);

def calculateManitoba():
    while True:
        try:
            amount = float(input("Please enter your amount before sales tax: $"));
        except ValueError:
            print("Invalid input. Please try again!");
        else:
            print("Amount before sales tax: " + str(amount) + "\nGST: " + str(gstManitoba(amount)) + "\nPST: " + str(pstManitoba(amount)) + "\nAmount with sales tax: " + str(totalManitoba(amount)));
            break;