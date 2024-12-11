def division(x=12, y=3, z=2):
    if y != 0 and z != 0:
        return x / y / z
    else:
        return "Division by zero!"
    
result = division(18)
print(result)