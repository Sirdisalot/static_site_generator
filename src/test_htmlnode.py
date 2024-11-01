import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()