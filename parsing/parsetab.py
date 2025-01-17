
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightEQUALleftPLUSMINUSSTARSLASHleftGREATERLESSEQUAL_EQUALNOT_EQUALGREATER_EQUALLESS_EQUALCOLON COMMA COMMENT ELSE EQUAL EQUAL_EQUAL FLOAT FOR GREATER GREATER_EQUAL IF IN LEFT_BRACKET LEFT_PAREN LESS LESS_EQUAL MINUS NEWLINE NOT_EQUAL NUMBER PLUS PRINT RIGHT_BRACKET RIGHT_PAREN SLASH STAR STRING VARIABLE WHILE\n    statements : statement\n               | statements statement\n    \n    statement : assignment\n              | print_statement\n              | if_statement\n              | while_statement\n              | for_statement\n              | NEWLINE\n    \n    while_statement : WHILE expression COLON statements\n    \n    for_statement : FOR VARIABLE IN expression COLON statements\n    \n    print_statement : PRINT LEFT_PAREN expression RIGHT_PAREN\n    \n    assignment : VARIABLE EQUAL expression\n               | VARIABLE EQUAL STRING\n               | VARIABLE EQUAL NUMBER\n               | VARIABLE EQUAL VARIABLE\n    \n    expression : term\n               | expression PLUS term\n               | expression MINUS term\n               | expression STAR term\n               | expression SLASH term\n               | expression GREATER term\n               | expression LESS term\n               | expression EQUAL_EQUAL term\n               | expression NOT_EQUAL term\n               | expression GREATER_EQUAL term\n               | expression LESS_EQUAL term\n    \n    term : NUMBER\n         | STRING\n         | VARIABLE\n         | FLOAT\n         | list\n    \n    list : LEFT_BRACKET elements RIGHT_BRACKET\n    \n    elements : expression\n             | elements COMMA expression\n    \n    if_statement : IF expression COLON statements else_statement\n    \n    else_statement :\n                  | ELSE COLON statements\n    \n    variable_assignment : VARIABLE EQUAL expression\n    '
    
