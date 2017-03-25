# Tokenizer

A tokenizer adapted for Twitter and other casual speech, with some regularization/normalization features.
Written in Python 3. Heavily based on nltk, but with a few more features added.

Some unit tests are included for the regularizer and tokenizer scripts.

## To Install

Easy peasy, lemon squeezy. (I checked in a virtualenv, and it worked!).

```
pip install git+https://github.com/erikavaris/tokenizer.git
```

## Usage

In the default (no regularization or normalization):

```
from tokenizer import tokenizer
T = tokenizer.TweetTokenizer()

tweet = "Hey @NLPer! This is a #NLProc tweet :-D"
tokens = T.tokenize(tweet)

print(tokens)

['Hey', '@NLPer', '!', 'This', 'is', 'a', '#NLProc', 'tweet', ':-D']
```

Strip handles, strip hash symbol, lowercase, take out urls:

```
from tokenizer import tokenizer
T = tokenizer.TweetTokenizer(preserve_handles=False, preserve_hashes=False, preserve_case=False, preserve_url=False)

tweet = "Hey @NLPer! This is a #NLProc tweet :-D http://www.somelink.com"
tokens = T.tokenize(tweet)

print(tokens)

['hey', '!', 'this', 'is', 'a', 'nlproc', 'tweet', ':-D']
```

Regularize common contractions:

```
from tokenizer import tokenizer
T = tokenizer.TweetTokenizer(regularize=True)

tweet = "Swear im gonna push this soon"
tokens = T.tokenize(tweet)

print(tokens)

['Swear', 'I', 'am', 'going', 'to', 'push', 'this', 'soon']
```

## Reddit version

A version of the tokenizer sensitive to Reddit usernames is also provided.

```
from tokenizer import tokenizer
R = tokenizer.RedditTokenizer()

text = "Hey u/NLPer! This is a #NLProc message."
tokens = R.tokenize(text)

print(tokens)

['Hey', 'u/NLPer', '!', 'This', 'is', 'a', '#NLProc', 'message', '.']
```


