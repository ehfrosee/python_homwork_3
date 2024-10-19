digit_string = input('Введите цифры. (допустимый разделитель: , ; /)')
seps = [',', ';', '/']

unique_list = []
for sep in seps:
  if digit_string.find(sep) != -1:
    dig_list = digit_string.split(sep)
    dig_set = set(digit_string.split(sep))
    for dig in dig_set:
      if dig_list.count(dig) == 1:
        unique_list.append(dig)
    break
print(unique_list)
