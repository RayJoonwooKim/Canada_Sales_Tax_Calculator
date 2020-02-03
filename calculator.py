from Functions.ChooseStates import *

yesChoices = ['Y', 'y'];
noChoices = ['N', 'n'];

print("Welcome to Canada Sales Tax Calculator!\n\n");

selectState();

while True:
    try:
        choice = str(input("\nDo you want to enter the new amount? (Y/N): "));
        if choice in yesChoices:
            print("\n");
            selectState();
        elif choice in noChoices:
            print("Thank you for using the program!");
            break;
        else:
            print("Please enter correct input! (Y or N)");
    except:
        break;