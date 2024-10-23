from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
    
#############################
######  Main Function  ######
#############################

def test_case(input_text, delimiter, text_type, case_name):
    print(f"\nTesting {case_name}:")
    print(f"Input: {input_text}")
    test_node = TextNode(input_text, TextType.TEXT)
    try:
        result = split_nodes_delimiter([test_node], delimiter, text_type)
        print("Results:")
        for node in result:
            print(f"Text: '{node.text}', Type: {node.text_type}")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    # Test cases - add more!
    test_case(
        "This is text with a `code block` in it",
        "`",
        TextType.CODE,
        "Simple code block"
    )
    
    test_case(
        "Here's **bold** text",
        "**",
        TextType.BOLD,
        "Simple bold text"
    )
    
    test_case(
        "Multiple `code` blocks `here` test",
        "`",
        TextType.CODE,
        "Multiple code blocks"
    )

    # Add more test cases here! Some ideas:
    # - Text with no delimiters
    # - Text with mismatched delimiters
    # - Text with delimiters at the start/end
    # - Empty text between delimiters
    # - Multiple delimiter pairs
    # - Spaces around delimiters
    # - ...what else can you think of?

if __name__ == "__main__":
    main()