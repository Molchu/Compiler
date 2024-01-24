import ply.lex as lex
import sys

# Tokens
tokens = (
    'EQUAL',
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'OR',
    'AND',
    'XOR',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'DEQUAL',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'QUOTES',
    'DOT',
    'PHP',
    'BREAK',
    'FUNCTION',
    'INCLUDE',
    'VAR',
    'PRINT',
    'WHILE',
    'CASE',
    'ECHO',
    'RETURN',
    'ELSE',
    'FOR',
    'IF',
    'DEFAULT',
    'ELSEIF',
    'SWITCH',
    'ID',
    'NUMBER',
    'FUNCTION_NAME',
    'STRING',
    'OPENPHP',
    'CLOSEPHP',
    'FOREACH',
    'AS'
)


t_EQUAL = r'\='
t_PLUS = r'\+'
t_PLUSPLUS = r'\++'
t_PLUSEQUAL = r'\+='
t_MINUS = r'-'
t_MINUSMINUS = r'--'
t_MINUSEQUAL = r'-='
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_OR = r'or'
t_AND = r'and'
t_XOR = r'xor'
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_DEQUAL = r'!='
t_ISEQUAL = r'=='
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_AMPERSANT = r'\&'
t_QUOTES = r'"'
t_DOT = r'\.'


def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_PHP(t):
    r"""php"""
    return t


def t_VAR(t):
    r"""var"""
    return t


def t_BREAK(t):
    r"""break"""
    return t



def t_FUNCTION(t):
    r"""function"""
    return t


def t_INCLUDE(t):
    r"""include"""
    return t


def t_PRINT(t):
    r"""print"""
    return t


def t_WHILE(t):
    r"""while"""
    return t


def t_CASE(t):
    r"""case"""
    return t


def t_ECHO(t):
    r"""echo"""
    return t

def t_RETURN(t):
    r"""return"""
    return t


def t_ELSE(t):
    r"""else"""
    return t

def t_AS(t):
    r"""as"""
    return t
    
def t_FOREACH(t):
    r"""foreach"""
    return t

def t_FOR(t):
    r"""for"""
    return t



def t_IF(t):
    r"""if"""
    return t

def t_DEFAULT(t):
    r"""default"""
    return t


def t_ELSEIF(t):
    r"""elseif"""
    return t

def t_SWITCH(t):
    r"""switch"""
    return t


def t_ID(t):
    r"""(\$)\w+(_\d\w)*"""
    return t


def t_FUNCTION_NAME(t):
    r"""\w+(_\d\w)*\("""
    t.value = t.value[:-1]
    lexer.lexpos -= 1
    return t


def t_STRING(t):
    r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\''
    return t

def t_NUMBER(t):
    r"""(\-)?\d(\.\d+)?"""
    t.value = float(t.value)
    return t


def t_OPENPHP(t):
    r"""<\?php"""
    return t


def t_CLOSEPHP(t):
    r"""\?>"""
    return t


def t_comments_oneline(t):
    r"""\#(.)*?\n"""
    t.lexer.lineno += 1


def t_comments_oneline2(t):
    r"""//(.)*?\n"""
    t.lexer.lineno += 1


def t_comments_multiline(t):
    r"""/\*(.|\n)*?\*/"""
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def analyze(codigoprueba, lexer):
    lexer.input(codigoprueba)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


lexer = lex.lex()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'prueba.php'
    f = open(file, 'r')
    codigoprueba = f.read()
    print(codigoprueba)
    lexer.input(codigoprueba)
    analyze(codigoprueba, lexer)
