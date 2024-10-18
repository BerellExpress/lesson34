def apply_all_func(int_list, *functions):
    # Создаем пустой словарь результатов
    results = {}

    for func in functions:
        try:
            result = func(int_list)
            if isinstance(result, dict):
                results.update(result)
            else:
                results[func.__name__] = result
        except Exception as e:
            print(f"Ошибка при выполнении функции {func.__name__}: {e}")

    return results


# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))