# Классический алгоритм на python: Быстрая сортировка
def quick_sort(array):
    # Если массив состоит из одного элемента, возвращаем его
    if len(array) < 2:
        return array
    else:
        # Выбираем опорный элемент. В данном случае - это первый элемент массива.
        pivot = array[0]
        # Составляем подмассив всех элементов, меньших опорного.
        less = [i for i in array[1:] if i <= pivot]
        # Составляем подмассив всех элементов, больших опорного.
        greater = [i for i in array[1:] if i > pivot]
        
# Рекурсивно сортируем и объединяем подмассивы.
return quick_sort(less) + [pivot] + quick_sort(greater)

# Пример использования:
unsorted_array = [10, 5, 2, 3]
print(quick_sort(unsorted_array)) 
# Результат: [2, 3, 5, 10]