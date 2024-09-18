from machine_instruc_generator import generate_machine_code
if __name__ == '__main__':

    # Program only runs when main.py is executed

    expression = input("Enter postfix expression:  ")



    with open('OUTPUT.txt', 'w') as output_file:
        output_file.write(f"Postfix expression:   {expression}\n")
        generate_machine_code(expression, output_file)

