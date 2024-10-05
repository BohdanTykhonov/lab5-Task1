N = int(input("Введіть кількість елементів масиву: "))
arr = []

print("Введіть елементи масиву:")
for i in range(N):
    arr.append(float(input(f"Елемент {i+1}: ")))

odd_elements = [arr[i] for i in range(N) if i % 2 == 0]
if len(odd_elements) > 0:
    avg_odd = sum(odd_elements) / len(odd_elements)
    print(f"Середнє арифметичне непарних елементів масиву: {avg_odd}")
else:
    print("Немає непарних елементів.")

negative_elements = [el for el in arr if el < 0]
if len(negative_elements) > 0:
    print("Від'ємні елементи у зворотному порядку:")
    print(negative_elements[::-1])
else:
    print("Від'ємних елементів немає.")
