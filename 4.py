print('Введите количество секунд:')
seconds = int(input())
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
print(seconds,'сек = ',minutes,'мин','/',hours,'ч','/',days,'д')