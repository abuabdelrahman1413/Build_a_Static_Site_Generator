import re;
def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

# images
# r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
# r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

def main():
    image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i
    print(extract_markdown_images(image));
    print();
    print("#########################");
    print();
    link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    
    print(extract_markdown_links(link));
    
if __name__ == "__main__":
    main()