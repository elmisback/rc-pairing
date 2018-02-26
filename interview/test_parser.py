import lisp_parser

def test_ast():
    return (lisp_parser.AST("(first (list 1 (+ 2 3) 9))")
            == ['first', ['list', 1, ['+', 2, 3], 9]])
