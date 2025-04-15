import unittest
from split_nodes import *

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

#markdown_imagdef test_extract_markdown_images(self):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_images_multiple(self):
        text = "![cat](https://i.imgur.com/cat.jpg) and ![dog](https://i.imgur.com/dog.jpg)"
        expected = [("cat", "https://i.imgur.com/cat.jpg"), ("dog", "https://i.imgur.com/dog.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_empty(self):
        text = "This has no images"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_nested_brackets(self):
        text = "![this [is] tricky](https://i.imgur.com/nested.png)"
        expected = [("this [is] tricky", "https://i.imgur.com/nested.png")]
        self.assertNotEqual(extract_markdown_images(text), expected)


#Split Nodes links and images


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )
def test_split_link_middle(self):
    node = TextNode(
        "Check out [BootDev](https://www.boot.dev) for backend courses!",
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    self.assertEqual(
        new_nodes,
        [
            TextNode("Check out ", TextType.TEXT),
            TextNode("BootDev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" for backend courses!", TextType.TEXT),
        ]
    )

def test_split_multiple_links_only(self):
    node = TextNode(
        "[Google](https://google.com)[YouTube](https://youtube.com)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    self.assertEqual(
        new_nodes,
        [
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode("YouTube", TextType.LINK, "https://youtube.com"),
        ]
    )

def test_split_link_with_spaces(self):
    node = TextNode(
        "See the docs [here](https://docs.python.org) for more info.",
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    self.assertEqual(
        new_nodes,
        [
            TextNode("See the docs ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://docs.python.org"),
            TextNode(" for more info.", TextType.TEXT),
        ]
    )











if __name__ == "__main__":
    unittest.main()
