import nltk, re, pprint

# ######################
# # 3.6 String Regex
# ######################

# [a-zA-Z]+   // all Strings with one or multiple characters from a to z, not case sensitive
# s = "This IS a SiMpLe STRing"
# nltk.re_show('[a-zA-Z]+', s)

# [A-Z][a-z]*   // all capital letters from A to Z followed bei none or multiple lowercase characters from a to z
# s = "This IS a SiMpLe STRing"
# nltk.re_show('[A-Z][a-z]*', s)

# p[aeiou]{,2}t   // letter p followed by one or two vocals ending with a t
# s = "This IS a SiMpLe pt piet put puut puuut"
# nltk.re_show('p[aeiou]{,2}t', s)

# \d+(\.\d+)?  // one or multiple digits followed by . followed by zero, one or multiple digits --> float numbers and integers
# s = "These are float numbers: 9.9, 1.23, 56.444, those are an integer: 9, 10"
# nltk.re_show('\d+(\.\d+)?', s)

# ([^aeiou][aeiou][^aeiou])*   // zero or multiple times: a consonant followed by vocal followed by a consonant
# s = "tut taat tiet nun nan mmm mmi imm"
# nltk.re_show('([^aeiou][aeiou][^aeiou])*', s)

# \w+|[^\w\s]+   // one or multiple alphanumeric characters without whitespace characters
# s = "tut taat\t tiet nun nan\n mmm       mmi imm A 7\n  "
# nltk.re_show('\w+|[^\w\s]+', s)
# ######################


# ######################
# # 3.7 String Regex
# ######################
from nltk import word_tokenize

# A single determiner(assume that a, an, and the are the only determiners).
# s = "The student has an open mind and a wild soul."
# tokens = word_tokenize(s)
# [nltk.re_show('^(a|A|an|An|the|The)$', t) for t in tokens]


# An arithmetic expression using integers, addition, and multiplication, such as 2 * 3 + 8.
# s = "The student didn't know how to calculate 3 + 4 or 45 * 2 + 12 or 3+3+3 or 444+5*9000 or 4*4."
# nltk.re_show('(\d+(\s+)?(\*|\+)(\s+)?)+\d+', s)
# ######################


# ###############################
# # 3.20 Access Text from Website
# ###############################
# from nltk import word_tokenize
# import urllib
# from bs4 import BeautifulSoup
# import ssl
#
# def weather(plz, city):
#     ssl._create_default_https_context = ssl._create_unverified_context
#     url = urllib.parse.quote(u'https://www.br.de/wettervorhersage/wetterprognose/{}/{}'.format(str(plz), city, end=' '), safe=':/')
#     html = urllib.request.urlopen(url).read().decode('utf8')
#     raw = BeautifulSoup(html, "html.parser").get_text()
#     tokens = word_tokenize(raw)
#     relevant_token = tokens.index("Aktuell")
#     tokens = tokens[relevant_token:relevant_token+15]
#     text = ' '.join(tokens)
#     text = text.replace(' :', ':')
#     print("\nDas Wetter in {}: \n{}\n".format(city, text, end=' '))
#
# weather(83395, 'Freilassing')
# weather(87700, 'Memmingen')
# weather(80333, 'München')
# ###############################


# ##########################
# # 3.21 Find unknown Words
# ##########################
# import urllib
# from bs4 import BeautifulSoup
# import ssl
#
# def unknown(url):
#     ssl._create_default_https_context = ssl._create_unverified_context
#     url = urllib.parse.quote(url, safe=':/')
#     html = urllib.request.urlopen(url).read().decode('utf8')
#     soup = BeautifulSoup(html, "html.parser")
#     for script in soup(["script", "style"]):
#         script.decompose()  # clean from script and style tags
#     raw = soup.get_text()
#     words = [w for w in nltk.word_tokenize(raw) if re.search(r'^[a-zA-Z]+$', w)]
#     known_words = nltk.corpus.words.words()
#     unknown_words = [u.lower() for u in words if u not in known_words]
#     unknown_words = sorted(set(unknown_words))
#     return unknown_words
#
# print(unknown('https://en.wikipedia.org/wiki/Endoskeleton'))
# print(unknown('http://www.azlyrics.com/lyrics/oasis/wonderwall.html'))
# print(unknown('http://haribo.de'))
# ##########################


# ########################
# # 3.24 hAck3r converter
# ########################
import textwrap
from nltk import word_tokenize
# # e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8
#
def hacker(str, dic):
    tokens = word_tokenize(str)
    tokens = [t.lower() for t in tokens]
    text = ' '.join(tokens)
    for regex, replacement in dic.items():
        text = re.sub(r'{}'.format(regex), replacement, text)
    print(textwrap.fill(text, 50))

str = """Yo listen up here's a story
About a little guy that lives in a blue world
And all day and all night and everything he sees
Is just blue like him inside and outside
Blue his house with a blue little window
And a blue corvette
And everything is blue for him and himself
And everybody around
'Cause he ain't got nobody to listen to
I'm blue da ba dee da ba die ..."""

