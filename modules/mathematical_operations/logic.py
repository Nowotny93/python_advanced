def define_math_operation(m_op):
    if '*' in m_op:
        m_op_joined = ''.join(m_op)
        first_num = m_op_joined.split('*')[0]
        second_num = m_op_joined.split('*')[1]
        print(f'{float(first_num) * int(second_num):.2f}')
    elif '+' in m_op:
        m_op_joined = ''.join(m_op)
        first_num = m_op_joined.split('+')[0]
        second_num = m_op_joined.split('+')[1]
        print(f'{float(first_num) + int(second_num):.2f}')
    elif '-' in m_op:
        m_op_joined = ''.join(m_op)
        first_num = m_op_joined.split('-')[0]
        second_num = m_op_joined.split('-')[1]
        print(f'{float(first_num) - int(second_num):.2f}')
    elif '/' in m_op:
        m_op_joined = ''.join(m_op)
        first_num = m_op_joined.split('/')[0]
        second_num = m_op_joined.split('/')[1]
        print(f'{float(first_num) / int(second_num):.2f}')
    elif '^' in m_op:
        m_op_joined = ''.join(m_op)
        first_num = m_op_joined.split('^')[0]
        second_num = m_op_joined.split('^')[1]
        print(f'{float(first_num) ** int(second_num):.2f}')

def output(m_op):
    define_math_operation(m_op)