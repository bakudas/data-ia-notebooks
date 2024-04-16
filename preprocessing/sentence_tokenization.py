#%%
import nltk
from nltk.corpus import gutenberg
from pprint import pprint
import numpy as np

# %%
nltk.download('gutenberg')
nltk.download('punkt')

# %%
# Load text corpora
alice = gutenberg.raw('carroll-alice.txt')
sample_text = alice[:1000]

# %%
print(sample_text)

# %%
len(alice)

# %%
# First 100 chars in the corpus
alice[:100]

# %%
# Default sentece tokenizer
default_st = nltk.sent_tokenize
alice_sentences = default_st(text=alice)
sample_sentences = default_st(text=sample_text)

# %%
print('Total sentences in sample_text:', len(sample_sentences))
print('Sample text sentences :-')
print(np.array(sample_sentences))
print('\nTotal sentences in alice:', len(alice_sentences))
print('First 5 sentences in alice:-')
print(np.array(alice_sentences[0:5]))

# %%
