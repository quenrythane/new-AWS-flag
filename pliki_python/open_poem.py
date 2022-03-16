def open_poem():
    text_lines = open('dane/ukraiński_wiersz.txt', encoding='utf-8').readlines()
    text_lines = list(map(lambda x: x.strip(), text_lines))
    return text_lines[2:]


print(open_poem()[-10:])
