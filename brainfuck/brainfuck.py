from brainfuck import Parser, Interpreter
import logging

class Brainfuck:
    def __init__(self):
        self.parser = Parser()
        self.interpreter = Interpreter()

    def run(self, code: str):

        parsed = self.parser.parse(code)
        interpreted = self.interpreter.interpret(parsed)

        logging.info("Interpreted: %s (%d chars)" % (interpreted, len(interpreted)))
        logging.info("RAM: %s" % str(self.interpreter.ram))
        logging.info("Stack: %s" % ' '.join(self.interpreter.stack))
        logging.info("Program counter: %d" % self.interpreter.pc)