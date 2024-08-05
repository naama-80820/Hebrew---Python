from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For, List


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table=[]

    def add_symbol(self, name, value, type, line_number):
        self.symbol_table.append({
            'name': name,
            'value': value,
            'type': type,
            'line_number': line_number
        })

    def get_symbol(self, name):
        for symbol in self.symbol_table:
            if symbol['name'] == name:
                return symbol
        return None

    def update_symbol_line(self, name, line_number):
        for symbol in self.symbol_table:
            if symbol['name'] == name:
                symbol['line_number']=line_number
                return True
        return False

    def display_symbol_table(self):
        print("Symbol Table:")
        for symbol in self.symbol_table:
            print(
                f"Name: {symbol['name']}, Value: {symbol['value']}, Type: {symbol['type']}, Line Number: {symbol['line_number']}")

    def visit(self, node):
        if isinstance(node, str) and node.strip() == '':
            return  # Ignore newlines and empty strings

        method_name=f'visit_{type(node).__name__}'
        if hasattr(self, method_name):
            visitor=getattr(self, method_name)
            return visitor(node)
        else:
            return self.generic_visit(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Num(self, node):
        return "Num"

    def visit_Str(self, node):
        return "Str"

    def visit_VarAssign(self, node):
        var_name=node.name
        value_type=self.visit(node.value)  # Visit the assigned value to determine its type
        line_number=node.line_number if hasattr(node, 'line_number') else None

        if self.get_symbol(var_name) is None:
            self.add_symbol(var_name, None, value_type, line_number)
        else:
            self.update_symbol_line(var_name, line_number)

    def visit_Var(self, node):
        var_name=node.name
        symbol=self.get_symbol(var_name)
        if symbol is None:
            raise Exception(f'Variable "{var_name}" used without prior definition.')
        return symbol['type']

    def visit_BinOp(self, node):
        left=self.visit(node.left)
        right=self.visit(node.right)
        if left == right:
            return left
        else:
            raise Exception(f"BinOp operands must be of the same type, got {left} and {right}")

    def visit_Print(self, node):
        value_type=self.visit(node.value)
        return "Print"

    def visit_If(self, node):
        condition_type=self.visit(node.condition)
        if condition_type != "Bool":
            raise Exception(f"If condition must be of type Bool, got {condition_type}")
        for stmt in node.then_body:
            self.visit(stmt)
        if node.else_body:
            for stmt in node.else_body:
                self.visit(stmt)
        return None

    def visit_Else(self, node):
        else_body=[self.visit(statement) for statement in node.body]
        return self.indent_statements(else_body)  # Return indented statements or empty string if no statements

    def visit_For(self, node):
        # Add the loop variable to the symbol table
        loop_var_name=node.var.name
        line_number=node.line_number if hasattr(node, 'line_number') else None
        self.add_symbol(loop_var_name, None, "Num", line_number)

        iterable_type=self.visit(node.iterable)
        if iterable_type != "Num" and iterable_type != "List":
            raise Exception(f"For loop iterable must be of type Num or List, got {iterable_type}")

        for stmt in node.body:
            self.visit(stmt)
        return None

    def visit_While(self, node):
        condition_type=self.visit(node.condition)

        if isinstance(node.condition, BinOp):
            if node.condition.op in ['>', '<', '>=', '<=', '==', '!=', 'and', 'or', 'not']:
                condition_type="Bool"

        if condition_type not in ["Bool"]:
            raise Exception(f"While condition must be of type Bool, got {condition_type}")

        for stmt in node.body:
            self.visit(stmt)
        return None

    def visit_List(self, node):
        element_types=set(self.visit(element) for element in node.elements)
        if len(element_types) > 1:
            raise Exception(f"List elements must be of the same type, got {element_types}")
        return "Num"

    def indent_statements(self, statements):
        indented='\n'.join(['\t' + stmt for stmt in statements if stmt is not None])
        return indented
