import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq(self):
        node = TextNode("This is a test", TextType.URL)
        node2 = TextNode("This is a test", TextType.URL)
        self.assertEqual(node, node2)
    def test_eq(self):
        node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    #HTMLNode

    def test_html_nodes(self):
        node = HTMLNode("b", "I want to learn to program", None, {'href': 'https://www.google.com', 'target': '_blank'})
        self.assertEqual(node.tag, "b")
        self.assertNotEqual(node.value, "I dont want to learn programming")
        self.assertEqual(node.children, None)

if __name__ == "__main__":
    unittest.main()