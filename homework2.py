import time
import multiprocessing

def factorize_number(n):
    """Знаходить усі дільники числа n"""
    return [i for i in range(1, n + 1) if n % i == 0]

def factorize(*numbers, parallel=False):
    """
    Функція знаходить дільники для списку чисел.
    
    :param numbers: Числа для факторизації
    :param parallel: Використовувати багатопроцесорність (True/False)
    :return: Список списків дільників
    """
    if parallel:
        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            results = pool.map(factorize_number, numbers)
    else:
        results = [factorize_number(num) for num in numbers]
    
    return results

# Тестування та замір часу
numbers = (128, 255, 99999, 10651060)

start_time = time.time()
a, b, c, d = factorize(*numbers, parallel=False)
end_time = time.time()
print("Синхронний час виконання:", end_time - start_time)

start_time = time.time()
a, b, c, d = factorize(*numbers, parallel=True)
end_time = time.time()
print("Паралельний час виконання:", end_time - start_time)

# Перевірка коректності
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


