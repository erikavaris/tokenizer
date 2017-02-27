#tokenizer, borrowing/built heavily from nltk
import nltk
from nltk.tokenize.casual import remove_handles, reduce_lengthening, _str_to_unicode, _replace_html_entities # EMOTICONS, EMOTICON_RE
import re

#urls - nltk version
URLS = r"""         # Capture 1: entire matched URL
  (?:
  https?:               # URL protocol and colon
    (?:
      /{1,3}                # 1-3 slashes
      |                 #   or
      [a-z0-9%]             # Single letter or digit or '%'
                                       # (Trying not to match e.g. "URI::Escape")
    )
    |                   #   or
                                       # looks like domain name followed by a slash:
    [a-z0-9.\-]+[.]
    (?:[a-z]{2,13})
    /
  )
  (?:                   # One or more:
    [^\s()<>{}\[\]]+            # Run of non-space, non-()<>{}[]
    |                   #   or
    \([^\s()]*?\([^\s()]+\)[^\s()]*?\) # balanced parens, one level deep: (...(...)...)
    |
    \([^\s]+?\)             # balanced parens, non-recursive: (...)
  )+
  (?:                   # End with:
    \([^\s()]*?\([^\s()]+\)[^\s()]*?\) # balanced parens, one level deep: (...(...)...)
    |
    \([^\s]+?\)             # balanced parens, non-recursive: (...)
    |                   #   or
    [^\s`!()\[\]{};:'".,<>?«»“”‘’]  # not a space or one of these punct chars
  )
  |                 # OR, the following to match naked domains:
  (?:
    (?<!@)                  # not preceded by a @, avoid matching foo@_gmail.com_
    [a-z0-9]+
    (?:[.\-][a-z0-9]+)*
    [.]
    (?:[a-z]{2,13})
    \b
    /?
    (?!@)                   # not succeeded by a @,
                            # avoid matching "foo.na" in "foo.na@example.com"
  )
"""

#my url version
#URLS = r"""(((http(s?):\/\/|www)|\w+\.(\w{2-3}))([\w\!#$&-;=\?\-\[\]~]|%[0-9a-fA-F]{2})+)"""

#my emoticons, borrowed & expanded from https://github.com/g-c-k/idiml/blob/master/predict/src/main/resources/data/emoticons.txt

EMOTICONS = []
with open('emoticons.txt', 'r') as f:
    for line in f:
        item = line.rstrip('\n')
        item = re.escape(item)
        EMOTICONS.append(item)

# Twitter specific:
HASHTAG = r"""(?:\#\w+)"""
TWITTER_USER = r"""(?:@\w+)"""

#separately compiled regexps
TWITTER_USER_RE = re.compile(TWITTER_USER, re.UNICODE)
HASHTAG_RE = re.compile(HASHTAG, re.UNICODE)
HASH_RE = re.compile(r'#(?=\w+)', re.UNICODE)
URL_RE = re.compile(URLS, re.UNICODE)
EMOTICON_RE = re.compile(r"""(%s)""" % "|".join(EMOTICONS), re.UNICODE)

# more regular expressions for word compilation, borrowed from nltk
#phone numbers
PHONE = r"""(?:(?:\+?[01][\-\s.]*)?(?:[\(]?\d{3}[\-\s.\)]*)?\d{3}[\-\s.]*\d{4})"""

# email addresses
EMAILS = r"""[\w.+-]+@[\w-]+\.(?:[\w-]\.?)+[\w-]"""
# HTML tags:
HTML_TAGS = r"""<[^>\s]+>"""
# ASCII Arrows
ASCII_ARROWS = r"""[\-]+>|<[\-]+"""
#long non-word, non-numeric repeats
#HANGS = r"""([^a-zA-Z0-9])\1{3,}"""
# Remaining word types:
WORDS = r"""
    (?:[^\W\d_](?:[^\W\d_]|['\-_])+[^\W\d_]) # Words with apostrophes or dashes.
    |
    (?:[+\-]?\d+[,/.:-]\d+[+\-]?)  # Numbers, including fractions, decimals.
    |
    (?:[\w_]+)                     # Words without apostrophes or dashes.
    |
    (?:\.(?:\s*\.){1,})            # Ellipsis dots.
    |
    (?:\S)                         # Everything else that isn't whitespace.
    """
TWITTER_REGEXPS = [URLS, PHONE] + EMOTICONS + [HTML_TAGS, ASCII_ARROWS, TWITTER_USER, HASHTAG, EMAILS, WORDS]

#WORD_RE = re.compile(r"""(%s)""" % "|".join(REGEXPS), re.VERBOSE | re.I | re.UNICODE)

class TweetTokenizer():

    def __init__(self, preserve_case=True, preserve_handles=True, preserve_hashes=True, regularize=False, preserve_len=True, preserve_emoji=True, preserve_html=True):
        self.preserve_case = preserve_case
        self.preserve_handles = preserve_handles
        self.preserve_hashes = preserve_hashes #keep the hash symbol; if False, strips the hash so that the token looks the same as non-hashtag tokens
        self.regularize = regularize # TODO
        self.preserve_len = preserve_len
        self.preserve_emoji = preserve_emoji # TODO
        self.preserve_html = preserve_html
        self.WORD_RE = re.compile(r"""(%s)""" % "|".join(TWITTER_REGEXPS), re.VERBOSE | re.I | re.UNICODE)

    def tokenize(self, text):
        text = _replace_html_entities(text)
        if not self.preserve_handles:
            text = re.sub(TWITTER_USER_RE, ' ', text)
        if not self.preserve_hashes:
            text = re.sub(HASH_RE, '', text)
        if not self.preserve_html:
            text = re.sub(URLS, ' ', text)
        if not self.preserve_len:
            text = reduce_lengthening(text)
        words = self.WORD_RE.findall(text)
        if not self.preserve_case:
            words = list(map((lambda x : x if EMOTICON_RE.search(x) else
                              x.lower()), words))
        return words



