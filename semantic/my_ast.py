class Num:
    def __init__(self, value):
        self.type = 'Num'
        self.value = value

class Str:
    def __init__(self, value):
        self.type = 'Str'
        self.value = value

class Var:
    def __init__(self, name):
        self.type = 'Var'
        self.name = name

class VarAssign:
    def __init__(self, name, value):
        self.type = 'VarAssign'
        self.name = name
        self.value = value

class BinOp:
    def __init__(self, left, op, right):
        self.type = 'BinOp'
        self.left = left
        self.op = op
        self.right = right

class Print:
    def __init__(self, value):
        self.type = 'Print'
        self.value = value

class If:
    def __init__(self, condition, if_body, else_body=None):
        self.type = 'If'
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

class Else:
    def __init__(self, body):
        self.type = 'Else'
        self.body = body

class While:
    def __init__(self, condition, body):
        self.type = 'While'
        self.condition = condition
        self.body = body

class For:
    def __init__(self, var, iterable, body):
        self.type = 'For'
        self.var = var
        self.iterable = iterable
        self.body = body

class List:
    def __init__(self, elements):
        self.type = 'List'
        self.elements = elements



def print_tree(node, indent=0):
    if isinstance(node, list):
        for item in node:
            print_tree(item, indent)
    else:
        prefix = '  ' * indent
        if isinstance(node, Num):
            print(prefix + f'Num: {node.value}')
        elif isinstance(node, Str):
            print(prefix + f'Str: {node.value}')
        elif isinstance(node, Var):
            print(prefix + f'Var: {node.name}')
        elif isinstance(node, VarAssign):
            print(prefix + f'VarAssign: {node.name}')
            print_tree(node.value, indent + 1)
        elif isinstance(node, BinOp):
            print(prefix + f'BinOp: {node.op}')
            print_tree(node.left, indent + 1)
            print_tree(node.right, indent + 1)
        elif isinstance(node, Print):
            print(prefix + f'Print:')
            print_tree(node.value, indent + 1)
        elif isinstance(node, If):
            print(prefix + 'If:')
            print(prefix + '  Condition:')
            print_tree(node.condition, indent + 1)
            print(prefix + '  If Body:')
            print_tree(node.if_body, indent + 1)
            if node.else_body:
                print(prefix + '  Else Body:')
                print_tree(node.else_body, indent + 1)
        elif isinstance(node, Else):
            print(prefix + 'Else:')
            print_tree(node.body, indent + 1)
        elif isinstance(node, While):
            print(prefix + 'While:')
            print(prefix + '  Condition:')
            print_tree(node.condition, indent + 1)
            print(prefix + '  Body:')
            print_tree(node.body, indent + 1)
        elif isinstance(node, For):
            print(prefix + 'For:')
            print(prefix + '  Variable:')
            print_tree(node.var, indent + 1)
            print(prefix + '  Iterable:')
            print_tree(node.iterable, indent + 1)
            print(prefix + '  Body:')
            print_tree(node.body, indent + 1)
        elif isinstance(node, List):
            print(prefix + 'List:')
            for element in node.elements:
                print_tree(element, indent + 1)
