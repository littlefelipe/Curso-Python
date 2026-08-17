# Python 3.14.3 (main, Jun 10 2026, 19:05:49) [GCC 13.3.0] on linux
numbers = [1,2,3]
new_numbers = [n for n in numbers]
numbers = [1,2,3]
new_numbers = [n + 3 for n in numbers]
name = "Felipe"
letters = [letter for letter in name]
rangex2 = [number * 2 for number in range(1,5)]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_names = [name.upper() for name in names if len(name) > 5]