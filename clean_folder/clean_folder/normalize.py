def normalize(name: str) -> str:
    cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    lat = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
           "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    trans_dict = {}

    for c, l in zip(cyrillic, lat):
        trans_dict[ord(c.upper())] = l.upper()
        trans_dict[ord(c)] = l
    trans_name = name.translate(trans_dict)
    new_name = ''

    for ch in trans_name:
        if 'a' <= ch.lower() <= 'z' or '0' <= ch <= '9' or ch == '.':
            new_name += ch
        else:
            new_name += '_'
    return new_name
