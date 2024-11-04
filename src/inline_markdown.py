import re  # Import the regular expressions module for pattern matching

# Import custom classes for representing nodes of text and text types
from textnode import TextNode, TextType


# Define a function to split nodes by a specified delimiter, applying specific text types
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []  # List to store the newly processed nodes
    for old_node in old_nodes:  # Iterate through each old node
        # Skip processing if the node's type isn't a regular text type
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []  # Temporary list for nodes created by splitting the text
        # Split text by the delimiter
        sections = old_node.text.split(delimiter)
        # Check if delimiter-based formatting is balanced, raising an error if not
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        # Alternate between normal text and the specified text type
        for i in range(len(sections)):
            if sections[i] == "":  # Skip empty sections
                continue
            # Assign text type based on position in the split sections
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        # Append all split nodes to the final list
        new_nodes.extend(split_nodes)
    return new_nodes  # Return the list of newly split nodes


# Define a function to extract and separate image nodes from text
def split_nodes_image(old_nodes):
    new_nodes = []  # List to store nodes after processing
    for old_node in old_nodes:  # Iterate over each old node
        if old_node.text_type != TextType.TEXT.value:  # Process only text nodes
            new_nodes.append(old_node)
            continue
        original_text = old_node.text  # Store the text of the current node
        images = extract_markdown_images(
            original_text)  # Extract image patterns
        if len(images) == 0:  # Skip if no images are found
            new_nodes.append(old_node)
            continue
        for image in images:  # Process each extracted image
            # Split text by the found image pattern, ensuring two sections
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            # Append text before the image if it exists
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # Create an image node with alt text and URL, then append it
            new_nodes.append(
                TextNode(
                    image[0],  # Alt text for the image
                    TextType.IMAGE,  # Node type as IMAGE
                    image[1],  # URL for the image
                )
            )
            # Set remaining text to process further
            original_text = sections[1]
        # Append any remaining text as a regular text node
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes  # Return the list with split image nodes


# Define a function to separate link nodes from text
def split_nodes_link(old_nodes):
    new_nodes = []  # List to store processed nodes
    for old_node in old_nodes:  # Iterate through each old node
        if old_node.text_type != TextType.TEXT.value:  # Skip non-text nodes
            new_nodes.append(old_node)
            continue
        original_text = old_node.text  # Store the text of the current node
        links = extract_markdown_links(original_text)  # Extract link patterns
        if len(links) == 0:  # Skip if no links are found
            new_nodes.append(old_node)
            continue
        for link in links:  # Process each extracted link
            # Split text by the found link pattern, ensuring two sections
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            # Append text before the link if it exists
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            # Create a link node with display text and URL, then append it
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            # Set remaining text to process further
            original_text = sections[1]
        # Append any remaining text as a regular text node
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes  # Return the list with split link nodes


# Define a function to extract all image patterns from the given text
def extract_markdown_images(text):
    # Pattern to match markdown image syntax ![alt_text](url)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)  # Find all matches
    return matches  # Return list of (alt_text, url) pairs


# Define a function to extract all link patterns from the given text
def extract_markdown_links(text):
    # Pattern to match markdown link syntax [text](url) excluding images
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)  # Find all matches
    return matches  # Return list of (text, url) pairs
