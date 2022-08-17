def get_postfix_form(s):

    def is_op(s):
        match s:
            case '+' | '-' | '*' | '/': return True
        return False

    def is_bracket(s):
        match s:
            case '(' | ')': return True
        return False

    def is_num(s):
        return not is_op(s) and not is_bracket(s)

    def prior(op):
        match op:
            case '+' | '-': return 1
            case '*' | '/': return 2

    for symb in s:
        if not is_num(symb):
            s = s.replace(symb, ' ' + symb + ' ')
    lis = s.split()
    st  = []
    que = []
    for e in lis:
        if is_num(e):
            que.append(e)
        elif is_op(e):
            while st and is_op(st[-1]) and prior(e) <= prior(st[-1]):
                que.append( st.pop() )
            if not st or st[-1] == '(' or is_op(st[-1]) and prior(e) > prior(st[-1]):
                st.append(e)
        elif e == '(':
            st.append(e)
        elif e == ')':
            while st and st[-1] != '(':
                que.append( st.pop() )
            if st:
                st.pop()
    while st:
        que.append( st.pop() )
    return ' '.join(que)

while True:
    exp = input( 'Enter an arithmetic expression in infix form: ' )
    print( f'This is the same expression in postfix form: { get_postfix_form(exp) }' )
    print()