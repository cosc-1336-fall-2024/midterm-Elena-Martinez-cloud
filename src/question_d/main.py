#add import
from question_d import get_assessment_value, get_tax_assessed

def main():
    while True:
        try:
            user_input = ("Enter the land value or enter 'exit' to quit: ")
            if user_input.lower() == 'quit':
                break

            actual_value = float(user_input)
            assessment_value = get_assessment_value(actual_value)
            tax_assessed = get_tax_assessed(assessment_value)

            print(f"Assessment Value: ${assessment_value: .2f}")
            print(f"Property Tax: ${tax_assessed:.2f}")
        except ValueError:
            print("Invalid! Enter a valid number.")

    main()


