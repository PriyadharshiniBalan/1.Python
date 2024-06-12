class MultipleFunctions:
    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area = (height*breadth)/2
        print("Area of Triangle: ",area)
    
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ", height1+height2+breadth1)
    
    def Subfields():
        fields = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        print('Sub-fields in AI are:')
        for field in fields:
            print(field)

    def OddEven():
        num = int(input("Enter a number: "))
        if (num%2 == 0):
            print(num, "is Even number")
        else:
            print(num, "is Odd number")

    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your Age: "))
        if (gender == 'Male' and age >= 21) or (gender == 'Female' and age >= 18):
            print('ELIGIBLE')
        else:
            print('NOT ELIGIBLE')

    def percentage():
        total = 0
        for i in range(0,5):
            mark = int(input(f"Subject{i+1}= "))
            total += mark
        print("Total :", total)
        print("Percentage :", total/5)