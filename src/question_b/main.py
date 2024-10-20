#add import
from question_b import reverse_string

def main():
    while True:
        user_input = input ("Enter a string to reverse or type exit: ")
        if user_input.lower() == 'exit':
            break
        reversed_value = reverse_string(user_input)
        print(f"Reversed: {reversed_value}")

    main()