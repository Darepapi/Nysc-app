print("Hello ! \n Welcome to the Official page of NYSC.")

x=int(input("If you are here for Mobilization, Please press 1 or enter  2 to apply for Exemption Certificate"))
while x!=1 and x!=2:
    print("You just entered an incorrect value! \nPlease enter a correct value!")
    x=int(input("Press 1 for NYSC or 2 for Exemption Certificate.."))
if x==1:
    print("N.Y.S.C MOBILIZATION")
    names=input("Enter your username: ")
    print("Welcome, User", names)
    a=int(input("Please enter your Year  of birth: "))
    resultedYear= 2019-a
    if resultedYear>30:
        print("Hello, Dear",names,", Your age is above 30 and you can't be mobilized for N.Y.S.C. \nPlease, apply for Exemption Form")
    else:
        print("Congratulation! Dear ",names, " You are eligible for Mobilization. \n An application form will be sent to the provided email.")
elif x==2:
    print("EXEMPTION CERTIFICATION")
    nameE=input("Please enter your Username:")
    print("Welcome, User", nameE)
    print("Please fill in the follow details for the application of Exemption Certificate..")
    dateOfBirth=int(input("Date Of Birth: "))
    month=input("Month Of Birth: ")
    year=int(input("Year Of Birth: "))
    yearCalculated=2019-year
    print("Congratulation, Dear User ",nameE,"!  \n Your currently calculated age is  ",yearCalculated,". An application form will be sent to the provided email.")
    


