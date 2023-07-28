# Unit_Testing-Grade-Converter-
 Let's create a fun and unique example for a unit test that will appeal to anyone. How about testing a function that converts a numeric grade into a letter grade, like the ones we get in school? We'll use PyCharm to run the tests.

Step 1: Create the Function to Test
Let's write a function called convert_to_letter_grade() that takes a numeric grade as input and returns the corresponding letter grade:

python
Copy code
# File: grade_converter.py

def convert_to_letter_grade(grade):
    if not isinstance(grade, (int, float)):
        raise ValueError("Grade must be a number.")
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
Step 2: Set Up the Unit Test File
Now, let's create a new Python file to write our unit tests. Create a file called test_grade_converter.py in the same directory as the grade_converter.py file.

Step 3: Write the Test Cases
In the test_grade_converter.py file, we'll write test cases to check if the convert_to_letter_grade() function works correctly for different grade inputs:

python
Copy code
# File: test_grade_converter.py

import unittest
from grade_converter import convert_to_letter_grade

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
Step 4: Run the Tests in PyCharm
Open the project in PyCharm, and make sure both grade_converter.py and test_grade_converter.py are visible in the Project Explorer.

To run the unit tests, right-click on test_grade_converter.py in the Project Explorer and select "Run 'test_grade_converter'". PyCharm will execute the tests and show the results in the "Run" tool window.

Step 5: Analyze Test Results
The output will show whether the tests passed or failed. In this example, all the tests should pass, and you'll see a fun display of different letter grades for various numeric inputs.

Step 6: Debugging Tests (Optional)
If any test fails and you need to investigate why, you can use PyCharm's debugging capabilities. Place breakpoints in the test or function, then right-click and choose "Debug 'test_case_name'" to start debugging. You can inspect variables, step through the code, and find the cause of the issue.

That's it! You have now set up and run unit tests for a fun and appealing example using PyCharm. Unit testing is a powerful technique to ensure your code works correctly and meets the desired behavior. Enjoy experimenting with writing more tests for different scenarios!
