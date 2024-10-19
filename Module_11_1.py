# импортируем библиотеку
import numpy as np

# создадим numpy массив из списка

data = [5, 7, 11, 8, 12]
arr = np.array(data)

print(arr)
print(arr.ndim) # проверяем сколько-мерный массив

arr1 = np.arange(0, 5, 1.5)  # функция, подобная range(), но умеет работать и с дробными числами
print(arr1)

arr2 = np.array([1, 2, 3, 4])  #все элементы * на 2
arr2 = arr2*2

print(arr2)

#Функции агрегаты
arr3 = np.random.randint(-5, 10, 10)  #генерируем случайные числа

print(arr3)
print(arr3.max())
print(arr3.min())
print(arr3.sum())

# Функции и одномерные массивы
arr4 = np.array([2, -1, 5, 8, -5 ])

print(arr4[2])    
print(arr4[:3])
print(arr4[(arr<8) & (arr>2)])  #подобно как со списками, но есть и другие удобные можности

arr4[1:4] = 0
print(arr4)

#Матрицы и многомерные массивы
matrix = np.array([(1, 2, 3), (4, 5, 6)])  # двухмерный массив

print(matrix)

matrix1 = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])  # трехмерный массив

print(matrix1)








