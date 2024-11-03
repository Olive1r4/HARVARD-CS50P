def main():
# Ask user for input X, Y and Z. X and Z are integers, Y is a string.
    x, y, z = input_values()
    print(f'The result of {x} {y} {z} is {calculate(x, y, z)}')
# return inputs from user
def input_values():
    # Ask for inputs and check if they are valid
    while True:
        try:
            x = int(input('Please enter an integer for X: '))
        except ValueError:
            print('Please enter a valid input')
            continue
        while True:
            y = input('Please enter a string for Y (+, -, *, /): ')
            if y in ['+', '-', '*', '/']:
                break
            else:
                print('Please enter a valid input')
        try:
            z = int(input('Please enter an integer for Z: '))
        except ValueError:
            print('Please enter a valid input')
            continue
        break
    return x, y, z

# Perform the calculation based on the operator
def calculate(x, y, z):
    # Perform the calculation based on the operator
    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '*':
        return x * z
    else:
        return x / z
 
if __name__ == '__main__':
    main()