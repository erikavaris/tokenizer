#testing regularization
import re

CONTRACTIONS_NEG = re.compile(r"cannot\b|\w+n't\b|shant|wont", re.I) #add cant? technically a separate word
CONTRACTIONS_FUT = re.compile(r"\b(i'll|he'll|she'll|you'll|youll|we'll)\b", re.I) #ill, hell, shell, well
# assuming "'d" is modal "should/would" for now; "had" also possible but not coded here
CONTRACTIONS_MOD = re.compile(r"\b(i'd|you'd|youd|he'd|she'd|we'd)\b", re.I) #id, hed, shed, wed
CONTRACTIONS_COPULA = re.compile(r"\b(i'm|im|you're|youre|we're|they're|theyre|he's|hes|shes|she's|it's)\b", re.I) #were, its
CONTRACTIONS_HAVE = re.compile(r"\w+'ve\b", re.I)
GOTTA = re.compile(r'\bgotta\b', re.I)
GONNA = re.compile(r'\bgonna\b', re.I)
HAFTA = re.compile(r'\bhafta\b', re.I)
WANNA = re.compile(r'\bwanna\b', re.I)

class Regularizer():
    '''Casual text regularization, for common contractions in English
    '''

    def __init__(self):
        pass

    def infinitives(self, text):
        '''Separate infinitive contractions.
        Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''

        if re.findall(GOTTA, text):
            text = re.sub(GOTTA, 'got to', text)
        if re.findall(GONNA, text):
            text = re.sub(GONNA, 'going to', text)
        if re.findall(HAFTA, text):
            text = re.sub(HAFTA, 'have to', text)
        if re.findall(WANNA, text):
            text = re.sub(WANNA, 'want to', text)

        return text

    def copula_contracts(self, text):
        '''Un-contract copulas. Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''
        cop_matches = re.findall(CONTRACTIONS_COPULA, text)
        if len(cop_matches) >= 1:
            for match in cop_matches:
                if match.lower() in ["i'm", "im"]:
                    replace_with = "I am"
                elif match.lower() in ["you're", "youre"]:
                    replace_with = "you are"
                elif match.lower() in ["they're", "theyre"]:
                    replace_with = "they are"
                elif match.lower() == "we're":
                    replace_with = "we are"
                elif match.lower() in ["hes", "shes"]:
                    replace_with = match.split("s")[0] + ' is'
                else:
                    replace_with = match.split("'")[0] + ' is'
                text = re.sub(match, replace_with, text)

        return text

    def neg_contracts(self, text):
        '''Un-contract negatives. Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''
        neg_matches = re.findall(CONTRACTIONS_NEG, text)
        if len(neg_matches) >= 1:
            # Get substrings, and replace with verb + not
            for match in neg_matches:
                if match.lower() in ["won't", "wont"]:
                    replace_with = "will not"
                elif match.lower() in ['cannot', "can't"]:
                    replace_with = 'can not'
                elif match.lower() in ["shan't", "shant"]:
                    replace_with = 'shall not'
                else:
                    splitting_neg = re.compile(r"n't", re.I)
                    replace_with = re.split(splitting_neg, match)[0] + " not"
                text = re.sub(match, replace_with, text)
        return text

    def fut_contracts(self, text):
        '''Un-contract futures. Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''
        fut_matches = re.findall(CONTRACTIONS_FUT, text)
        if len(fut_matches) >= 1:
            # Get substrings and replace with pro + will
            for match in fut_matches:
                if match.lower() == "youll":
                    replace_with = match.split("ll")[0] + ' will'
                else:
                    replace_with = match.split("'")[0] + ' will'
                text = re.sub(match, replace_with, text)
        return text

    def mod_contracts(self, text):
        '''Un-contract modals. Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''
        mod_matches = re.findall(CONTRACTIONS_MOD, text)
        if len(mod_matches) >= 1:
            # Get substrings and replace with pro + would
            for match in mod_matches:
                if match.lower() == "youd":
                    replace_with = match.split("d")[0] + ' would'
                else:
                    replace_with = match.split("'")[0] + ' would'
                text = re.sub(match, replace_with, text)

        return text

    def have_contracts(self, text):
        '''Un-contract futures. Returns text string.
        ::param text:: tweet
        ::type text:: str
        '''
        have_matches = re.findall(CONTRACTIONS_HAVE, text)
        if len(have_matches) >= 1:
            # Get substrings and replace with pro + have
            for match in have_matches:
                replace_with = match.split("'")[0] + ' have'
                text = re.sub(match, replace_with, text)
        return text

    def regularize(self, text):
        '''Simple regularization to de-contract negatives,
        futures, modals, copulas, and pluperfect.
        Returns text string
        ::param text:: tweet text
        ::type text:: str
        '''
        text = self.infinitives(text)
        text = self.neg_contracts(text)
        text = self.fut_contracts(text)
        text = self.mod_contracts(text)
        text = self.copula_contracts(text)
        text = self.have_contracts(text)

        return text
