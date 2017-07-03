import unittest
import tokenizer


class TestTokenizerDefaults(unittest.TestCase):

    def setUp(self):
        self.T = tokenizer.TweetTokenizer()
        self.redditT = tokenizer.RedditTokenizer()

    def test_emoticon(self):
        text = 'this is a tweet with kitty =^^= emoticon'
        actual = self.T.tokenize(text)
        expected = ['this', 'is', 'a', 'tweet', 'with', 'kitty', '=^^=', 'emoticon']
        self.assertEqual(actual, expected)

    def test_url(self):
        text = 'this is a url https://t.co/1234_MOD tweet'
        actual = self.T.tokenize(text)
        expected = ['this', 'is', 'a', 'url', 'https://t.co/1234_MOD', 'tweet']
        self.assertEqual(actual, expected)

    def test_hashtag(self):
        text = 'this is a #hash_tag tweet'
        actual = self.T.tokenize(text)
        expected = ['this', 'is', 'a', '#hash_tag', 'tweet']
        self.assertEqual(actual, expected)

    def test_phone(self):
        text = 'this has a phone (323) 123-4567 number in it'
        actual = self.T.tokenize(text)
        expected = ['this', 'has', 'a', 'phone', '(323) 123-4567', 'number', 'in', 'it']
        self.assertEqual(actual, expected)

    def test_email(self):
        text = 'this has an email@email.com in it'
        actual = self.T.tokenize(text)
        expected = ['this', 'has', 'an', 'email@email.com', 'in', 'it']
        self.assertEqual(actual, expected)

    def test_arrow(self):
        text = 'a tweet with an --> arrow'
        actual = self.T.tokenize(text)
        expected = ['a', 'tweet', 'with', 'an', '-->', 'arrow']
        self.assertEqual(actual, expected)

    def test_handle(self):
        text = 'a tweet at @some_handle somewhere'
        actual = self.T.tokenize(text)
        expected = ['a', 'tweet', 'at', '@some_handle', 'somewhere']
        self.assertEqual(actual, expected)

    def test_reddit_user(self):
        text = "reddit with user u/reddit-name mention"
        actual = self.redditT.tokenize(text)
        expected = ['reddit', 'with', 'user', 'u/reddit-name', 'mention']
        self.assertEqual(actual, expected)

    def test_reddit_subreddit(self):
        text = "reddit with r/subreddit mention"
        actual = self.redditT.tokenize(text)
        expected = ['reddit', 'with', 'r/subreddit', 'mention']
        self.assertEqual(actual, expected)

class TestTokenizerRegularizations(unittest.TestCase):

    def test_hash_removal(self):
        T = tokenizer.TweetTokenizer(preserve_hashes=False)
        text = 'this has #hash_tag and # separately'
        actual = T.tokenize(text)
        expected = ['this', 'has', 'hash_tag', 'and', '#', 'separately']
        self.assertEqual(actual, expected)

    def test_handle_removal(self):
        T = tokenizer.TweetTokenizer(preserve_handles=False)
        text = '@somehandle a tweet at that person'
        actual = T.tokenize(text)
        expected = ['a', 'tweet', 'at', 'that', 'person']
        self.assertEqual(actual, expected)

    def test_url_removal(self):
        T = tokenizer.TweetTokenizer(preserve_url=False)
        text = 'this is a url https://t.co/1234_MOD tweet'
        actual = T.tokenize(text)
        expected = ['this', 'is', 'a', 'url', 'tweet']
        self.assertEqual(actual, expected)

    def test_case_lowering(self):
        T = tokenizer.TweetTokenizer(preserve_case=False)
        text = 'This is a tweet with Upper Cases and :-D emoticon' #make sure it doesn't lower case the emoticon
        actual = T.tokenize(text)
        expected = ['this', 'is', 'a', 'tweet', 'with', 'upper', 'cases', 'and', ':-D', 'emoticon']
        self.assertEqual(actual, expected)

    def test_shortening(self):
        T = tokenizer.TweetTokenizer(preserve_len=False)
        text = 'This is a loooooong tweettttt'
        actual = T.tokenize(text)
        expected = ['This', 'is', 'a', 'looong', 'tweettt']
        self.assertEqual(actual, expected)

    def test_regularization(self):
        T = tokenizer.TweetTokenizer(regularize=True)
        text = "I'd've had to figure this out"
        actual = T.tokenize(text)
        expected = ['I', 'would', 'have', 'had', 'to', 'figure', 'this', 'out']
        self.assertEqual(actual, expected)

    def test_emoji(self):
        T = tokenizer.TweetTokenizer(preserve_emoji=False)
        text = "This is a tweet with😊" #no space between text and emoji
        actual = T.tokenize(text)
        expected = ['This', 'is', 'a', 'tweet', 'with']
        self.assertEqual(actual, expected)


