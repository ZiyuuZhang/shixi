def check_brackets(input_string):
    stack = []
    result = ""

    num_left = 0     #统计左括号数量
    for char in input_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                stack.pop()     
                num_left += 1            #统计正确括号数量，即为正确的左括号数量
            
    num_right = 0       #统计右括号数量
    for char in input_string:
        if char == '(' and num_left != 0:           #在达到正确括号数量前，遇到的左括号均可认为是正确的
            result += ' '
            num_left -= 1
            num_right += 1  #对应正确右括号数量
        elif char == '(' and num_left == 0:
            result += 'x'
        elif char == ')' and num_right ==0:
            result += '?'
        elif char == ')' and num_right !=0:
            result += ' '
            num_right -= 1
        else:
            result += ' '

    return result

if __name__ == "__main__":
    while True:
        try:
            input_string = input()
            result = check_brackets(input_string)
            print(result)
        except EOFError:
            break