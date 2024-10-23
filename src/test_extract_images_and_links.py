import unittest
import re
from extract_images_and_links import extract_markdown_images, extract_markdown_links

class TestExtractImages(unittest.TestCase):
    def test_one_image(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_images(image),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif")],
        )
        
    def test_two_images(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(image),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
        )
        
    def test_group_images(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)";
        self.assertEqual(
            extract_markdown_images(image),
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
        )
        
class TestExtractLinks(unittest.TestCase):
    def test_one_link(self):
        link = "My email is [lane@example.com](mailto:lane@example.com) and my friend's email is [hunter@example.com](mailto:hunter@example.com)"
        self.assertEqual(
            extract_markdown_links(link),
            [("lane@example.com", "mailto:lane@example.com"), ("hunter@example.com", "mailto:hunter@example.com")],
        )

    def test_two_links(self):
        link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        
        self.assertEqual(
            extract_markdown_links(link),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
        )
        
    def test_group_links(self):
        link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to youtube](https://www.youtube.com/@bootdotdev)";
        self.assertEqual(
            extract_markdown_links(link),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev"), ("to youtube", "https://www.youtube.com/@bootdotdev")],
        )