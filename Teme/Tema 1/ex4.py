numar = input('Introduceti un numar:')
if numar.isalpha():
    print(f' Caracterele introduse {numar.upper()} este de tip Alpha')
elif 0 < int(numar) <= 10:
    print(f' Numarul introdus {numar} este valid')
elif int(numar) > 10:
    print(f' Numarul introdus {numar} este mai mare ca 10')
elif int(numar) == 0:
    print(f' Numarul introdus {numar} este 0')
elif int(numar) < 0:
    print(f' Numarul introdus {numar} este negativ')
    print(f' Numarul introdus {numar} este negativ si a fost transformat in numarul pozitv {abs(int(numar))}')
