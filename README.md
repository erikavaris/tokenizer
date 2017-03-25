# Tokenizer

A tokenizer adapted for Twitter and other casual speech, with some regularization/normalization features.
Written in Python 3. Heavily based on nltk, but with a few more features added.

Some unit tests are included for the regularizer and tokenizer scripts.

# Usage

In the default (no regularization or normalization):

```
import tokenizer
T = tokenizer.TweetTokenizer()

tweet = "Hey @NLPer! This is a #NLProc tweet :-D"
tokens = T.tokenize(tweet)

print(tokens)

['Hey', '@NLPer', '!', 'This', 'is', 'a', '#NLProc', 'tweet', ':-D']
```

Strip handles, strip hash symbol, lowercase, take out urls:

```
import tokenizer
T = tokenizer.TweetTokenizer(preserve_handles=False, preserve_hashes=False, preserve_case=False, preserve_url=False)

tweet = "Hey @NLPer! This is a #NLProc tweet :-D http://www.somelink.com"
tokens = T.tokenize(tweet)

print(tokens)

['hey', '!', 'this', 'is', 'a', 'nlproc', 'tweet', ':-D']
```

Regularize common contractions:

```
import tokenizer
T = tokenizer.TweetTokenizer(regularize=True)

tweet = "Swear im gonna push this soon"
T.tokenize(tweet)

['Swear', 'I', 'am', 'going', 'to', 'push', 'this', 'soon']
```

## Reddit version

A version of the tokenizer sensitive to Reddit usernames is also provided.

```
import tokenizer
R = tokenizer.RedditTokenizer()

text = "Hey u/NLPer! This is a #NLProc message."
R.tokenize(text)

['Hey', 'u/NLPer', '!', 'This', 'is', 'a', '#NLProc', 'message', '.']
```


