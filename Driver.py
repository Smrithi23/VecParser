import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
from VecLexer import VecLexer
from VecParser import VecParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VecLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VecParser(stream)
    tree = parser.parse()
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main(sys.argv)