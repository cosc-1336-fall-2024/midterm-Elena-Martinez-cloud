#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import test_config, reverse_string

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_reverse_string(self):
        self.assertEquals (reverse_string("hello world"), "dlrow olleh")
        self.assertEquals (reverse_string("hello"), "olleh")