import liyn_lexer
import liyn_parser
import liyn_interpreter


lexer = liyn_lexer.BasicLexer()
parser = liyn_parser.BasicParser()
env = {}

file = open('test.liyn')
text = file.readlines()

for line in text :
	tree = parser.parse(lexer.tokenize(text))
    liyn_interpreter.BasicExecute(tree, env)