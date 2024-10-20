#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import test_config, get_assessment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_question_d_config(self):
        self.assertEqual(True, test_config())

    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)
    
    def test_get_tax_assessed(self):
        self.assertEqual(get_tax_assessed(6000), 43.20)
        self.assertEqual(get_tax_assessed(10000), 72)
        