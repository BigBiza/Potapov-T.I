seconds = int(input('Введите количество секунд:'))
minutes = seconds // 60
hours = minutes // 60
days = hours // 24
secs = seconds % 60
mins = minutes % 60
h= hours % 24
print(days,':',h,':',mins,':',secs,)