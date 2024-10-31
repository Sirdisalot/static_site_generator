import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type(self):
        node = TextNode("This is not a text node", TextType.ITALIC)
        self.assertTrue(node.text_type == TextType.ITALIC)

    def test_eq_url(self):
        node = TextNode("This is not a text node", TextType.ITALIC)
        self.assertTrue(node.url == None)


if __name__ == "__main__":
    unittest.main()