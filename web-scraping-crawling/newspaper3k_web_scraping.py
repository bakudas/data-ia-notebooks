# Web Scraping with Newspaper3k

# Nesse notebook exploraremos os fundamentos de realização de Raspagem de Dados. Usaremos as seguintes bibliotecas:
# Newspaper3k - Biblioteca com heurísticas prontas para raspar sites de notícias
# Requests - Realiza chamadas HTTP e baixa o código fonte da página que queremos baixar

# Importando as bibliotecas
# %%
import requests
import newspaper
from newspaper import Article

# %%
# Baixando uma página específica
url = 'https://www.bbc.com/portuguese/articles/c72pr0yjzjlo'

# %%
article = Article(url)
article.download()
article.parse()

# %%
print(article.title)
print(article.authors)
print(article.publish_date)

# %%
# Running some nlp with newspaper
article.nlp()

# %%
print("Title: \n" + str(article.title))
print("Authors: \n" + str(article.authors))
print("Summary(nlp): \n" + str(article.summary))
print("Keywords(nlp): \n" + str(article.keywords))
print("Top Image: \n" + article.top_image)
print("Article URL: \n" + str(article.url))

# %%
# Using build fuction to get all the information
globo = newspaper.build('http://globo.com/')

# %%
# Print the number of articles
print(globo.size())

# %%
# Print url of the first 10 articles
[a.url for a in globo.articles[:10]]

# %%
# Print the first 10 articles details
[print("- {} - {:%d/%m/%Y}".format(a.title, a.publish_date)) for a in globo.articles[1:11]]
