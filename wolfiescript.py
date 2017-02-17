#------------------------------------------------------------
# NAME: Salvatore Termine
# SBUID: 109528463
#------------------------------------------------------------


import ply.lex as lex
import ply.yacc as yacc
import sys

#------------------------------------------------------------
# Classes
#------------------------------------------------------------

class integer:
	def __init__(self, value):
		self.value = value
	def evaluate(self):
		return self.value

class real:
	def __init__(self, value):
		self.value = value
	def evaluate(self):
		return self.value

class String:
	def __init__(self, value):
		self.value = value
	def evaluate(self):
		return self.value

class List:
	def __init__(self, value):
		self.value = value
	def evaluate(self):
		return self.value

class Name:
	def __init__(self, value):
		self.value = value
	def evaluate(self):
		return dictionary[self.value]

class Assignment:
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def evaluate(self):
		left = self.left
		right = self.right.evaluate()
		dictionary[left] = right

class Stmt:
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def evaluate(self):
		self.left.evaluate()
		if(self.right != None):
			self.right.evaluate()

class Print:
	def __init__(self, left):
		self.left = left
	def evaluate(self):
		left = self.left.evaluate()
		print(left)

class While:
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def evaluate(self):
		while(self.left.evaluate() == 1):
			self.right.evaluate()

class If:
	def __init__(self,left,right):
		self.left = left
		self.right = right
		self.e = None
	def evaluate(self):
		if(self.left.evaluate() == 1):
			self.right.evaluate()
		elif(self.e != None):
			self.e.evaluate()

class Else:
	def __init__(self, left):
		self.left = left
	def evaluate(self):
		self.left.evaluate()

class Bin_op:
	def __init__(self, left, right, op):
		self.left = left
		self.right = right
		self.op = op

	def evaluate(self):
		op = self.op
		left = self.left.evaluate()
		right = self.right.evaluate()
		if op == '+':
			if isinstance(left, int) & isinstance(right, int):
				return left + right
			elif isinstance(left, str) & isinstance(right, str):
				return left + right
			elif isinstance(left, float) & isinstance(right, float):
				return left + right
			elif isinstance(left, list) & isinstance(right, list):
				return left + right
		elif op == '-':
			if isinstance(left, int) & isinstance(right, int):
				return left - right
			elif isinstance(left, float) & isinstance(right, float):
				return left - right
		elif op == '**':
			if isinstance(left, int) & isinstance(right, int):
				return left ** right
			elif isinstance(right, float) & isinstance(left, float):
				return left ** right
		elif op == '*':
			if isinstance(left, int) & isinstance(right, int):
				return left * right
			elif isinstance(right, float) & isinstance(left, float):
				return left * right
		elif op == '//':
			if isinstance(left, int) & isinstance(right, int):
				return left // right
			elif isinstance(right, float) & isinstance(left, float):
				return left // right
		elif op == '/':
			if isinstance(left, int) & isinstance(right, int):
				return left / right
			elif isinstance(right, float) & isinstance(left, float):
				return left / right
		elif op == '%':
			if isinstance(left, int) & isinstance(right, int):
				return left % right
			elif isinstance(right, float) & isinstance(left, float):
				return left % right
		else:
			raise Semantic_Error()

class ListIndex_op:
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def evaluate(self):
		left = self.left.evaluate()
		right = self.right.evaluate()
		if isinstance(left, str) & isinstance(right, int):
			return left[right]
		elif isinstance(left, list) & isinstance(right, int):
			return left[right]
		else: raise Semantic_Error()

class Semantic_Error(Exception):
	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)

class Boolean_op:
	def __init__(self, left, right, op):
		self.left = left
		self.right = right
		self.op = op
	def evaluate(self):
		left = self.left.evaluate()
		right = self.right.evaluate()
		op = self.op
		if op == 'and':
			if isinstance(left, int) & isinstance(right, int):
				if left and right:
					return 1
				else:
					return 0
		elif op == 'or':
			if isinstance(left, int) & isinstance(right, int):
				if left or right:
					return 1
				else:
					return 0
		elif op == 'not':
			if isinstance(right, int):
				if not right:
					return 1
				else:
					return 0
		elif op == 'in':
			if isinstance(left, int) & isinstance(right, int):
				if left in right:
					return 1
				else:
					return 0
		else:
			raise Semantic_Error()

