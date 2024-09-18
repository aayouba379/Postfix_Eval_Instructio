from stack import Stack
from validation import is_postfix_valid

def generate_machine_code(postfix, output_file):

    stack = Stack()
    counter = 1

    # Remove white spaces
    tokens = postfix.replace(' ', '')

    if not is_postfix_valid(postfix):
        output_file.write('Invalid postfix\n')
        return f"End of Operation"

    for e in tokens:

        if e.isalpha():        # Check operands are letters
            stack.push(e)

        elif e in '^*/+-' :

            #Check if list have enough operands to perform operation
            if stack.size() < 2:
                output_file.write(f"Not enough operands in stack\n")
                return f"End of Operation"

            operand2 = stack.pop()
            operand1 = stack.pop()

            temp = f"TEMP{counter}"    # Initializing temporary variables
            counter += 1

            if e == '-':
                output_file.write(f"{'LD':8}{operand1}\n")
                output_file.write(f"{'SB':8}{operand2}\n")
            elif e == '+':
                output_file.write(f"{'LD':8}{operand1}\n")
                output_file.write(f"{'AD':8}{operand2}\n")
            elif e == '*':
                output_file.write(f"{'LD':8}{operand1}\n")
                output_file.write(f"{'ML':8}{operand2}\n")
            elif e == '^':
                output_file.write(f"{'LD':8}{operand1}\n")
                output_file.write(f"{'EX':8}{operand2}\n")
            else:
                output_file.write(f"{'LD':8}{operand1}\n")
                output_file.write(f"{'DV':8}{operand2}\n")


            output_file.write(f"{'ST':8}{temp}\n")
            stack.push(temp)

    # Ensure stack is completely empty
    if not stack.is_empty():
        for i in range(stack.size()):
            stack.pop()

    return f"End of Operation"

