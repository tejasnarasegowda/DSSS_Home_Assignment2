import unittest
from math_quiz import function_rand_integer, function_rand_math_oper, function_math_probsol


class TestMathGame(unittest.TestCase):

    def test_function_rand_integer(self):
        # Here we check if test random numbers generated are in the defined range
        min = 1
        max = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_rand_integer(min, max)
            self.assertTrue(min <= rand_num <= max)

    def test_function_rand_math_oper(self):
        # 500 random operations are generated and expected operations are validated.
       for _ in range(500):  
        operation = function_rand_math_oper()
        self.assertIn(operation, ['+', '-', '*'])

    def test_function_math_probsol(self): # List of test cases are seen for the solution comparison with input values (number1, number2, o, expected_problem, expected_answer)
            
            #  loop executes with the following test cases which calls the function with the input values, and checks if the output matches the expected values.
            test_cases = [
                            (5, 2, '+', '5 + 2', 7),
                            (13, 2, '+', '13 + 2', 15),
                            (0, 8, '+', '0 + 8', 8),
                            (2, 3, '*', '2 * 3', 6),
                            (7, 2, '-', '7 - 2', 5),
                            (9, 1, '*', '9 * 1', 9),
                            (8, 5, '+', '8 * 5', 13),
                            (6, 3, '-', '6 - 3', 3),
                            (5, 9, '*', '5 * 9', 45),
                            (5, 3, '+', '5 + 3', 8)
                          ]

            for number1, number2, o, expected_problem, expected_answer in test_cases:
                problem, answer = function_math_probsol(number1, number2, o)              #Here we call the function to get the problem and answer.
                self.assertEqual(problem, expected_problem)                     #Here we check if the problem generated with random numbers matches the expected problem.               
                self.assertEqual(answer, expected_answer)                       #Here we check if the problem generated with random numbers matches the expected answer.
                
            

if __name__ == "__main__":
    unittest.main()
