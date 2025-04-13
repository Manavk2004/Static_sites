import unittest

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

if __name__ == "__main__":
    unittest.main()