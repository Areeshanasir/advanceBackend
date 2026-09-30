# --- Scenario 1: When x is NOT defined (Triggers the except block) ---
print("--- Scenario 1 ---")
try:
    print(x)  # x is not defined, causes an error
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished\n")


# --- Scenario 2: When x IS defined (Runs successfully) ---
print("--- Scenario 2 ---")
try:
    x = "Hello, Python!"
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")