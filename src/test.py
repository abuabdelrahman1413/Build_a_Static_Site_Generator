# str = "Hello *Moram* i love you";
# strSplited = str.split("*");
# print(strSplited);

list1 = [1,2,3];
list2= [4,4,8,0];
# list1.append(list2);
# print(list1);
print();
print();

list1.extend(list2);
print(list1);


import re

text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
matches = re.findall(r"teapot", text)
print(matches) # ['teapot']
matches2 = re.findall(r"I'm", text);
print(matches2);


text = "My phone number is 555-555-5555 and my friend's number is 555-555-5556"
matches = re.findall(r"\d{3}-\d{3}-\d{4}", text);
print(matches) # ['555-555-5555', '555-555-5556']


text = "I have a (cat) and a (dog)"
matches = re.findall(r"\((.*?)\)", text);
print(matches) # ['cat', 'dog']

text = "My email is lane@example.com and my friend's email is hunter@example.com"
matches = re.findall(r"\w*@\w+\.\w+", text);
print(matches) # ['lane@example.com', 'hunter@example.com']

text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text);
print(matches);
