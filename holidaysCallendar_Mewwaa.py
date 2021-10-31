# Author: Ewa Zalewska
# Concept: Holidays callendar in Python
# Github: https://github.com/Mewwaa

from dateutil.relativedelta import relativedelta
from datetime import date
import datetime
import holidays


Argentina = holidays.Argentina()
Australia = holidays.Australia()
Austria = holidays.Austria()
Belgium = holidays.Belgium()
Canada = holidays.Canada()
Colombia = holidays.Colombia()
Czech = holidays.Czech()
Denmark = holidays.Denmark()
Finland = holidays.Finland()
France	= holidays.France()
Germany = holidays.Germany()
Hungary = holidays.Hungary()
Ireland = holidays.Ireland()
Italy = holidays.Italy()
Japan = holidays.Japan()
Mexico	= holidays.Mexico()
Netherlands = holidays.Netherlands()
NewZealand = holidays.NewZealand()
Norway = holidays.Norway()
Poland = holidays.Polish()
Portugal = holidays.Portugal()
Scotland = holidays.Scotland()
Slovenia = holidays.Slovenia()
Slovakia = holidays.Slovakia()
SouthAfrica = holidays.SouthAfrica()
Spain = holidays.Spain()
Sweden = holidays.Sweden()
Switzerland = holidays.Switzerland()
UnitedKingdom = holidays.UnitedKingdom()
UnitedStates = holidays.UnitedStates()
Wales = holidays.Wales()



print("Hello, please enter the number of the country whose holiday you want to check from the list below")
print("-----------------------")
print("1. Argentina")
print("2. Australia")
print("3. Austria")
print("4. Belgium")
print("5. Canada")
print("6. Colombia")
print("7. Czech")
print("8. Denmark")
print("9. Finland")
print("10. France")
print("11. Germany")
print("12. Hungary")
print("13. Ireland")
print("14. Italy")
print("15. Japan")
print("16. Mexico")
print("17. Netherlands")
print("18. NewZealand")
print("19. Norway")
print("20. Poland")
print("21. Portugal")
print("22. Scotland")
print("23. Slovenia")
print("24. Slovakia")
print("25. SouthAfrica")
print("26. Spain")
print("27. Sweden")
print("28. Switzerland")
print("29. UnitedKingdom")
print("30. UnitedStates")
print("31. Wales")
print("")
print("0. EXIT")
print("-----------------------")


choice=int(input("Enter your choice: "))


while True:
    if choice == 1:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Argentina.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 2:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Australia.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 3:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Austria.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 4:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Belgium.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 5:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Canada.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 6:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Colombia.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 7:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Czech.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 8:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Denmark.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 9:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Finland.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 10:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+France.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 11:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Germany.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 12:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Hungary.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 13:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Ireland.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 14:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Italy.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 15:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Japan.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 16:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Mexico.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 17:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Netherlands.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 18:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+NewZealand.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 19:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Norway.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 20:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Poland.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 21:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Portugal.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 22:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Scotland.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 23:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Slovenia.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 24:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Slovakia.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 25:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+SouthAfrica.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 26:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Spain.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 27:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Sweden.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 28:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Switzerland.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 29:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+UnitedKingdom.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 30:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+UnitedStates.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 31:
        print(" ")
        date=str(input("Enter the date you want to check: "))
        print(" ")
        print("**************************")
        print("This date is "+Wales.get(date))
        print(" ")
        input("Press Enter to continue...") 
        break

    elif choice == 0:
        break

    else:
        print("Something went wrong")

    

input("Press Enter to continue...")