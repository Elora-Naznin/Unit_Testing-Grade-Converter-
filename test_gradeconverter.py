
import unittest
from gradeconverter import convert_to_letter_grade

class TestGradeConverter(unittest.TestCase):

    def test_grade_A(self):
        result = convert_to_letter_grade(95)
        self.assertEqual(result, "A")

    def test_grade_B(self):
        result = convert_to_letter_grade(85)
        self.assertEqual(result, "B")

    def test_grade_C(self):
        result = convert_to_letter_grade(75)
        self.assertEqual(result, "C")

    def test_grade_D(self):
        result = convert_to_letter_grade(65)
        self.assertEqual(result, "D")

    def test_grade_F(self):
        result = convert_to_letter_grade(55)
        self.assertEqual(result, "F")

    def test_invalid_grade(self):
        with self.assertRaises(ValueError):
            convert_to_letter_grade("not a number")

if __name__ == '__main__':
    unittest.main()
