while True:
    userInput = float(input("Celsius:"))
    try:
        Fahrenheit = int(userInput) * 9/5 + 32
        print (Fahrenheit)

        choice = input ("Do you want to continue?")
        if choice.lower() != "yes":
            break

    except ValueError:
        print ("Invalid Input.")