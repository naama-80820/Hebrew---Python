from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For, List

def generate_code(node):
    switch = {
        Num: generate_num,
        Str: generate_str,
        Var: generate_var,
        VarAssign: generate_var_assign,
        BinOp: generate_bin_op,
        Print: generate_print,
        If: generate_if,
        Else: generate_else,
        While: generate_while,
        For: generate_for,
        List: generate_list,
    }
    generator = switch.get(type(node), lambda _: "")
    return generator(node)

def generate_num(node):
    return str(node.value)

def generate_str(node):
    return f'"{node.value}"'

def generate_var(node):
    return node.name

def generate_var_assign(node):
    return f"{node.name} = {generate_code(node.value)}"

def generate_bin_op(node):
    left = generate_code(node.left)
    right = generate_code(node.right)
    return f"{left} {node.op} {right}"

def generate_print(node):
    value = generate_code(node.value)
    return f"print({value})"

def generate_if(node):
    code = f"if {generate_code(node.condition)}:\n"
    if hasattr(node, 'if_body') and node.if_body:
        for stmt in node.if_body:
            code += f"    {generate_code(stmt)}\n"
    if hasattr(node, 'else_body') and node.else_body:
        code += f"else:\n"
        if isinstance(node.else_body, Else):
            for stmt in node.else_body.body:
                code += f"    {generate_code(stmt)}\n"
    return code

def generate_else(node):
    code = "else:\n"
    if isinstance(node.body, list):
        for stmt in node.body:
            code += f"    {generate_code(stmt)}\n"
    else:
        code += f"    {generate_code(node.body)}\n"
    return code

def generate_while(node):
    condition = generate_code(node.condition)
    body = [generate_code(stmt) for stmt in node.body]
    code = f"while {condition}:\n"
    for stmt in body:
        code += f"    {stmt}\n"
    return code

def generate_for(node):
    identifier = generate_code(node.var)
    iterable = generate_code(node.iterable)
    body = [generate_code(stmt) for stmt in node.body]
    code = f"for {identifier} in {iterable}:\n"
    for stmt in body:
        code += f"    {stmt}\n"
    return code

def generate_list(node):
    elements = [generate_code(element) for element in node.elements]
    return f"[{', '.join(elements)}]"

def indent_statements(statements):
    indented_statements = []
    for stmt in statements:
        indented_statements.append(f"    {stmt}")
    return "\n".join(indented_statements)
