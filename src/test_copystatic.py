import unittest
from copystatic import extract_title

class TestCopyStatic(unittest.TestCase):
    def test_extract_title(self):
        node = extract_title("# Hello")
        self.assertEqual(node, "Hello")

    def test_no_title(self):
        with self.assertRaises(Exception) as context:
            extract_title("## Hello")
            self.assertTrue("No h1 header" in context.exception)
    
    

if __name__ == "__main__":
    unittest.main()