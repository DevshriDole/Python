import re

def find_urls(text):
    url_pattern = r'https?://[^\s,"]+'
    urls = re.findall(url_pattern,text)
    return urls

sample_text = """
Check out our website at https://www.example.com or our blog at http://blog.example.com/posts/123.
Also visit https://another-site.org/about-us for more info.
"""

urls = find_urls(sample_text)
print("Found URLS:")
for url in urls:
    print(url)