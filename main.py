while True:
    try:
        file: str = input('Введите слово: ')
        if len(file) < 3 or file.isalpha() == False:
            raise Exception
        with open(f'{file}.txt', 'w') as file:
            break
    except Exception:
        print('Введите слово корректно')
        continue


