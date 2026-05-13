import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    input_wrong = "This is a header"
    input_double = "# This is a header # This isn't"
    result = "This is a header"
    def test_no_hash(self):
        with self.assertRaises(ValueError):
            extract_title(self.input_wrong)
    
    def test_title_double_hash(self):
        self.assertEqual(extract_title(self.input_double), "This is a header # This isn't") 
    
    def test_title_correct(self):
        self.assertEqual(extract_title("# This is a header"), "This is a header")
                        

if __name__ == "__main__":
    unittest.main()