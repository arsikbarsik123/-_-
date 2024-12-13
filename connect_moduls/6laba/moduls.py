
with open("example.txt", "w") as file:
    file.write("privet privet privet privet privet \n")
    file.write("privet privet privet privet privet \n")    
    file.write("privet privet privet privet privet \n")

def format_text(text, alignment):
    """
    1. Вывести форматированный текст: по левому, по центру, по правому краю.
    """
    width = 50
    if alignment == "left":
        return text.ljust(width)
    elif alignment == "center":
        return text.center(width)
    elif alignment == "right":
        return text.rjust(width)
    else:
        raise ValueError("Неверный тип выравнивания. Используйте left, center или right.")

def create_table(rows, cols):
    """
    2. Вывести псевдографикой таблицу со строками и столбцами.
    """
    table = []
    for i in range(rows):
        row = "|" + "|".join([" " * 5 for _ in range(cols)]) + "|"
        separator = "+" + "+".join(["-" * 5 for _ in range(cols)]) + "+"
        table.append(row)
        table.append(separator)
    return "\n".join(table[:-1])

def remove_characters_from_file(file_name, chars):
    """
    3. Считать строку из файла. Вычеркнуть из неё символы, полученные из клавиатуры.
    """
    with open(file_name, "r") as file:
        content = file.read()
    filtered_content = "".join([c for c in content if c not in chars])
    return filtered_content

def search_string_in_file(file_name, query):
    """
    5. Считать строку с клавиатуры. Выполнить её поиск в файле в режиме неполного соответствия.
    Вывести номер последней строки, удовлетворяющей условию (для мальчиков).
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    last_match = -1
    for i, line in enumerate(lines):
        if query in line:
            last_match = i + 1
    return last_match if last_match != -1 else "Совпадений не найдено."

def reverse_scrolling_text(file_name):
    """
    7. Считать строку из файла и вывести её в формате бегущей строки, движущейся в обратном направлении (для мальчиков).
    """
    with open(file_name, "r") as file:
        content = file.read().strip()
    for i in range(len(content), 0, -1):
        print(content[i:] + content[:i], end="\r")