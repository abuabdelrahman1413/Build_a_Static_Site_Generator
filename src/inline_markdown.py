from textnode import TextNode, TextType


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


if __name__ == "__main__":
    # Step 1: Create a TextNode with some raw markdown text
    node = TextNode(
        "This is an `example code` within a sentence", TextType.TEXT)

    # Step 2: Call your function
    result_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    # Step 3: Print results to verify they match expected output
    for res_node in result_nodes:
        print(f"Text: {res_node.text}, Type: {res_node.text_type}")
