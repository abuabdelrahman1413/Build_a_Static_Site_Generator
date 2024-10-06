from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode


def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": "https://www.google.com"})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": "https://www.google.com", "alt": "image"})
    else:
        raise ValueError("Invalid text type")
