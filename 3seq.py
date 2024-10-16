digit_string = input('Введите список цифр . (допустимый разделитель: , ; /)')
del_digit = input('Введите удаляемые цифры . (допустимый разделитель: , ; /)')
seps = [',', ';', '/']

for sep in seps:
  if digit_string.find(sep) != -1:
    dig_list = digit_string.split(sep)
    break

for sep in seps:
  if del_digit.find(sep) != -1:
    del_list = del_digit.split(sep)
    break
for dig in dig_list.copy():
    if dig in del_list:
        dig_list.remove(dig)

print(dig_list)