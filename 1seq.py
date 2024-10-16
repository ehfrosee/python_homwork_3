len_list = int(input("Введите количество элементов: "))

digit_list = []

for i in range(len_list):
    digit = input('Введиде цифру:')
    digit_list.append(int(digit))

digit_list.sort()
print(digit_list)