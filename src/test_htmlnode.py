import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_value_none(self):
        node = HTMLNode(props=None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_single_props_value(self):
        node = HTMLNode(props={"target": "_blank"})
        excpected = f' target="_blank"'
        self.assertEqual(node.props_to_html(), excpected)

    def test_multiple_props_values(self):
        node = HTMLNode(props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        expected = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode(
    tag="a",
    value="Click me",
    props={"href": "https://boot.dev"},
    children=None
)
        print(node)

    def test_tag_value_none(self):
        node = LeafNode(tag=None, value="a")
        expected = "a"
        self.assertEqual(node.to_html(), expected)

    def test_value_none(self):
        node = LeafNode(tag="a", value=None)
        self.assertRaises(ValueError)

    def test_tag_value_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        excpected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), excpected)

    def test_multiple_entries(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = "<p>This is a paragraph of text.</p>"
        expected2= '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node2.to_html(), expected2)
    

if __name__ == "__main__":
    unittest.main()