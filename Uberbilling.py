Bike=10
Auto=15
Cab=25
print("Welcome to Uber\n1.Bike\n2.Auto\n3.cab")
option=(input("Enter your vehicle from above"))


if option=="1" or option=="Bike":
    c=int(input("Enter the Current Location:"))
    d=int(input("Enter the Destination:"))
    dis=c-d
    print("-----------------------")
    print("Your Current Location:",c)
    print("Your Destination:",d)
    print("Total Distance is:",dis)
    amount=dis*Bike
    print("Amount to be paid:",amount)
    print("Enjoy your ride")
elif option=="2" or option=="Auto":
    c=int(input("Enter the Current Location:"))
    d=int(input("Enter the Destination:"))
    dis=c-d
    print("-----------------------")
    print("Your Current Location:",c)
    print("Your Destination:",d)
    print("Total Distance is:",dis)
    amount=dis*Auto
    print("Amount to be paid:",amount)
    print("Enjoy your ride")
elif option=="3" or option=="Cab":
    c=int(input("Enter the Current Location:"))
    d=int(input("Enter the Destination:"))
    dis=c-d
    print("-----------------------")
    print("Your Current Location:",c)
    print("Your Destination:",d)
    print("Total Distance is:",dis)
    amount=dis*Cab
    print("Amount to be paid:",amount)
    print("Enjoy your ride")
else:
    print("Enter only above three number or vehicle")
   

    
