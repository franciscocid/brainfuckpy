from unittest import TestCase
from brainfuck import Interpreter

class TestInterpreter(TestCase):

    def setUp(self):
        self.interpreter = Interpreter()

    def test_interpreter_resets_all_properties(self):
        self.interpreter.reset()
        
        self.assertEqual(self.interpreter.ram.data, [0] * 1024)
        self.assertEqual(self.interpreter.stdout, '')
        self.assertEqual(self.interpreter.input_ptr, 0)
        self.assertEqual(self.interpreter.pc, 0)
        self.assertEqual(self.interpreter.stack, [])