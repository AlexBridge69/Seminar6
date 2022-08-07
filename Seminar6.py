'''
Задача 1.
Написать программу вычисления арифметического выражения заданного строкой.
Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
'''
cur_idx=0

def is_bracket_valid(expr: str) -> bool:
    parity=0
    for char in expr:
        if char=='(':
            parity+=1
        elif char==')':
            parity-=1
        else:
            pass
        if parity<0:
            return False
    return parity==0

def skip_spaces(expr: str):
    global cur_idx
    while cur_idx<len(expr) and expr[cur_idx].isspace():
        cur_idx+=1

def get_number(expr: str):
    global cur_idx
    is_int=True
    num_idx=cur_idx
    while cur_idx<len(expr) and expr[cur_idx].isdigit():
        cur_idx+=1
    if cur_idx<len(expr) and expr[cur_idx]=='.':
        is_int=False
        cur_idx+=1
    while cur_idx<len(expr) and expr[cur_idx].isdigit():
        cur_idx+=1
    
    return int(expr[num_idx:cur_idx]) if is_int else float(expr[num_idx:cur_idx])

def get_term_3(expr: str):
    global cur_idx
    skip_spaces(expr)

    if cur_idx>len(expr)-1:
        return
    
    if expr[cur_idx] == '(':
        cur_idx+=1
        exp=get_expr(expr)
        skip_spaces(expr)
        if expr[cur_idx]==')':
            cur_idx+=1
            return exp
        else:
            print("Не парные скобки!")
            return
    
    return get_number(expr)

def get_term_2(expr: str):
    global cur_idx
    skip_spaces(expr)

    if expr[cur_idx]=='-':
        cur_idx+=1
        return -get_term_3(expr)
    return get_term_3(expr)

def get_term_1(expr: str):
    global cur_idx
    skip_spaces(expr)
    term_2=get_term_2(expr)
    if cur_idx>len(expr)-1:
        return term_2
    
    skip_spaces(expr)
    if expr[cur_idx]=='*':
        cur_idx+=1
        return term_2*get_term_1(expr)
    elif expr[cur_idx]=='/':
        cur_idx+=1
        return term_2/get_term_1(expr)

    return term_2

def get_expr(expr: str):
    global cur_idx
    skip_spaces(expr)

    term_1=get_term_1(expr)
    if cur_idx>len(expr)-1:
        return term_1
    
    skip_spaces(expr)

    if expr[cur_idx]=='+':
        cur_idx+=1
        return term_1+get_expr(expr)
    elif expr[cur_idx]=='-':
        cur_idx+=1
        return term_1-get_expr(expr)
    
    return term_1

def evaluate(expr: str):
    if expr is None or len(expr)==0:
        print('Пустое выражение')
        return
    else:
        if is_bracket_valid(expr):
            return get_expr(expr)
        else:
            print('Не соответствие открытых и закрытых скобок')
            return

while True:
    expr=input("Введите выражение для рассчёта (чтобы выйти, нажмите 'x'): ")
    if expr=='x':
        break
    print(f' ={evaluate(expr)}')
    cur_idx=0

'''
Задача 2.
Реализовать RLE алгоритм. Реализовать модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 
'''

def compressing_text(original_text):
    compressed_text = ""
    i = 0
    while (i <= len(original_text)-1):
        count = 1
        ch = original_text[i]
        j = i
        while (j < len(original_text)-1):    
            if (original_text[j] == original_text[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        compressed_text = compressed_text + str(count) + ch
        i = j + 1
    return compressed_text

def decompressing_text(incoming_text):
    decompressed_text = ""
    i = 0
    j = 0
    while (i <= len(incoming_text) - 1):
        run_count = int(incoming_text[i])
        run_word = incoming_text[i + 1]
        for j in range(run_count):
            decompressed_text = decompressed_text+run_word
            j = j + 1
        i = i + 2
    return decompressed_text


with open("original_text.txt", "r") as original:
    original_data=original.read()

encoded=compressing_text(original_data)

with open("compressed_text.txt", 'w') as result_file:
    result_file.write(encoded)

