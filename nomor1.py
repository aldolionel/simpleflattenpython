def check(sentence):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    a = list(char for char in sentence)
    b = ['{','(',')','[',']','}'] 
    myList = []

    for sym in a:
        for brack in b:
            if sym == brack:
                myList.append(sym)
    
    stack = []
    for i in myList:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False



print(check('abcd(ex45{uuuu)000]ccc'))