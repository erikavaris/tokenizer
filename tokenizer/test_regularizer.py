#test regularizer
import unittest
import reg

class TestRegularizer(unittest.TestCase):

    def setUp(self):
        self.R = reg.Regularizer()

    def test_infinitives(self):
        text = 'I gotta get to the Igottaloo but hafta get home too'
        actual = self.R.infinitives(text)
        expected = "I got to get to the Igottaloo but have to get home too"
        self.assertEqual(actual, expected)

    def test_copulas(self):
        text = "I'm about to get more coffee"
        actual = self.R.copula_contracts(text)
        expected = "I am about to get more coffee"
        self.assertEqual(actual, expected)

    def test_copulas2(self):
        text = "Im about to get more coffee"
        actual = self.R.copula_contracts(text)
        expected = "I am about to get more coffee"
        self.assertEqual(actual, expected)

    def test_copulas3(self):
        text = "Hes about to get more coffee"
        actual = self.R.copula_contracts(text)
        expected = "He is about to get more coffee"
        self.assertEqual(actual, expected)

    def test_copulas4(self):
        text = "he's about to get more coffee"
        actual = self.R.copula_contracts(text)
        expected = "he is about to get more coffee"
        self.assertEqual(actual, expected)

    def test_neg(self):
        text = "I can't go"
        actual = self.R.neg_contracts(text)
        expected = "I can not go"
        self.assertEqual(actual, expected)

    def test_neg2(self):
        text = "I wont go"
        actual = self.R.neg_contracts(text)
        expected = "I will not go"
        self.assertEqual(actual, expected)

    def test_fut(self):
        text = "You'll finish soon"
        actual = self.R.fut_contracts(text)
        expected = "You will finish soon"
        self.assertEqual(actual, expected)

    def test_fut2(self):
        text = "Youll finish soon"
        actual = self.R.fut_contracts(text)
        expected = "You will finish soon"
        self.assertEqual(actual, expected)

    def test_have(self):
        text = "You've got to finish soon"
        actual = self.R.have_contracts(text)
        expected = "You have got to finish soon"
        self.assertEqual(actual, expected)

    def test_mod(self):
        text = "I'd eat that"
        actual = self.R.mod_contracts(text)
        expected = "I would eat that"
        self.assertEqual(actual, expected)

    def test_regularize(self):
        text = "I'd've eaten that"
        actual = self.R.regularize(text)
        expected = "I would have eaten that"
        self.assertEqual(actual, expected)
