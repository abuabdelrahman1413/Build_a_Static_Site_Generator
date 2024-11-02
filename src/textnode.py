from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        """
        :param text: the text to be represented
        :param text_type: the type of the text, see TextType Enum
        :param url: the url to be linked to (optional)
        """
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        """
        Check if two TextNode objects are equal.

        Two TextNode objects are considered equal if and only if their
        text_type, text, and url attributes are equal.
        """
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        """
        Return a string representation of this TextNode.

        This method returns a string in the format
        `TextNode(text, text_type, url)`. The string is meant to be
        unambiguous and easy for a human to read.
        """

        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    """
    Convert a TextNode to an HTMLNode.

    Args:
        text_node (TextNode): The TextNode to convert.

    Returns:
        HTMLNode: The converted HTMLNode.

    Raises:
        ValueError: If the TextNode's text_type is not one of TEXT, BOLD, ITALIC, CODE, LINK, or IMAGE.
    """
    if text_node.text_type == TextType.TEXT.value:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD.value:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC.value:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE.value:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK.value:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE.value:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text_type}")
