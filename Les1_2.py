x = int(input("введите время в секундах:"))
h = x // 3600
min = (x // 60) - (h * 60)
sec = x - (h * 3600) - (min * 60)
print(f"{h:02}:{min:02}:{sec:02}")
