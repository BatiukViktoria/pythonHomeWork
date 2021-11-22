print("Введите числа через пробел, и нажмите Enter:")
input_string = input()

a = input_string.split()[0]
b = input_string.split()[1]

if a>b:
    print("Tут точно А > В")
if a<b:
    print("грустный_тромбон.мр3")
if a==b:
    print("UNBELIEVABLE")

