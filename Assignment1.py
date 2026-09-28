# Question 1

try:
  age = int(input("Please enter your age: "))

  if age < 18:
    print("You are a minor.")
  elif 18 <= age <= 65:
    print("You are an adult.")
  else:
    print("You are a senior citizen.")

except ValueError:
  print("Invalid input. Please enter a valid numerical value for your age.")
  
  
  # Question 2
  
def calculator():
  try:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ").strip()
    num2 = float(input("Enter the second number: "))

    match operator:
      case "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
      case "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
      case "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
      case "/":
        if num2 == 0:
          print("Error: Division by zero is not allowed.")
        else:
          result = num1 / num2
          print(f"Result: {num1} / {num2} = {result}")
      case _:
        print("Invalid operator. Please choose from +, -, *, /.")

  except ValueError:
    print("Invalid input. Please enter valid numerical values for the numbers.")


if __name__ == "__main__":
  calculator()
  
  
  #Question 3
  
 
n = int(input("Enter the number of terms (n): "))


if n <= 0:
  print("Error: Please enter a positive integer greater than 0.")
else:

  fib_sequence = []
  a, b = 0, 1

  for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

  print(f"Fibonacci sequence up to {n} terms:")
  print(", ".join(map(str, fib_sequence)))