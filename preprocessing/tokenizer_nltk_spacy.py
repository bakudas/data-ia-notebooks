#%%
import nltk
import spacy
import numpy as np

# %%
def tokenize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens

# %%
sample_text = """On a holiday to Kerala on India's south-western Malabar Coast,
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
    health and longevity."""

# %%
sents = tokenize_text(sample_text)
print(sents)

# %%
# download spacy model
# !python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')
text_spacy = nlp(sample_text)
sentences = [str(sent) for sent in text_spacy.sents]
print(np.array(sentences))

sent_words = [str([(word.text) for word in sent]) for sent in text_spacy.sents]
np.array(sent_words)

words = [word.text for word in text_spacy]
np.array(words)

# %%
# Remove accents from words
from unicodedata import normalize
def remove_accented_chars(text):
    text = normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

# %%
remove_accented_chars('Sómě Áccěntěd těxt, ãoût åccěntěd chårš')

# %%
# Expand contractions
import re

# %%
CONTRACTION_MAP = {
    "ain't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "Y'all": "You all",
    "I've": "I have",
}

# %%
def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match) if contraction_mapping.get(match) else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction
    expanded_text = contractions_pattern.sub(expand_match, text)
    return expanded_text

# %%
expand_contractions("Y'all can't expand contractions I'd think")

# %%
# Remove special characters
def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
    text = re.sub(pattern, '', text)
    return text

# %%
remove_special_characters("Well this was fun! What do you think? 123#@!", True)

# %%
# Case conversion
def text_lowercase(text):
    return text.lower()

def text_uppercase(text):
    return text.upper()

# %%
# Text Correction
# Correct Repeating Characters
def correct_repeating_characters(text):
    def remove_repeating_char(match_obj):
        char = match_obj.group(0) # Get the matched character
        return char[0]
    corrected_text = re.sub(r'(.)\1+', remove_repeating_char, text) # Remove repeating characters
    return corrected_text

correct_repeating_characters("I looooveee youuuuuu")

# Correct Repeating Characters with nltk
from nltk.corpus import wordnet # Import wordnet from the NLTK
nltk.download('wordnet') # Download wordnet

def remove_repeating_characters(tokens):
    repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)') # Create a regex pattern to identify repeating characters
    match_substitution = r'\1\2\3' # Create a substitution pattern to remove repeating characters
    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word # Return the word if it is a valid word
        new_word = repeat_pattern.sub(match_substitution, old_word) # Replace repeating characters
        return replace(new_word) if new_word != old_word else new_word # Recur if the word is changed
    correct_tokens = [replace(word) for word in tokens] # Iterate over each token
    return correct_tokens

sample_sentence = "My schooool is realllllyyy amaaazinggggg and coolllll"
correct_tokens = remove_repeating_characters(nltk.word_tokenize(sample_sentence))
' '.join(correct_tokens)
