import ply.yacc as yacc
from Analizador_lexico import tokens
import Analizador_lexico
import sys

VERBOSE = 1
ERRORES = 0 

def p_program(p):
    """program : OPENPHP declaration_list CLOSEPHP"""
    pass


def p_declaration_list(p):
    """declaration_list : declaration_list  declaration
                        | declaration"""
    pass


def p_declaration(p):
    """declaration : var_declaration
                  | fun_declaration
                  | header_declaration """
    pass


def p_header_declaration(p):
    """header_declaration : INCLUDE QUOTES ID DOT PHP QUOTES SEMICOLON"""
    pass


def p_var_declaration_1(p):
    """var_declaration : var_declaration2 SEMICOLON"""
    pass


def p_var_declaration_2(p):
    """var_declaration2 : ID COMMA var_declaration2
                        | ID 
                        | ID LBRACKET NUMBER RBRACKET COMMA var_declaration2
                        | ID NUMBER 
                        | ID EQUAL ID COMMA var_declaration2
                        | ID EQUAL NUMBER
                        | ID EQUAL var_declaration2
                        | ID EQUAL AMPERSANT ID """
    pass

def p_fun_declaration(p):
    """fun_declaration : FUNCTION FUNCTION_NAME LPAREN params RPAREN fun_body"""
    pass


def p_params(p):
    """params : var_declaration2
              | empty"""
    pass


def p_fun_body(p):
    """fun_body : LBLOCK local_declarations statement_list RBLOCK"""
    pass


def p_local_declarations(p):
    """local_declarations : local_declarations var_declaration
                          | empty"""
    pass


def p_statement_list(p):
    """statement_list : statement_list statement
                      | empty"""
    pass


def p_statement(p):
    """statement : expression_statament
                | writing_statament
                | writing_print
                | selection_statament
                | iteration_statament
                | return_statament
    """
    pass


def p_statement_block(p):
    """statement_block : LBLOCK statement_list RBLOCK
                       | statement"""
    pass


def p_expression_statament(p):
    """expression_statament : expression SEMICOLON
                            | SEMICOLON"""
    pass


def p_writing_statament(p):
    """writing_statament : ECHO ID SEMICOLON
                         | ECHO STRING SEMICOLON
                         | ECHO NUMBER SEMICOLON"""
    pass

def p_writing_print(p):
    """writing_print : PRINT ID SEMICOLON
                         | PRINT STRING SEMICOLON
                         | PRINT NUMBER SEMICOLON"""
    pass

def p_selection_statament(p):
    """selection_statament : IF LPAREN expression RPAREN statement_block
                           | IF LPAREN expression RPAREN statement_block ELSE statement_block
                           | IF LPAREN expression RPAREN statement_block ELSEIF selection_statament
                           | SWITCH LPAREN ID RPAREN statement
                           | CASE NUMBER COLON statement BREAK SEMICOLON
                           | DEFAULT COLON statement BREAK SEMICOLON"""
    pass


def p_iteration_statament(p):
    """iteration_statament : WHILE LPAREN expression RPAREN statement_block
                            | FOREACH LPAREN var_declaration2 AS var_declaration2 RPAREN statement_block
                            | FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement_block
                           """
    pass


def p_return_statament(p):
    """return_statament : RETURN VAR SEMICOLON
                        | RETURN NUMBER SEMICOLON
                        | RETURN expression SEMICOLON
                        | RETURN FUNCTION_NAME LPAREN params RPAREN SEMICOLON"""
    pass


def p_expression(p):
    """expression : var EQUAL expression
                  | STRING
                  | NUMBER
                  | simple_expression
                  | var PLUSEQUAL expression
                  | expression AND expression
                  | expression OR expression
                  | expression XOR expression 
                  | expression MINUSEQUAL expression  """
    pass


def p_var(p):
    """var : ID
           | ID LBRACKET NUMBER RBRACKET
           | ID LBRACKET ID RBRACKET"""
    pass


def p_simple_expression(p):
    """simple_expression : additive_expression relop additive_expression
                         | additive_expression"""
    pass


def p_additive_expression(p):
    """additive_expression : additive_expression addop term
                           | term
                           | term MINUSMINUS
                           | term PLUSPLUS"""
    pass


def p_relop(p):
    """relop : LESS
            | LESSEQUAL
            | GREATER
            | GREATEREQUAL
            | DEQUAL
            | ISEQUAL
    """
    pass

def p_addop(p):
    """addop : PLUS
            | MINUS
    """
    pass


def p_mulop(p):
    """mulop : TIMES
            | DIVIDE"""
    pass


def p_term(p):
    """term : term mulop factor
            | factor"""
    pass


def p_factor(p):
    """factor : LPAREN expression RPAREN
              | var
              | NUMBER"""
    pass

def p_empty(p):
    """empty :"""
    pass


def p_error(p):
    ERRORES = 1
    if VERBOSE:
        if p is not None:
            print("Error sintatico en la linea " + str(p.lexer.lineno) + " no se esperaba el Token  " + str(p.value))
        else:
            print("Error sintatico en la linea: " + str(Analizador_lexico.lexer.lineno))
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()


if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'prueba.php'

    f = open(file, 'r')
    data = f.read()
    parser.parse(data, tracking=True)
    if ERRORES == 0:
        print("Todo se reconocio correctamente")
    else:
        print("ALGO NO ESTA BIEN!!!")
    
    

