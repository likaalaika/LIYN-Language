import liyn_lexer
import liyn_parser
import liyn_interpreter

if __name__ == '__main__':
	lexer = liyn_lexer.BasicLexer()
	parser = liyn_parser.BasicParser()
	env = {}
	while True :
		try :
			text = input('liyn > ')
			 except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            liyn_interpreter.BasicExecute(tree, env)