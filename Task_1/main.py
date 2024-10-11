def caching_fibonacci():
    cache = {}  # Створюємо порожній словник для кешу

    def fibonacci(n):  # Вкладена функція для обчислення чисел Фібоначчі
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Обчислюємо значення Фібоначчі рекурсивно і зберігаємо в кеш
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))