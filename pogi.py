while True:
    try:
        tanong = input(str("POGI KA BA? (yes or no) "))
        if tanong.lower() != "yes":
            print ("hmmmm")
    except ValueError:
        print ("INVALID")
