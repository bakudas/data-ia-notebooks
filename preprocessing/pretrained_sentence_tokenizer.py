#%%
import nltk
from nltk.corpus import europarl_raw
nltk.download('europarl_raw')
german_text = europarl_raw.german.raw(fileids='ep-00-01-17.de')

# %%
# Total characters in the corpus
print(len(german_text))
# First 100 chars in the corpus
print(german_text[:100])

# %%
# Default sentece tokenizer
default_st = nltk.sent_tokenize
german_default_st = default_st(text=german_text, language='german')

# %%
# Load the german tokenizer
german_tokenizer = nltk.data.load(resource_url='tokenizers/punkt/german.pickle')
german_sentences = german_tokenizer.tokenize(german_text)

# %%
print(type(german_tokenizer))
print(german_default_st == german_sentences)

# %%
# PunkSentenceTokenizer
# Verify the type of german_tokenizer
# Should be PunktSentenceTokenizer
print(type(german_tokenizer))

# %%
import numpy as np
# Print the first 5 sentences
print(np.array(german_sentences[:5]))

# %%
# RegexpTokenizer
SENTENCE_TOKENS_PATTERN = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
regex_st = nltk.tokenize.RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True)
sample_sentence = regex_st.tokenize(german_text)
print(np.array(sample_sentence[:5]))
