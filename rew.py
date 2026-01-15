while True:
    try:
        number = int(input("Enter a number"))
        if number >= 0 and number <=100:
            break
        else:
            print("invalid")                
    except ValueError:
        print("Please enter a valid integer.")