class classfunctions():
    def subfields(my_list):
        print("Sub-fields in AI are:")
        for item in my_list:
            print(item)

    def Odd_or_Even():
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            return(f"{num} is even number")
        else:
            return(f"{num} is odd number")

    def MarriageEligibility():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if (gender == "Male" or gender == "male") and age >= 21:
            return "Eligible"
        elif (gender == "Female" or gender == "female") and age > 18:
            return "Eligible"
        else:
            return "Not Eligible"

    def percentage():
        mark1 = int(input("Subject1= "))
        mark2 = int(input("Subject2= "))
        mark3 = int(input("Subject3= "))
        mark4 = int(input("Subject4= "))
        mark5 = int(input("Subject5= "))
        total = mark1+mark2+mark3+mark4+mark5
        print(f"Total : {total}")
        percentage = total/5
        return f"percentage: {percentage}"

    def Triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print(f"Area of triangle: {(Height*Breadth)/2}")
        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        breadth = int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+breadth")
        return f"Perimeter of triangle: {Height1+Height2+breadth}"