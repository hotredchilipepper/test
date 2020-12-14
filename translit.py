def translit(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|h|tc|ch|sh|shch||y||e|iu|ia'.split(
        '|')
    tab = {k: v for k, v in zip(cyrillic, latin)}
    newtext = ''
    for ch in text:
        func = str.capitalize if ch.isupper() else str.lower
        newtext += func(tab.get(ch.lower(), ch))
    return newtext

text = 'привет мир'
print(translit(text))
