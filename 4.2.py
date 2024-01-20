inch_to_cm = 2.54

while True:

    inches = float(input("Enter a length in inches (or a negative value to exit): "))


    if inches <= 0:
        print("Exiting the program.")
        break


    cm = inches * inch_cm
    print(f"{inches} inches is equal to {cm:.2f} centimeters")
