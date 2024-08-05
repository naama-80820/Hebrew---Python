import ply.lex as lex

# Reserved words
reserved_words = {
    'הדפס': 'PRINT',
    'אם': 'IF',
    'אחרת': 'ELSE',
    'בעוד': 'WHILE',
    'עבור': 'FOR',
    'ב': 'IN',
}

tokens = [
    "LEFT_PAREN",
    "RIGHT_PAREN",
    "LEFT_BRACKET",
    "RIGHT_BRACKET",
    "COMMA",
    "MINUS",
    "PLUS",
    "SLASH",
    "STAR",
    "COLON",
    "EQUAL",
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',

    "NUMBER",
    "FLOAT",
    "STRING",
    "VARIABLE",
    "NEWLINE",
    "COMMENT",
] + list(reserved_words.values())

# Regular expression rules for simple tokens
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r','
t_MINUS = r'-'
t_PLUS = r'\+'
t_SLASH = r'/'
t_STAR = r'\*'
t_COLON = r':'
t_EQUAL = r'='
t_EQUAL_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

# Declare the state
states = (
  ('comment','exclusive'),
)

# Rules for reserved words
def t_RESERVED_WORDS(t):
    r'(הדפס|אם|אחרת|בעוד|עבור|ב)'
    t.type = reserved_words.get(t.value)
    return t

# Rule to new lines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

#הסדר חשוב
# Rules for float numbers
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Rules for integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Rules for strings - path & regular
def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value[1:-1]
    return t

# Rules for variables
def t_VARIABLE(t):
    r'[א-ת_]+[א-ת0-9_]*'
    t.type = 'VARIABLE'
    return t

# Rule to ignore spaces and tabs
t_ignore = ' \t'

# Rule to handle errors
def t_error(t):
    print(f"תו לא חוקי '{t.value[0]}' בשורה{t.lineno}")
    t.lexer.skip(1)


# Rule to enter comment state
def t_COMMENT(t):
    r'\#'
    t.lexer.begin('comment')

# Rule to handle comments
def t_comment_comment(t):
    r'.+'
    pass

# Rule to exit comment state on newline
def t_comment_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')

# Rule to ignore  in comment state
t_comment_ignore = ' \t'

# Rule to errors in comment state
def t_comment_error(t):
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Example usage
# data = '''
# !
# נעמה = 6
# הדפס "שלום"
# # זו תגובה
# אם 5 > 3:
#     הדפס  "זה נכון"
# '''
#
# lexer.input(data)
# for tok in lexer:
#     print(tok)
