# Enum is used to define the different types of text nodes (e.g. TextNode, ElementNode, etc.)
from enum import Enum

class TextType(Enum):
    """
    Enum is used to define the different types of text nodes (e.g. TextNode, ElementNode, etc.)
    """
    HTML = "html"
    LEAF = "leaf"
    Text = "text"

