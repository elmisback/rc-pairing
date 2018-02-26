#!/usr/bin/env python
"""lisp-parser: parse Lisp expressions."""

def AST(string):
    """Returns an abstract syntax tree for a Lisp expression.

    Expects first and last characters of `string` to be parens.
    Valid atoms/values are symbols without spaces or non-negative integers.
    """
    assert(len(string) > 0)
    assert(string[0] == '(' and string[-1] == ')')

    # tokenize: pad parens with spaces, then split on spaces.
    #
    # This works because parens and spaces are the only token delimiters.
    tokens = (string.replace('(', ' ( ')
                   .replace(')', ' ) ')
                   .split())

    # Start the tree by stripping the outermost parens.
    tokens = tokens[1:-1]
    root = []

    # Keep track of root--it's going to change.
    stack = [root]

    # Then build the tree in depth-first order.
    for token in tokens:
        if token == '(':
            # Start a new subtree
            # (a child of root),
            # put root where we can come back to it,
            # and then call the child root.
            child = []
            root.append(child)
            stack.append(root)
            root = child
        elif token == ')':
            # Go back to the previous root.
            root = stack.pop()
        elif token.isdigit():
            root.append(int(token))
        else:
            root.append(token)

    # Finally, take the original root off the stack.
    return stack.pop()

if __name__ == "main":
    import sys
    if len(sys.argv) > 1:
        print(AST(sys.argv[1]))
    else:
        print("lisp-parser requires one argument, eg '(first (list 1 (+ 2 3) 9))'")
