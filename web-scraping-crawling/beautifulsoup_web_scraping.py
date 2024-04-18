# Webscraping com BeautifulSoup

# Setup Ambiente:
# Nesse notebook exploraremos os fundamentos de realização de Raspagem de Dados. Usaremos as seguintes bibliotecas:
# BeautifulSoup - Interpreta o código HTML das páginas e nos permite especificar de onde pegar os dados
# Requests - Realiza chamadas HTTP e baixa o código fonte da página que queremos baixar
# pip install beautifulsoup4

# Importando as bibliotecas
#%%
from bs4 import BeautifulSoup

# %%
import requests

# %%
# Exemplo simples usando HTML próprio
source_code = """
<html>
  <head>
    <title>Título da Página</title>
    <meta name="author" content="John Doe">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <h1>Introdução</h1>
    <p>Esse é o texto introdutório para a página atual.</p>
    <p>Um documento pode conter vários parágrafos</p>
    <p>Esse texto foi escrito por <span class="author">Fulano</span></p>
  </body>
</html>
"""

# %%
soup = BeautifulSoup(source_code, 'html.parser') # Cria o objeto BeautifulSoup

# %%
soup.title # Retorna a tag <title>

# %%
soup.title.text # ou .string

# %%
print(soup.prettify()) # Exibe o HTML formatado

# %%
# Exemplo utilizando CSS Locator
soup.select('p') # Retorna uma lista com todos os parágrafos

# %%
soup.select_one('h1').text # ou .string

# %%
soup.select_one('span.author').string # ou .text

# %%
# Raspanda uma notícia do site G1
url = 'https://valor.globo.com/empresas/noticia/2024/04/18/fusoes-e-aquisicoes-no-setor-de-energia-devem-movimentar-r-30-bilhoes-neste-ano.ghtml'

# %%
response = requests.get(url) # Faz a requisição da página
source_code = response.text # Pega o conteúdo da página
source_code[:1000] # Exibe os primeiros 1000 caracteres

# %%
soup = BeautifulSoup(source_code, 'html.parser') # Cria o objeto BeautifulSoup

# %%
soup.title.text # Exibe o título da página

# %%
title_element = soup.select_one('.title') # Seleciona o elemento com a classe 'title'
print(title_element.text) # Exibe o título da notícia

# %%
# Usar o get_text() para unir texto com um separador por nós (/n)
body = soup.select_one('.mc-article-body').get_text(separator='\n')
print(body)

# %%
# Limpar o texto da notícia
clean_body = [x.strip() for x in body.splitlines()] # Remove espaços em branco
clean_body = [x for x in clean_body if x] # Remove linhas vazias
clean_body = '\n'.join(clean_body) # Junta as linhas em um único texto
print(clean_body)
