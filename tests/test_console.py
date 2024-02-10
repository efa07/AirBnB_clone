import unittest
from unittest.mock import patch
from io import StringIO
from hbnb_command import HBNBCommand

class HBNBCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.hbnb = HBNBCommand()
        self.output = StringIO()

    def tearDown(self):
        self.output.close()

    def test_do_EOF(self):
        self.assertTrue(self.hbnb.do_EOF(""))

    def test_do_quit(self):
        self.assertTrue(self.hbnb.do_quit(""))

    def test_emptyline(self):
        with patch("sys.stdout", new=self.output):
            self.hbnb.emptyline()
        self.assertEqual(self.output.getvalue(), "")

    def test_do_create_missing_class_name(self):
        with patch("sys.stdout", new=self.output):
            self.hbnb.do_create("")
        self.assertEqual(self.output.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class_name(self):
        with patch("sys.stdout", new=self.output):
            self.hbnb.do_create("invalid_class")
        self.assertEqual(self.output.getvalue(), "** class doesn't exist **\n")

    # Add more test cases for other commands...

if __name__ == "__main__":
    unittest.main()
