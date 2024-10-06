import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode
from node_converters import text_node_to_html_node
from textnode import TextNode


class TestNodeConverters(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Hello, world!", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Hello, world!")

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Hello, world!", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Hello, world!</b>")

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Hello, world!", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Hello, world!</i>")

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Hello, world!", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<code>Hello, world!</code>")

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Hello, world!", "link")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(), '<a href="https://www.google.com">Hello, world!</a>'
        )

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("Hello, world!", "image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<img src="https://www.google.com" alt="image"></img>',
        )
