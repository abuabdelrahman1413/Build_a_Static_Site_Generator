# Enum is used to define the different types of text nodes (e.g. TextNode, ElementNode, etc.)
from enum import Enum

class TextType(Enum):
    """
    Enum is used to define the different types of text nodes (e.g. TextNode, ElementNode, etc.)
    """
    Normal = "normal"
    Bold = "bold"
    Italic = "italic"
    Code = "code"
    Link = "link"
    Image = "image"

class TextNode:
    """
    TextNode is used to define the different types of text nodes (e.g. TextNode, ElementNode, etc.)
    """
    def __init__(self, text: str, textType: TextType, url: str = None):
        self.text = text
        self.textType = textType.value
        self.url = url

    def __eq__(self, other):
        """
        Override the default Equals behavior
        """
        return self.text == other.text and self.textType == other.textType and self.url == other.url
    
    def __repr__(self):
        """
        Override the default representation
        """
        return f"TextNode({self.text}, {self.textType}, {self.url})"
    