class Comparison_op:
	def __init__(self, left, right, op):
		self.op = op
		self.left = left
		self.right = right
	def evaluate(self):
		left = self.left.evaluate()
		right = self.right.evaluate()
		op = self.op
		if op == '>=':
			if isinstance(left, int) & isinstance(right, int):
				if left >= right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left >= right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left >= right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left >= right:
					return 1
				else:
					return 0
		elif op == '>':
			if isinstance(left, int) & isinstance(right, int):
				if left > right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left > right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left > right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left > right:
					return 1
				else:
					return 0
		elif op == '<=':
			if isinstance(left, int) & isinstance(right, int):
				if left <= right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left <= right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left <= right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left <= right:
					return 1
				else:
					return 0
		elif op == '<':
			if isinstance(left, int) & isinstance(right, int):
				if left < right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left < right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left < right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left < right:
					return 1
				else:
					return 0
		elif op == '==':
			if isinstance(left, int) & isinstance(right, int):
				if left == right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left == right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left == right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left == right:
					return 1
				else:
					return 0
		elif op == '!=':
			if isinstance(left, int) & isinstance(right, int):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left != right:
					return 1
				else:
					return 0
		elif op == '<>':
			if isinstance(left, int) & isinstance(right, int):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, float):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, int) & isinstance(right, float):
				if left != right:
					return 1
				else:
					return 0
			elif isinstance(left, float) & isinstance(right, int):
				if left != right:
					return 1
				else:
					return 0
		else:
			print("Semantic Error")

#------------------------------------------------------------
# LEXER
#------------------------------------------------------------

tokens = (
	'REAL',
	'INTEGER',
	'STRING',
	'PLUS',
	'MINUS',
	'POWER',
	'MULTIPLY',
	'FLOOR',
	'DIVISION',
	'MOD',
	'LPAREN',
	'RPAREN',
	'LCURL',
	'RCURL',
	'GR_EQ',
    'LE_EQ',
	'GREATER',
	'LESS',
    'EQUALS',
    'NOT_EQ',
    'NEQ',
    'LSQR', 
    'RSQR',
    'COMMA',
    'AND',
    'OR',
    'NOT',
    'IN',
    'IF',
    'ELSE',
    'WHILE',
    'NAME',
    'ASSIGN',
    'SEMICOLON',
    'PRINT'
	)

dictionary = {}

# TOKENS DEFINED
t_PLUS = r'\+'
t_MINUS = r'-'
t_POWER = r'\*\*'
t_MULTIPLY = r'\*'
t_FLOOR = r'//'
t_DIVISION = r'/'
t_MOD = r'\%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_GR_EQ   = r'\>\='
t_LE_EQ   = r'\<\='
t_GREATER = r'\>'
t_LESS    = r'\<'
t_EQUALS  = r'\=\='
t_NOT_EQ  = r'\!\='
t_NEQ     = r'\<\>'
t_LSQR    = r'\['
t_RSQR    = r'\]'
t_COMMA   = r','
t_NOT     = r'not'
t_OR      = r'or'
t_AND     = r'and'
t_IN  	  = r'in'
t_IF      = r'if'
t_ELSE    = r'else'
t_WHILE   = r'while'
t_NAME    = r'(?! in|not|and|or|if|else|while|print|for)([A-Za-z][A-Za-z0-9_]*)'
t_ASSIGN  = r'='
t_SEMICOLON = r';'
t_PRINT   = r'print'
t_LCURL   = r'\{'
t_RCURL   = r'\}'

# DEFINE WHAT A REAL NUMBER IS
def t_REAL(t):
	r'[0-9]+\.[0-9]* | [0-9]*\.[0-9]+'
	t.value = float(t.value)
	return t

