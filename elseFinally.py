
print("--- Scenario 1 (Success) ---")
try:
    x = 10
    print(f"Value of x: {x}")
except ZeroDivisionError:
    print("Caught a division by zero error!")
else:
    print("Success! No exception was raised.")
finally:
    print("The 'try except' is finished.\n")


print("--- Scenario 2 (Error) ---")
try:
    x = 10 / 0  
    print(f"Value of x: {x}")
except ZeroDivisionError:
    print("Caught a division by zero error!")
else:
    print("Success! No exception was raised.") 
finally:
    print("The 'try except' is finished.")