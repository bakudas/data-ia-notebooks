#%%
import nltk
import numpy as np

# %%
sample_text = """
    On a holiday to Kerala on India's south-western Malabar Coast,
    Shilpa Iyer decided to visit Kotakkal, a town that became famous after
    the establishment of Arya Vaidya Sala, Kerala's best-known centre for
    the practice of Ayurveda, in 1902. Seven days later, she left the
    historical treatment centre after completeing panchakarma, a cleansing
    and rejuvenating programme for the body, mind and consciousness.

    "There was nothing really wrong, but I was always busy with the demands
    of modern life and plagued with continual aches and pains. So, I decided
    to focus on my own health," Iyer says.

    Panchakarma, a holistic Ayurvedic therapy, involves a series of
    detoxifying procedures. It integrates herbal medicines, cleansing
    therapies, personalised diet plans and wellness activities to eliminate
    the root cause of disease, revive and rejuvenate the body, and ensure
    health and longevity.
"""

# %%
# Default word tokenizer from nltk
# This tokenizer divides a text into a list of words(tokens)
default_wt = nltk.word_tokenize(sample_text)
print(np.array(default_wt))

# %%
# TreeBankWordTokenizer from nltk
# This tokenizer uses regular expressions to tokenize text as in Penn Treebank
# It assumes that the text has already been segmented into sentences
# and it tokenizes the sentences into words
treebank_wt = nltk.TreebankWordTokenizer()
words = treebank_wt.tokenize(sample_text)
print(np.array(words))

# %%
# TokTokTokenizer from nltk
# This tokenizer splits punctuation from words and splits contractions
# For example, don't becomes do n't and word's becomes word 's
from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()
words = tokenizer.tokenize(sample_text)
print(np.array(words))


# %%
# RegexpTokenizer from nltk
# This tokenizer splits a string into substrings using a regular expression
# The regular expression passed as an argument to the tokenizer is
# used to identify the delimiters
from nltk.tokenize import RegexpTokenizer
TOKEN_PATTERN = r'\w+'  # This pattern matches words
regex_wt = RegexpTokenizer(pattern=TOKEN_PATTERN, gaps=False)
words = regex_wt.tokenize(sample_text)
print(np.array(words))

# pattern to identify tokens by using gaps
GAP_PATTERN = r'\s+'  # This pattern matches spaces
regex_wt = RegexpTokenizer(pattern=GAP_PATTERN, gaps=True)
words = regex_wt.tokenize(sample_text)
print(np.array(words))

# %%
word_indices = list(regex_wt.span_tokenize(sample_text))
print(word_indices)
print(np.array([sample_text[start:end] for start, end in word_indices]))

# %%
# Inherited Tokenizers from RegexpTokenizer
# WordPunctTokenizer
from nltk.tokenize import WordPunctTokenizer
word_punct = WordPunctTokenizer()
words = word_punct.tokenize(sample_text)
print(np.array(words))

# WhitespaceTokenizer
from nltk.tokenize import WhitespaceTokenizer
whitespace_wt = WhitespaceTokenizer()
words = whitespace_wt.tokenize(sample_text)
print(np.array(words))
