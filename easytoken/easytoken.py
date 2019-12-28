from itertools import chain
import os
import sys
import nltk

import re
import string

PUNCTUATION_REGEX = re.compile('[{0}]'.format(re.escape(string.punctuation)))


def strip_punchuation(s, all=False):
    """Removes punctuation from a string.
    :param s: The string.
    :param all: Remove all punctuation. If False, only removes punctuation from
        the ends of the string.
    """
    if all:
        return PUNCTUATION_REGEX.sub('', s.strip())
    else:
        return s.strip().strip(string.punctuation)


def itokenize(self, text, *args, **kwargs):
        """Return a generator that generates tokens "on-demand".
        .. versionadded:: 0.6.0
        :rtype: generator
        """
        return (t for t in self.tokenize(text, *args, **kwargs))


def lowerstrip(s, all=False):
    """Makes text all lowercase and strips punctuation and whitespace.
    :param s: The string.
    :param all: Remove all punctuation. If False, only removes punctuation from
        the ends of the string.
    """
    return strip_punchuation(s.lower().strip(), all=all)


class Wordeasytoken():
    """NLTK's recommended word easytoken (currently the TreeBankeasytoken).
    Uses regular expressions to tokenize text. Assumes text has already been
    segmented into sentences.
    Performs the following steps:
    * split standard contractions, e.g. don't -> do n't
    * split commas and single quotes
    * separate periods that appear at the end of line
    """

    def tokenize(self, text, include_punc=True):
        '''Return a list of word tokens.
        :param text: string of text.
        :param include_punc: (optional) whether to include punctuation as separate tokens. Default to True.
        '''
        tokens = nltk.tokenize.word_tokenize(text)
        if include_punc:
            return tokens
        else:
            # Return each word token
            # Strips punctuation unless the word comes from a contraction
            # e.g. "Let's" => ["Let", "'s"]
            # e.g. "Can't" => ["Ca", "n't"]
            # e.g. "home." => ['home']
            return [word if word.startswith("'") else strip_punchuation(word, all=False)
                    for word in tokens if strip_punchuation(word, all=False)]


class Sentenceeasytoken():
    """NLTK's sentence easytoken (currently PunktSentenceeasytoken).
    Uses an unsupervised algorithm to build a model for abbreviation words,
    collocations, and words that start sentences,
    then uses that to find sentence boundaries.
    """

    # @requires_nltk_corpus
    def tokenize(self, text):
        '''Return a list of sentences.'''
        return nltk.tokenize.sent_tokenize(text)

    def itokenize(self, text, *args, **kwargs):
        """Return a generator that generates tokens "on-demand".
        .. versionadded:: 0.6.0
        :rtype: generator
        """
        return (t for t in self.tokenize(text, *args, **kwargs))


#: Convenience function for tokenizing sentences
sent_tokenize = Sentenceeasytoken().itokenize

_word_easytoken = Wordeasytoken()  # Singleton word easytoken


def word_tokenize(text, include_punc=True, *args, **kwargs):
    """Convenience function for tokenizing text into words.
    NOTE: NLTK's word easytoken expects sentences as input, so the text will be
    tokenized to sentences before being tokenized to words.
    """
    words = chain.from_iterable(
        _word_easytoken.itokenize(sentence, include_punc=include_punc,
                                  *args, **kwargs)
        for sentence in sent_tokenize(text))
    return words



if __name__ == "__main__":
    print(Wordeasytoken.tokenize(Wordeasytoken,text="I am a good boy"))