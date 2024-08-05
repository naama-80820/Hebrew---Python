from semantic.my_ast import Num, BinOp, Print, Str, VarAssign, Var, If, Else, While, For, List
import sys
import ply.lex as lex
import ply.yacc as yacc
from lexing.lexer import lexer, tokens
from parsing.parser import parser
from semantic.semantic_analyzer import SemanticAnalyzer
from code_gen.code_generator import generate_code

def read_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            input_code = file.read()
            lexer.input(input_code)
          #  print("Reading input file completed.")

            # ניתוח סינטקטי
            result = parser.parse(input_code)
          #  print("Parsed AST:", result)

            # ניתוח סמנטי
            analyzer = SemanticAnalyzer()
            for stmt in result:
                analyzer.visit(stmt)
          #  print("Semantic analysis completed.")

            # יצירת קוד פייתון
            python_code = "\n".join(generate_code(stmt) for stmt in result if stmt is not None)
       #     print("Generated Python code:", python_code)

            # פלט לקובץ טקסט
            write_to_file(output_file, python_code)
           # print("Output written to", output_file)

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

def write_to_file(output_file, content):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("err")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
   # print("Input file:", input_file)
   # print("Output file:", output_file)
    read_file(input_file, output_file)
    #print("Script completed successfully.")
