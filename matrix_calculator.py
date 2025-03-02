import numpy as np


def get_matrix(rows, cols, name):
    print(f"Введите элементы матрицы {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        if len(row) != cols:
            print("Ошибка: Пожалуйста, введите правильное количество элементов!")
            return get_matrix(rows, cols, name)
        matrix.append(row)
    return np.array(matrix)


def main():
    rows = int(input("Введите количество строк матриц: "))
    cols = int(input("Введите количество столбцов матриц: "))

    A = get_matrix(rows, cols, 'A')
    B = get_matrix(rows, cols, 'B')

    while True:
        print("\nВыберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            print("Сумма матриц:\n", A + B)
        elif choice == '2':
            print("Разность матриц:\n", A - B)
        elif choice == '3':
            if A.shape[1] == B.shape[0]:
                print("Произведение матриц:\n", np.dot(A, B))
            else:
                print("Ошибка: Размерности матриц не соответствуют для умножения!")
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Неверный выбор, попробуйте снова!")


if __name__ == "__main__":
    main()
