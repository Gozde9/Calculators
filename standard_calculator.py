def get_complex_number(name):
    while True:
        try:
            return complex(input(f"Введите комплексное число {name} (пример: 1+2j): "))
        except ValueError:
            print("Ошибка: Введите корректное комплексное число!")


def main():
    while True:
        print("\nВыберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Выход")
        choice = input("Ваш выбор: ")

        if choice in {'1', '2', '3', '4'}:
            A = get_complex_number('A')
            B = get_complex_number('B')

        if choice == '1':
            print(f"Результат сложения: {A + B}")
        elif choice == '2':
            print(f"Результат вычитания: {A - B}")
        elif choice == '3':
            print(f"Результат умножения: {A * B}")
        elif choice == '4':
            if B != 0:
                print(f"Результат деления: {A / B}")
            else:
                print("Ошибка: Деление на ноль невозможно!")
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова!")


if __name__ == "__main__":
    main()
