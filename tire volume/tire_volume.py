# i used a while loop to continue asking if the user say yes
# in the end the program asks to display the stored data

from math import pi
from datetime import datetime

while True:
    # prompt the user for questions
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    # calculation to find the tire volume
    tire_volume = (pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    # display result
    print(f"The approximate volume is {tire_volume:.2f} liters")


    """
    Exceeding the Requirements
    """
    current_date = datetime.today()
    current_date = (f"{current_date:%Y-%m-%d}")

    with open("Volume.txt", "at") as volumes_file:
        print()
        buy_tire = input("Do you want to buy tires with the dimesions you entered? [YES/NO] ").lower()
        if buy_tire == "yes":
            phone_number = input("insert your phone number: ")
            
            print(f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {tire_volume:.2f}, {phone_number}", file=volumes_file)

        if buy_tire == "no":
            print(f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {tire_volume:.2f}, ", file=volumes_file)

    add_again = input("Do you want to calculate the volume of another tire? [YES/NO] ").lower()
    if add_again == "yes":
        print()
        print("New Values:")
        continue

    else:
        print("Thank you for using.")

        data = input("Do you want to see the volume data file: [YES/NO] ").lower()
        if data == "yes":
            print()
            print("Volume Tire Data:")
            with open("volume.txt", "r") as exemplo:
                for i in exemplo:
                    print(f"{i}", end="")
        break
