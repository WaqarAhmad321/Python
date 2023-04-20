# To convert the temperature from farenhiet to Celsius
def conversion(cel):
    result = (cel * (9/5)) + 32
    return result


cel = int(input("Enter the temperature : \n"))
print("The temperature in farenhiet is :", conversion(cel))