# DEFINE WHAT AN INTEGER IS
def t_INTEGER(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t

# DEFINE WHAT A STRING IS
def t_STRING(t):
	r'"[^"]*"'
	t.value = t.value[1:-1]
	return t

t_ignore  = ' \t'

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("SYNTAX ERROR")
	t.lexer.skip(1)

lex.lex()


#------------------------------------------------------------
# Parser
#------------------------------------------------------------

precedence = (
	('left','PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'FLOOR', 'DIVISION', 'MOD', 'GR_EQ', 'GREATER', 'LE_EQ', 'LESS', 'EQUALS', 'NOT_EQ','NEQ'),
	('right', 'POWER'),
	('right', 'ASSIGN')
	)	


def p_stmt_block(t):
	'block : LCURL stmts RCURL'
	t[0] = t[2]

def p_stmt_stmts(t):
	'stmts : stmt'
	t[0] = Stmt(t[1], None)

def p_stmt_stmts_stmts(t):
	'stmts : stmt stmts'
	t[0] = Stmt(t[1],t[2])

def p_stmt_assignment(t):
	'''stmt : NAME ASSIGN expression SEMICOLON
			| NAME ASSIGN list SEMICOLON
			| NAME ASSIGN listindex SEMICOLON
			| NAME ASSIGN listindex expression SEMICOLON'''
	t[0] = Assignment(t[1], t[3])

def p_stmt_print(t):
	'stmt : PRINT LPAREN expression RPAREN SEMICOLON'
	t[0] = Print(t[3])

def p_stmt_while(t):
	'stmt : WHILE LPAREN expression RPAREN block'
	t[0] = While(t[3], t[5])

def p_stmt_if(t):
	'ifstmt : IF LPAREN expression RPAREN block'
	t[0] = If(t[3],t[5])

def p_stmt_ifm(t):
	'stmt : ifstmt'
	t[0] = t[1]

def p_stmt_ifelse(t):
	'ifelse : ifstmt ELSE block'
	t[1].e = Else(t[3])
	t[0] = t[1]

def p_stmt_ifelsem(t):
	'stmt : ifelse'
	t[0] = t[1]

def p_stmt_else(t):
	'stmt : ELSE block'
	t[0] = Else(t[2])

def p_expression_group(t):
	'expression : LPAREN expression RPAREN'
	t[0] = t[2]

def p_expression_bin_op(t):
	'''expression : expression PLUS expression
				  | expression MINUS expression
				  | expression POWER expression
				  | expression MULTIPLY expression
				  | expression FLOOR expression
				  | expression DIVISION expression
				  | expression MOD expression'''
	t[0] = Bin_op(t[1],t[3], t[2])

def p_expression_comparison(t):
	'''expression : expression GR_EQ expression
				| expression GREATER expression
				| expression LE_EQ expression
				| expression LESS expression
				| expression EQUALS expression
				| expression NOT_EQ expression
				| expression NEQ expression'''
	t[0] = Comparison_op(t[1],t[3],t[2])

def p_list(t):
	'list : LSQR commalist RSQR'
	t[0] = List(t[2])

def p_comma_list(t):
	'commalist : expression'
	t[0] = [t[1].evaluate()]

def p_comma_list_recursive(t):
	'commalist : commalist COMMA expression'
	t[0] = t[1] + [t[3].evaluate()]

def p_empty_list(t):
	'list : LSQR RSQR'
	t[0] = List([])

def p_expression_list(t):
	'expression : list'
	t[0] = t[1]

def p_list_index(t):
	'''listindex : list LSQR expression RSQR
				  | string LSQR expression RSQR
				  | expression LSQR expression RSQR'''
	t[0] = ListIndex_op(t[1],t[3])

def p_list_expression(t):
	'expression : listindex'
	t[0] = t[1]

def p_expression_boolean(t):
	'''expression : expression  OR expression
				| expression AND expression
				| expression IN expression'''
	t[0] = Boolean_op(t[1],t[3], t[2])

def p_expression_not(t):
	'expression : NOT expression'
	t[0] = Boolean_op(integer(1), t[2], t[1])

def p_real_number(t):
	'number : REAL'
	t[0] = real(t[1])

def p_int_number(t):
	'number : INTEGER'
	t[0] = integer(t[1])

def p_string_string(t):
	'string : STRING'
	t[0] = String(t[1])

def p_expresion_string(t):
	'expression : string'
	t[0] = t[1]

def p_expression_number(t):
	'expression : number'
	t[0] = t[1]

def p_expression_name(t):
	'expression : NAME'
	t[0] = Name(t[1])

def p_error(t):
	raise SyntaxError()

yacc.yacc()

#-----------------------------------------------------------
# Main
#-----------------------------------------------------------

argv = sys.argv

try:
	input_file = open(argv[1], "r")
	whole_file = input_file.read()
	yacc.parse(whole_file).evaluate()
	input_file.close()
except IOError:
	print("Error opening the file")
except SyntaxError:
	print("Syntax Error")












































