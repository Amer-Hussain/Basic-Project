unit = str(input("what is the Unit (C, F or K): ")) 
temp = float(input("what is the Temperature: "))
C = "C or c"
F = "F or f"
K = "K or k"


# -----------------------------------------------------------------------------------

                # for C to K & F
    # "C to F" (0°C × 9/5) + 32 = 32°F
    # "C to K" 0°C + 273.15 = 273.15K
if unit == "C" or "c":
    f = (temp*9/5)+32
    k = temp+273.15
    print(f"The temperature in Fahrenheit & Kelvin is {round(f, 2)}°F & {round(k, 2)}°K")

# -----------------------------------------------------------------------------------

                # for F to C & K
    # "F to C" (0°F − 32) × 5/9 = -17.78°C
    # "F to K" (0°F − 32) × 5/9 + 273.15 = 255.372K
elif unit == "F" or "f":
    c = (temp-32)*5/9
    k = c+273.15
    print(f"The temperature in Celsius & Kelvin is {round(c, 2)}°C {round(k, 2)}°K ")

    # -----------------------------------------------------------------------------------
                
                # for K to C & F
    # "K to C" 0K − 273.15 = -273.1°C
    # "K to F" (0K − 273.15) × 9/5 + 32 = -459.7°F

elif unit == "K" or "k":
    c = temp-273.15
    f = c*9/5+32
    print(f"The temperature in Celsius & Fahrenheit is {round(c, 2)}°C {round(f, 2)}°F ")
    
    # -----------------------------------------------------------------------------------

                # Wrong input
else:
    print("The unit is not correct")