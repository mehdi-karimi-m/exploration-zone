from timeit import timeit

code1 = """
def xfactor_calculator(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")

    return 10 / age

    
try:
    xfactor_calculator(0)
except ValueError as error:
    pass
"""

code2 = """
def xfactor_calculator(age):
    if age <= 0:
        return None
    
    return 10 / age

result = xfactor_calculator(0)
if result == None:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
