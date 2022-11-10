def bracketFunction():
    brackets= input('Введите скобочную последовательность: ')
    stack = []
    is_good = True

    for i in brackets:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                is_good = False
                break
            open_bracket = stack.pop()
            if open_bracket == '(' and i ==')':
                continue
            if open_bracket == '[' and i ==']':
                continue
            if open_bracket == '{' and i =='}':
                continue
            is_good = False
            break

    if is_good and len(stack) == 0:
        print('Yes')
    else:
        print('No')

# Дана скобочная последовательность: [((())()(())]], она считается неправильной, нужно удалить лишние открывающую и закрывающую скобки: [(())()(())]


