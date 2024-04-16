#%%
import requests

# %%
url = 'https://www.gutenberg.org/cache/epub/8001/pg8001-images.html'
data = requests.get(url)
print(data.content)

# %%
print(data.content[1163:2200])

# %%
import re
from bs4 import BeautifulSoup

# %%
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    return stripped_text

# %%
clean_content = strip_html_tags(data.content)

# %%
print(clean_content[803:])
