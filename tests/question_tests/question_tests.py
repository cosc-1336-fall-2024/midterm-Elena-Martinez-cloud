#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_c.question_c import test_config, get_bonus_pay_amount

class Test_Config(unittest.TestCase):

    def test_question_c_config(self):
        self.assertEqual(True, test_config())

    def test_get_bonus_pay_amount(self):
        test_case = {
            -1: 'Invalid arguments',
            2000: 10,
            600: 36,
            1000: 70,
            1500: 120,
            2000: 'Invalid arguments'
        }
        for sales, expected in test_case.items():
            result = get_bonus_pay_amount(sales)
            self.assertEqual(result, expected)