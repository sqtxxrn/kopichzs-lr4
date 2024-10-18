import random


def is_multiple_of_5_or_7(column):
    """Проверяет, содержит ли столбец только кратные 5 или 7."""
    for value in column:
        if value % 5 != 0 and value % 7 != 0:
            return False
    return True


def get_column(matrix, col_index):
    """Извлекает элементы заданного столбца из матрицы."""
    return [row[col_index] for row in matrix]


def find_columns(matrix):
    """Находит индексы столбцов, содержащих только кратные 5 или 7."""
    column_indices = []

    if not matrix or not matrix[0]:  # Проверка на пустую матрицу
        return column_indices

    num_columns = len(matrix[0])

    for col in range(num_columns):
        column_data = get_column(matrix, col)
        if is_multiple_of_5_or_7(column_data):
            column_indices.append(col)

    return column_indices


def generate_random_matrix(rows, cols, min_value=1, max_value=100):
    """Генерирует матрицу с случайными натуральными числами."""
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]


def main():
    # Генерация случайных матриц размером 3x3
    array1 = generate_random_matrix(3, 3)
    array2 = generate_random_matrix(3, 3)

    # Вывод сгенерированных массивов
    print("Сгенерированный массив 1:")
    for row in array1:
        print(row)

    print("\nСгенерированный массив 2:")
    for row in array2:
        print(row)

    # Поиск и вывод валидных столбцов
    for i, array in enumerate([array1, array2], start=1):
        print(f"\nМассив {i}:")
        columns = find_columns(array)
        if columns:
            print(f"Столбцы, содержащие только кратные 5 или 7: {columns}")
        else:
            print("Нет столбцов с кратными 5 или 7")


if __name__ == "__main__":
    main()