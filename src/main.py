from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode

# def main():
#     # Example 1: Simple paragraph
#     paragraph = LeafNode("p", "This is a paragraph of text.")
#     print("Example 1:")
#     print(paragraph.to_html())
#     print()

#     # Example 2: Link with href attribute
#     link = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
#     print("Example 2:")
#     print(link.to_html())
#     print()

#     # Example 3: Span with multiple attributes
#     span = LeafNode("span", "Styled text", {"style": "color: blue;", "class": "highlight"})
#     print("Example 3:")
#     print(span.to_html())
#     print()

#     # Example 4: LeafNode with no tag (raw text)
#     raw_text = LeafNode(None, "This is just some text.")
#     print("Example 4:")
#     print(raw_text.to_html())
#     print()

#     # Example 5: Trying to create a LeafNode with no value (should raise an error)
#     try:
#         invalid_node = LeafNode("p", None)
#         invalid_node.to_html()
#     except ValueError as e:
#         print("Example 5 (Error case):")
#         print(f"ValueError: {e}")

def main():
    # Test case 1: Simple parent node with leaf children
    simple_parent = ParentNode(
        "div",
        [
            LeafNode("p", "This is a paragraph"),
            LeafNode("span", "This is a span"),
        ]
    )
    print("Simple parent node:")
    print(simple_parent.to_html())
    print()

    # Test case 2: Nested parent nodes
    nested_parent = ParentNode(
        "section",
        [
            LeafNode("h1", "Title"),
            ParentNode(
                "article",
                [
                    LeafNode("p", "Article paragraph 1"),
                    LeafNode("p", "Article paragraph 2"),
                ]
            ),
        ]
    )
    print("Nested parent nodes:")
    print(nested_parent.to_html())
    print()

    # Test case 3: Parent node with properties
    parent_with_props = ParentNode(
        "div",
        [LeafNode("p", "Paragraph with class")],
        {"class": "container", "id": "main"}
    )
    print("Parent node with properties:")
    print(parent_with_props.to_html())
    print()

    # Test case 4: Error case - no tag
    try:
        no_tag = ParentNode(None, [LeafNode("p", "This should fail")])
        print(no_tag.to_html())
    except ValueError as e:
        print(f"Correctly raised ValueError: {e}")
    print()

    # Test case 5: Error case - no children
    try:
        no_children = ParentNode("div", [])
        print(no_children.to_html())
    except ValueError as e:
        print(f"Correctly raised ValueError: {e}")

    
if __name__ == "__main__":
    main()