_lr_action_items = {'NEWLINE':([0,1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,32,45,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,66,67,68,69,],[8,8,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,8,8,-11,8,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,8,-35,8,8,8,8,]),'VARIABLE':([0,1,2,3,4,5,6,7,8,11,12,13,14,15,16,18,19,20,21,22,23,24,27,28,29,30,32,33,34,35,36,37,38,39,40,41,42,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,66,67,68,69,],[9,9,-1,-3,-4,-5,-6,-7,-8,21,21,26,-2,27,21,-16,-27,-28,-29,-30,-31,21,-15,-12,-13,-14,9,21,21,21,21,21,21,21,21,21,21,9,21,-11,9,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,21,9,-35,9,9,9,9,]),'PRINT':([0,1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,32,45,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,66,67,68,69,],[10,10,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,10,10,-11,10,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,10,-35,10,10,10,10,]),'IF':([0,1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,32,45,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,66,67,68,69,],[11,11,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,11,11,-11,11,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,11,-35,11,11,11,11,]),'WHILE':([0,1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,32,45,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,66,67,68,69,],[12,12,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,12,12,-11,12,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,12,-35,12,12,12,12,]),'FOR':([0,1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,32,45,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,66,67,68,69,],[13,13,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,13,13,-11,13,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,13,-35,13,13,13,13,]),'$end':([1,2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,68,69,],[0,-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,-11,-36,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,-9,-35,-10,-37,]),'ELSE':([2,3,4,5,6,7,8,14,18,19,20,21,22,23,27,28,29,30,47,48,49,50,51,52,53,54,55,56,57,58,59,61,63,68,69,],[-1,-3,-4,-5,-6,-7,-8,-2,-16,-27,-28,-29,-30,-31,-15,-12,-13,-14,-11,64,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,-9,-35,-10,-37,]),'EQUAL':([9,],[15,]),'LEFT_PAREN':([10,],[16,]),'NUMBER':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[19,19,30,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'STRING':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[20,20,29,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'FLOAT':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'LEFT_BRACKET':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'COLON':([17,18,19,20,21,22,23,25,49,50,51,52,53,54,55,56,57,58,59,62,64,],[32,-16,-27,-28,-29,-30,-31,45,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,66,67,]),'PLUS':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[33,-16,-27,-28,-29,-30,-31,33,-29,33,-28,-27,33,33,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,33,33,]),'MINUS':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[34,-16,-27,-28,-29,-30,-31,34,-29,34,-28,-27,34,34,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,34,34,]),'STAR':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[35,-16,-27,-28,-29,-30,-31,35,-29,35,-28,-27,35,35,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,35,35,]),'SLASH':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[36,-16,-27,-28,-29,-30,-31,36,-29,36,-28,-27,36,36,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,36,36,]),'GREATER':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[37,-16,-27,-28,-29,-30,-31,37,-29,37,-28,-27,37,37,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,37,37,]),'LESS':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[38,-16,-27,-28,-29,-30,-31,38,-29,38,-28,-27,38,38,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,38,38,]),'EQUAL_EQUAL':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[39,-16,-27,-28,-29,-30,-31,39,-29,39,-28,-27,39,39,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,39,39,]),'NOT_EQUAL':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[40,-16,-27,-28,-29,-30,-31,40,-29,40,-28,-27,40,40,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,40,40,]),'GREATER_EQUAL':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[41,-16,-27,-28,-29,-30,-31,41,-29,41,-28,-27,41,41,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,41,41,]),'LESS_EQUAL':([17,18,19,20,21,22,23,25,27,28,29,30,31,44,49,50,51,52,53,54,55,56,57,58,59,62,65,],[42,-16,-27,-28,-29,-30,-31,42,-29,42,-28,-27,42,42,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,42,42,]),'RIGHT_PAREN':([18,19,20,21,22,23,31,49,50,51,52,53,54,55,56,57,58,59,],[-16,-27,-28,-29,-30,-31,47,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,]),'RIGHT_BRACKET':([18,19,20,21,22,23,43,44,49,50,51,52,53,54,55,56,57,58,59,65,],[-16,-27,-28,-29,-30,-31,59,-33,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,-34,]),'COMMA':([18,19,20,21,22,23,43,44,49,50,51,52,53,54,55,56,57,58,59,65,],[-16,-27,-28,-29,-30,-31,60,-33,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-32,-34,]),'IN':([26,],[46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,32,45,66,67,],[1,48,61,68,69,]),'statement':([0,1,32,45,48,61,66,67,68,69,],[2,14,2,2,14,14,2,2,14,14,]),'assignment':([0,1,32,45,48,61,66,67,68,69,],[3,3,3,3,3,3,3,3,3,3,]),'print_statement':([0,1,32,45,48,61,66,67,68,69,],[4,4,4,4,4,4,4,4,4,4,]),'if_statement':([0,1,32,45,48,61,66,67,68,69,],[5,5,5,5,5,5,5,5,5,5,]),'while_statement':([0,1,32,45,48,61,66,67,68,69,],[6,6,6,6,6,6,6,6,6,6,]),'for_statement':([0,1,32,45,48,61,66,67,68,69,],[7,7,7,7,7,7,7,7,7,7,]),'expression':([11,12,15,16,24,46,60,],[17,25,28,31,44,62,65,]),'term':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[18,18,18,18,18,49,50,51,52,53,54,55,56,57,58,18,18,]),'list':([11,12,15,16,24,33,34,35,36,37,38,39,40,41,42,46,60,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'elements':([24,],[43,]),'else_statement':([48,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement','statements',1,'p_statements','parser.py',16),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',17),
  ('statement -> assignment','statement',1,'p_statement','parser.py',27),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',28),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',29),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',30),
  ('statement -> for_statement','statement',1,'p_statement','parser.py',31),
  ('statement -> NEWLINE','statement',1,'p_statement','parser.py',32),
  ('while_statement -> WHILE expression COLON statements','while_statement',4,'p_while_statement','parser.py',38),
  ('for_statement -> FOR VARIABLE IN expression COLON statements','for_statement',6,'p_for_statement','parser.py',44),
  ('print_statement -> PRINT LEFT_PAREN expression RIGHT_PAREN','print_statement',4,'p_print_statement','parser.py',50),
  ('assignment -> VARIABLE EQUAL expression','assignment',3,'p_assignment','parser.py',56),
  ('assignment -> VARIABLE EQUAL STRING','assignment',3,'p_assignment','parser.py',57),
  ('assignment -> VARIABLE EQUAL NUMBER','assignment',3,'p_assignment','parser.py',58),
  ('assignment -> VARIABLE EQUAL VARIABLE','assignment',3,'p_assignment','parser.py',59),
  ('expression -> term','expression',1,'p_expression','parser.py',72),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser.py',73),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser.py',74),
  ('expression -> expression STAR term','expression',3,'p_expression','parser.py',75),
  ('expression -> expression SLASH term','expression',3,'p_expression','parser.py',76),
  ('expression -> expression GREATER term','expression',3,'p_expression','parser.py',77),
  ('expression -> expression LESS term','expression',3,'p_expression','parser.py',78),
  ('expression -> expression EQUAL_EQUAL term','expression',3,'p_expression','parser.py',79),
  ('expression -> expression NOT_EQUAL term','expression',3,'p_expression','parser.py',80),
  ('expression -> expression GREATER_EQUAL term','expression',3,'p_expression','parser.py',81),
  ('expression -> expression LESS_EQUAL term','expression',3,'p_expression','parser.py',82),
  ('term -> NUMBER','term',1,'p_term','parser.py',91),
  ('term -> STRING','term',1,'p_term','parser.py',92),
  ('term -> VARIABLE','term',1,'p_term','parser.py',93),
  ('term -> FLOAT','term',1,'p_term','parser.py',94),
  ('term -> list','term',1,'p_term','parser.py',95),
  ('list -> LEFT_BRACKET elements RIGHT_BRACKET','list',3,'p_list','parser.py',110),
  ('elements -> expression','elements',1,'p_elements','parser.py',116),
  ('elements -> elements COMMA expression','elements',3,'p_elements','parser.py',117),
  ('if_statement -> IF expression COLON statements else_statement','if_statement',5,'p_if_statement','parser.py',126),
  ('else_statement -> <empty>','else_statement',0,'p_else_statement','parser.py',132),
  ('else_statement -> ELSE COLON statements','else_statement',3,'p_else_statement','parser.py',133),
  ('variable_assignment -> VARIABLE EQUAL expression','variable_assignment',3,'p_variable_assignment','parser.py',148),
]
