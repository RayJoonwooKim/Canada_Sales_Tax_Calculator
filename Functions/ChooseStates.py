from Functions.QuebecSalesTax import *
from Functions.AlbertaSalesTax import *
from Functions.BCSalesTax import *
from Functions.ManitobaSalesTax import *
from Functions.NewBrunswickSalesTax import *
from Functions.NLSalesTax import *
from Functions.NTSalesTax import *
from Functions.NovaScotiaSalesTax import *
from Functions.NunavutSalesTax import *
from Functions.OntarioSalesTax import *
from Functions.PEISalesTax import *
from Functions.SaskatchewanSalesTax import *
from Functions.YukonSalesTax import *
from os import system

def selectState():
    range = [1,2,3,4,5,6,7,8,9,10,11,12,13];
    while True:
        try:
            print("\n1. Alberta");
            print("2. British Colombia");
            print("3. Manitoba");
            print("4. New Brunswick");
            print("5. Newfoundland and Labrador");
            print("6. Northwest Territories");
            print("7. Nova Scotia");
            print("8. Nunavut");
            print("9. Ontario");
            print("10. Prince Edward Island");
            print("11. Quebec");
            print("12. Saskatchewan");
            print("13. Yukon");
            choice = int(input("\nPlease choose your state: "));
            if choice == 1:
                calculateAlberta();
                break;
            elif choice == 2:
                calculateBC();
                break;
            elif choice == 3:
                calculateManitoba();
                break;
            elif choice == 4:
                calculateNB();
                break;
            elif choice == 5:
                calculateNL();
                break;
            elif choice == 6:
                calculateNT();
                break;
            elif choice == 7:
                calculateNovaScotia();
                break;
            elif choice == 8:
                calculateNunavut();
                break;
            elif choice == 9:
                calculateOntario();
                break;
            elif choice == 10:
                calculatePEI();
                break;
            elif choice == 11:
                calculateQuebec();
                break;
            elif choice == 12:
                calculateSaskatchewan();
                break;
            elif choice == 13:
                calculateYukon();
                break;
            elif choice not in range:
                system('cls');
                print("Please enter the number for your state!");
        except ValueError:
            print("Please enter the number for your state!");
