import unittest
import lab_2
from unittest.mock import patch
from io import StringIO


class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.student_list = []

    def test_printAllList(self):
        self.student_list = [
            {"name": "Alex", "age": 20, "phone": "111", "country": "USA"}
        ]

        with patch("sys.stdout", new_callable=StringIO) as fake_output:
            lab_2.printAllList(self.student_list)
            output = fake_output.getvalue().strip()

        expected = "Student name is Alex, Age is 20, Phone is 111, Country is USA"
        self.assertEqual(output, expected)

    def test_deleteElement(self):
        self.student_list = [
            {"name": "Bob", "age": 25, "phone": "222", "country": "UK"}
        ]

        with patch("builtins.input", return_value="Bob"):
            lab_2.deleteElement(self.student_list)

        self.assertEqual(len(self.student_list), 0)

    def test_deleteElement_not_found(self):
        self.student_list = [
            {"name": "Bob", "age": 25, "phone": "222", "country": "UK"}
        ]

        with patch("builtins.input", return_value="Alex"):
            lab_2.deleteElement(self.student_list)

        self.assertEqual(len(self.student_list), 1)

    def test_addNewElement(self):
        self.student_list = [
            {"name": "Bob", "age": 25, "phone": "222", "country": "UK"}
        ]

        with patch("builtins.input", side_effect=["Alice", "111", "20", "USA"]):
            lab_2.addNewElement(self.student_list)

        self.assertEqual(len(self.student_list), 2)
        self.assertEqual(self.student_list[0]["name"], "Alice")

    def test_updateElement_found(self):
        self.student_list = [
            {"name": "Bob", "age": 25, "phone": "222", "country": "UK"}
        ]

        with patch("builtins.input", side_effect=["Bob", "Bob_Updated", "333", "26", "Germany"]):
            lab_2.updateElement(self.student_list)

        self.assertEqual(len(self.student_list), 1)
        self.assertEqual(self.student_list[0]["name"], "Bob_Updated")

    def test_updateElement_not_found(self):
        self.student_list = [
            {"name": "Bob", "age": 25, "phone": "222", "country": "UK"}
        ]

        with patch("builtins.input", return_value="Alex"):
            lab_2.updateElement(self.student_list)

        self.assertEqual(len(self.student_list), 1)


if __name__ == "__main__":
    unittest.main()