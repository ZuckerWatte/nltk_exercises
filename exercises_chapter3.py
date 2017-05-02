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

# p[aeiou]{,2}t   // letter p followed by one or two vocals
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

# A single determiner(assume that a, an, and the are the only determiners).
# s = "The student has an open mind and a wild soul."
# nltk.re_show('\s?(a|A|an|An|the|The)\s', s)

# An arithmetic expression using integers, addition, and multiplication, such as 2 * 3 + 8.
# s = "The student didn't know how to calculate 3 + 4 or 45 * 2 + 12 or 3+3+3 or 444+5*9000 or 4*4."
# nltk.re_show('(\d+(\s+)?(\*|\+)(\s+)?)+\d+(\s+)?', s)

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
#     words = [w for w in re.findall(r'\w+', raw) if w.islower()]
#     unknown_words = [u for u in words if u not in nltk.corpus.words.words()]
#     print(unknown_words)

#unknown('https://en.wikipedia.org/wiki/Endoskeleton')
#unknown('http://www.azlyrics.com/lyrics/oasis/wonderwall.html')
# ##########################


# ########################
# # 3.24 hAck3r converter
# ########################
import textwrap
from nltk import word_tokenize
# e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8

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
    'e':'3',
    'i':'1',
    'o':'0',
    'l':'|',
    '\ss':' $',
    's':'5',
    '\.':'5w33t!',
    'ate':'8'
}

hacker(str, dic)
# ########################