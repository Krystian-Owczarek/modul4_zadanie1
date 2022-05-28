def is_palindrom(keyword):
    rev_keyword = reversed(keyword)
    if list(keyword) == list(rev_keyword):
        print("to palindrom")
    else:
        print("nie jest palindromem")

keyword = input('Słowo: ')
is_palindrom(keyword)