dic = {
    'ate': '8',
    'e':'3',
    'i':'1',
    'o':'0',
    'l':'|',
    '(^s|\ss)':' $',
    's':'5',
    '\.':'5w33t!'
}

hacker('Sorry for being late!', dic)
hacker(str, dic)
# ########################


# #############################
# # 3.30 Normalization/Stemming
# #############################
# from nltk import word_tokenize
# porter = nltk.PorterStemmer()
# lancaster = nltk.LancasterStemmer()
#
# def porter_stemmer(str):
#     tokens = word_tokenize(str)
#     tokens = [t.lower() for t in tokens]
#     porter_tokens = [porter.stem(t) for t in tokens]
#     print(porter_tokens)
#
# def lancaster_stemmer(str):
#     tokens = word_tokenize(str)
#     tokens = [t.lower() for t in tokens]
#     lancaster_tokens = [lancaster.stem(t) for t in tokens]
#     print(lancaster_tokens)
#
# str = """Finally someone let me out of my cage
# Now time for me is nothing cause I'm counting no age
# Now I couldn't be there now you shouldn't be scared
# I'm good at repairs and I'm under each snare
# Intangible, I bet you didn't think so
# I command you to, panoramic view you
# Look I'll make it all manageable
# Pick and choose, sit and lose
# All you different crews
# Chicks and dudes, who you think is really kicking tunes"""
#
# porter_stemmer(str)
# lancaster_stemmer(str)
# #############################


# ####################################
# # 3.34 Adjectives to Nouns Converter
# ####################################
# def adj_to_noun(adjs):
#     adj_nouns = {}
#     for adj in adjs:
#         noun = re.sub(r'an$', 'a', adj)
#         noun = re.sub(r'ian$', 'ia', noun)
#         adj_nouns[adj] = noun
#
#     for adj, noun in adj_nouns.items():
#         print(adj, ': ', noun)
#
# nationality_adjs = ['African', 'American', 'Asian', 'Australian', 'Bavarian', 'Bulgarian', 'Canadian', 'Mexican', 'Romanian', 'South American']
# adj_to_noun(nationality_adjs)
# ####################################


# ############################
# # 3.38 Hyphens at linebreaks
# ############################
# from nltk import word_tokenize
#
# # A) Write a regular expression that identifies words that are hyphenated at a line-break.
# s = """My hus-
# band is fifty-
# six years old and my son-in-
# law is twenty-two."""
# nltk.re_show('(\w+-)+\n\w+', s)
# hypenated_linebreak_words = [''.join(w) for w in re.findall(r'(\w+-)*(\w+-)(\n\w+)',s)]
# print(hypenated_linebreak_words)
#
# # B) Use re.sub() to remove the \n character from these words.
# hypenated_words = [re.sub(r'\n', '', w) for w in hypenated_linebreak_words]
# print(hypenated_words)
#
# # C) How might you identify words that should not remain hyphenated once the newline is removed
# non_hyphen_words = [re.sub(r'-', '', w) for  w in hypenated_words if re.sub(r'-', '', w) in nltk.corpus.words.words()]
# normal_words = [w for  w in hypenated_words if re.sub(r'-', '', w) not in nltk.corpus.words.words()] + non_hyphen_words
# print(normal_words)
# ############################


# #########################
# # 3.39 Soundex Algorithm
# #########################
# from nltk import word_tokenize
#
# def soundex(str, dic_letters, dic_digits):
#     soundex = ''
#     tokens = word_tokenize(str)
#     for token in tokens:
#         first = token[0]
#         for regex, replacement in dic_letters.items():
#             token = re.sub(r'{}'.format(regex), replacement, token)
#         for regex, replacement in dic_digits.items():
#             token = re.sub(r'{}'.format(regex), replacement, token)
#         token = re.sub(r'(?!^)[aeiouy]', '', token)
#         token = re.sub(r'^.{1}', first, token)
#         while len(token) < 4:
#             token = token + '0'
#         if len(token) > 4:
#             token = token[:4]
#         soundex += ' ' + token
#     print(str)
#     print(soundex)
#
# dic_letters = {
#     '[hwHW]':'',
#     '[bfpvBFPV]':'1',
#     '[cgjkqsxzCGJKQSXZ]':'2',
#     '[dtDT]':'3',
#     '[lL]':'4',
#     '[mnMN]':'5',
#     '[rR]':'6'
# }
#
# dic_digits = {
#     '11+':'1',
#     '22+':'2',
#     '33+':'3',
#     '44+':'4',
#     '55+':'5',
#     '66+':'6'
# }
#
# str = "Robert Ashcraft and Rupert Tymczak and Rubin Pfister"
# soundex(str, dic_letters, dic_digits)
# #########################


# ################################
# # 3.41 Nested List Comprehension
# ################################
# words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
# vsequences = set()
# for word in words:
#     vowels = []
#     for char in word:
#         if char in 'aeiou':
#             vowels.append(char)
#     vsequences.add(''.join(vowels))
# print(sorted(vsequences))
#
# s = sorted(set([''.join([c for c in w if c in 'aeiou']) for w in words]))
# print(s)
# ################################