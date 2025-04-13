import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
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
    
#LeafNode
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            "<a href='https://www.google.com'>Click me!</a>",
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

#ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

#text_node_to_html_node
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link_text(self):
        node = TextNode("Boot.dev", TextType.LINK, url="https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<a>Boot.dev</a>")

    def test_image_node(self):
        node = TextNode("Dog photo", TextType.IMAGE, url="dog.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<img src='dog.jpg' alt='Dog photo'>")

    

if __name__ == "__main__":
    unittest.main()