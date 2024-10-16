digit_string = input('Введите цифры. (допустимый разделитель: , ; /)')
seps = [',', ';', '/']

for sep in seps:
  if digit_string.find(sep) != -1:
    dig_list = list(set(digit_string.split(sep)))
    break
print(dig_list)