while True:
    try: 
        value = int(input("Enter a value from 0 - 6: "))
        for x in range(6):
            if value > 6:
                print ("You've entered a large number.")
                break
            else: 
                value <= 6;
                print (x)
    except ValueError:
        print ("Invalid input.")