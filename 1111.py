my_shelf = dict()

#допиши введення даних і додавання їх до словника
a = input("Введіть автора:")
books = []
book = input("Введіть книгу (s - cтоп):")
while book != "s":
    books.append(book)
    book = input("Введіть книгу (s - cтоп):")
my_shelf[a] = books
print(my_shelf)