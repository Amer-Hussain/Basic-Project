unit = str(input("what is the Unit (C, F or K): ")) 
unit2 = str(input("what is the 2 Unit (C, F or K): ")) 
temp = float(input("what is the Temperature: "))

if unit == "C" or "c" and unit2 == "F" or "f": 
    f = (temp*9/5)+32
    # k = temp+273.15
    print(f"The temperature in Fahrenheit is {round(f, 2)}°F")
elif unit == "C" or "c" and unit2 == "K" or "k":
    # f = (temp*9/5)+32
    k = temp+273.15
    print(f"The temperature in Kelvin is {round(k, 2)}°K")


elif unit == "F" or "f" and unit2 == "C" or "c":
    c = (temp-32)*5/9
    # k = c+273.15
    print(f"The temperature in Celsius is {round(c, 2)}°C ")
elif unit == "F" or "f" and unit2 == "K" or "k":
    c = (temp-32)*5/9
    k = c+273.15
    print(f"The temperature in Kelvin is {round(k, 2)}°K ")


elif unit == "K" or "k" and unit2 == "C" or "c":
    c = temp-273.15
    # f = c*9/5+32
    print(f"The temperature in Celsius is {round(c, 2)}°C")
elif unit == "K" or "k" and unit2 == "F" or "f":
    c = temp-273.15
    f = c*9/5+32
    print(f"The temperature in Fahrenheit is {round(f, 2)}°F ")


else:
    print("The unit is not correct")
                
                
                
                
                
                
                
                
                
                
                # Wrong input
    # "F to C" (69°F − 32) × 5/9 = 20.556°C
    # "F to K" (0°F − 32) × 5/9 + 273.15 = 255.372K

                # for C to K & F
    # "C to F" (0°C × 9/5) + 32 = 32°F
    # "C to K" 0°C + 273.15 = 273.15K
                # for F to C & K
    # "F to C" (0°F − 32) × 5/9 = -17.78°c
    # "F to K" (0°F − 32) × 5/9 + 273.15 = 255.372K
                # for K to C & F
    # "K to C" 0K − 273.15 = -273.1°C
    # "K to F" (0K − 273.15) × 9/5 + 32 = -459.7°F