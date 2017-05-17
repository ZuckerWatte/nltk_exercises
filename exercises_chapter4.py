import nltk, re, pprint

# #######################
# # 4.2 Tuples and Lists
# #######################

# def sequence_operations(list_or_tuple):
#     print('Sequenz:', list_or_tuple)
#     print('Sortierte Sequenz:', sorted(list_or_tuple))
#     print('Umgekehrte Reihenfolge', [x for x in reversed(list_or_tuple)])
#     print('Sequenz hat die Länge:', len(list_or_tuple))
#     print('Vereinen zweier Sequenzen', list_or_tuple + list_or_tuple)
#     print('Multiplizieren einer Sequenz:', list_or_tuple * 3)
#     print('4 appears', list.count(4), 'times')
#
#
# list = [4, 8, 2]
# tuple = (4, 8, 2)
# sequence_operations(list)
# sequence_operations(tuple)

# def list_operations(list):
#     list.append(6)
#     print('Element was adden:', list)
#     list.pop()
#     print('Last element was removed:', list)
#     list.remove(8)
#     print('Specific elment was removed:', list)
#
# list = [4, 8, 2]
# list_operations(list)
# #######################


###########################
# 4.10 Sort Words by Length
###########################
#
# def sort_words_by_length(words):
#     words.sort(key=len)
#     return words
#
# words = ['Das', 'ist', 'das', 'Haus', 'vom', 'Nikolaus']
# print(sort_words_by_length(words))

###########################


# #######################################
# # 4.13 Word Length and Number of Vowels
# #######################################

# Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words,
# adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.

# def word_length_vowels(words):
#     word_length_vowels = [(len(word), len(re.sub(r'[^aeiou]', '', word)), word) for word in words]
#     word_vowels = [[[] for _ in range(max([x[1] for x in word_length_vowels])+1)] for _ in range(max(x[0] for x in word_length_vowels)+1)]
#
#     for length, vowels, word in word_length_vowels:
#         word_vowels[length][vowels].append(word)
#     return word_vowels
#
# words = nltk.corpus.brown.words(categories=['hobbies'])
# word_vowels = word_length_vowels(words[100:115])
#
# # print word of length 5, that contan 2 vowels
# print(arr[5][2])

# #######################################


# #####################################
# # 4.14 New Words in last 10% of Text
# #####################################

# from nltk.book import *
#
# def novel10(text):
#     split = int(0.9 * len(text))
#     early_words = set(text[:split])
#     late_words = set(text[split:])
#     return [w for w in late_words if not w in early_words]
#
# moby_dick = text1
# genesis = text3
# text = nltk.word_tokenize('The new word in the last ten percent is cat')
#
# print('\n New words in last 10% of Moby Dick ({} words): \n'.format(len(moby_dick)), novel10(moby_dick))
# print('\n New words in last 10% of Genesis ({} words): \n'.format(len(genesis)), novel10(genesis))
# print('\n New words in last 10% of Testtext ({}): \n'.format(len(text)), novel10(text))

# #####################################


# ################
# # 4.16 Gematria
# ################
#
# import random
#
# letter_vals = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 80, 'g': 3,
#     'h': 8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50,
#     'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6,
#     'v':6, 'w':800, 'x':60, 'y':10, 'z':7
# }
#
# def gematria(word):
#     gematria_sum = sum(letter_vals[c.lower()] for c in word)
#     return gematria_sum
#
# def find_666(text):
#     gematria_vals = [(w, gematria(w)) for w in text if re.search(r'^[a-zA-Z]+$', w) and gematria(w) == 666]
#     return len(gematria_vals), gematria_vals
#
# def process_documents(files, corpus):
#     for file in files:
#         count_666 = find_666(corpus.words(file))
#         if count_666[0] is not 0:
#             print('\n The document {} contains {} words with the gematria number 666: {}'.format(file, count_666[0], [w for (w, _) in count_666[1]]))
#         else:
#             print('\n The document {} contains NO words with the gematria number 666.'.format(file))
#
# def built_gematria_lexicon(gematria_words):
#     gematria_lexicon = {}
#     for w, val in gematria_words:
#         if re.search(r'^[a-zA-Z]+$', w):
#             if val in gematria_lexicon:
#                 gematria_lexicon[val].append(w)
#             else:
#                 gematria_lexicon[val] = [w]
#     return gematria_lexicon
#
#
# def decode(text, gematria_lexicon, percentage=0.3):
#     replace_percentage = int(percentage * len(text))
#     replace_positions = [random.choice(range(len(text))) for _ in range(replace_percentage)]
#     gematria_vals = [(pos, gematria(text[pos])) for pos in replace_positions]
#     for pos, gem in gematria_vals:
#         if gem in gematria_lexicon:
#             gematria_equivalent = random.choice(gematria_lexicon[gem])
#             text[pos] = gematria_equivalent
#     hidden_meaning = ' '.join(text)
#     return hidden_meaning
#
# # find occurences of words with gematria number 666
# state_union_corpus = nltk.corpus.state_union
# state_union_files = nltk.corpus.state_union.fileids()
# #process_documents(state_union_files, state_union_corpus)
#
# # replace randomly words with gematria equivalent
# brown_words = set(nltk.corpus.brown.words())
# brown_words_gematria = [(w, gematria(w)) for w in brown_words if re.search(r'^[a-zA-Z]+$', w)]
# brown_gematria_lexicon = built_gematria_lexicon(brown_words_gematria)
#
# text = nltk.word_tokenize(input('\n Please enter some text: '))
# text = [t for t in text if re.search(r'^[a-zA-Z]+$', t)]
# print('\n The hidden meaning of your text is: ', decode(text, brown_gematria_lexicon))

# ################


#######################################
# 4.17 Remove frequently occuring words
#######################################

# def shorten(text, n):
#     tokens = nltk.word_tokenize(text)
#     most_common_words = nltk.FreqDist([t.lower() for t in tokens]).most_common(n)
#     shortened_tokens = []
#     for i, t in enumerate(tokens):
#         if not t.lower() in [w for (w, _) in most_common_words]:
#             shortened_tokens.append(t)
#
#     shortened_text = ' '.join(shortened_tokens)
#     return shortened_text
#
# text = input('\n  Please enter some text: ')
# print(shorten(text, 3))

#######################################


########################
# 4.18 Indexing Lexicon
########################

# from nltk.corpus import wordnet as wn
#
# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         if 'value' in trie:
#             trie['value'].append(value)
#         else:
#             trie['value'] = [value]
#
# def built_trie(contents, trie):
#     for word, synonyms in contents:
#         for synonym in synonyms:
#             insert(trie, word, synonym)
#     return trie
#
# def lookup_word_in_lexicon(trie, word):
#     if word:
#         current, rest = word[0], word[1:]
#         if current in trie:
#             return lookup_word_in_lexicon(trie[current], rest)
#         return "Word wasn't found in the lexicon."
#     else:
#         return ', '.join(trie['value'])
#
#
# synsets = wn.all_synsets('n')
# synsets_synonyms = [(syn.lemma_names()[0], syn.lemma_names()[1:]) for syn in synsets if syn.lemma_names()[1:]]
# trie = {}
# synonym_lexicon = built_trie(synsets_synonyms, trie)
#
# search = input('Search synonyms for: ')
# print('Synonyms for {} are: {}'.format(search, (lookup_word_in_lexicon(synonym_lexicon, search))))

#######################################


###################################
# 4.19 Sorting Synsets by Proximity
###################################

# from nltk.corpus import wordnet as wn
#
# def sort_synsets(target, synsets):
#     sorted_synsets = sorted([(target.shortest_path_distance(syn), syn) for syn in synsets])
#     return ', '.join([syn.name() for (_, syn) in sorted_synsets])
#
# target = wn.synset('right_whale.n.01')
# synsets = [wn.synset('minke_whale.n.01'), wn.synset('orca.n.01'), wn.synset('novel.n.01'), wn.synset('tortoise.n.01')]
# print('\n from nearest to most distant synset of {}: '.format("right_whale.n.01"), sort_synsets(target, synsets))

###################################


#############################################
# 4.21 Difference between Text and Vocabulary
#############################################

#from nltk.book import *
#print(list(w for w in set(text3[:50]).difference(set(text3[50:100]))))

#############################################


#############################################
# 4.23 Difference between Text and Vocabulary
#############################################

# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         trie['value'] = value
#
# def lookup(trie, key):
#     current = key[0]
#     if len(key)>1:
#         rest = key[1:]
#         if current not in trie:
#             return ["no results", '']
#         return lookup(trie[current], rest)
#     else:
#         if current in trie and 'value' in trie[current]:
#            return [trie[current]['value'], '']
#         return check_prefix(trie, current)
#
# def check_prefix(trie, key, str=''):
#     if key == 'value':
#         return [trie['value'], '({})'.format(str[1:])]
#     elif key in trie and len(trie[key].keys()) == 1:
#         str += key
#         next = list(trie[key].keys())[0]
#         return check_prefix(trie[key], next, str)
#     return ["no result", '']
#
#
# trie = {}
# insert(trie, 'cat', 'sweetest animal ever')
# insert(trie, 'catherine', 'sweetest girl ever')
# insert(trie, 'catering', 'sweetest service ever')
# insert(trie, 'chocolate', 'sweetest sweets ever')
#
# search = input('\nsearch dictionary for: ')
# result = lookup(trie, search)
# print('{}{}: {}'.format(search, result[1], result[0]))
#############################################


#######################
# 4.26 Catalan Numbers
#######################
# C0 = 1, and Cn+1 = Σ0..n (CiCn-i)
# 1, 1, 2, 5, 14, 42, 132, 429, 1430

# def catalan(n):
#     if n < 0:
#         return 'negative input'
#     elif n <= 1:
#         return 1
#
#     sum = 0
#     for i in range(n):
#         sum += catalan(i) * catalan(n-1-i)
#     return sum
#
# # not working yet
# def catalan_dynamic(n, lookup=[1,1]):
#     if n < 0:
#         return 'negative input'
#     sum = 0
#     if n in list(range(len(lookup))):
#         return lookup[n]
#     for i in range(n):
#         sum += catalan_dynamic(i) * catalan_dynamic(n-1-i)
#         #if i != 0 and i != 1:
#         lookup.append(sum)
#     return lookup[n]
# 
# print(catalan(7))
# print(catalan_dynamic(4))

#######################


####################
# 4.31 Justify Text
####################

# import textwrap, re
#
# def justify_text(str, width):
#     sents = textwrap.wrap(str, width=width)
#     justified_text = [add_blanks(s, width) for s in sents]
#     return justified_text
#
# def add_blanks(s, width):
#     s = s.replace(' ', '  ', width-len(s))
#     if len(s) < width:
#         return add_blanks(s, width)
#     return s
#
# str = """Yo listen up here's a story
# About a little guy that lives in a blue world
# And all day and all night and everything he sees
# Is just blue like him inside and outside
# Blue his house with a blue little window
# And a blue corvette
# And everything is blue for him and himself
# And everybody around
# 'Cause he ain't got nobody to listen to
# I'm blue da ba dee da ba die ..."""
#
# justified_text = justify_text(str, 50)
# pprint.pprint(justified_text)
####################


############################################
# 4.32 Sentences with highest Word Frequency
############################################

# from nltk.corpus import brown
#
# def word_freq_in_sents(words, sents, n):
#     total_freqdist = nltk.FreqDist([w.lower() for w in words])
#     summed_word_freq = [(sum([total_freqdist[w] for w in s]), i) for (i,s) in enumerate(sents)]
#     highest_ranked_sentences = sorted(sorted(summed_word_freq)[-n:], key=lambda x: x[1])
#     return highest_ranked_sentences
#
# words_news = brown.words(categories='news')
# sents_news = brown.sents(categories='news')
#
# highest_ranked_sentences = word_freq_in_sents(words_news, sents_news, 3)
# for sent in highest_ranked_sentences:
#     print('\nTotal Word Frequency: {}\n{}'.format(sent[0], ' '.join(sents_news[sent[1]])))

############################################


#######################
# 4.35 n x n Crosswords
#######################

# write a program to implement a brute-force algorithm for discovering word squares,
# a kind of n × n crossword in which the entry in the nth row is the same as the entry
# in the nth column.

# from nltk.corpus import words,brown
# import random
#
#
# def build_crossword(n, len_dict):
#     word = random.choice(len_dict[n])
#     crossword = [word]
#     trie = build_trie(len_dict[len(word)])
#     crossword = find_words(n, crossword, trie, 0)
#     if not crossword:
#         return build_crossword(n, len_dict)
#     return crossword
#
# def find_words(n, crossword, trie, c):
#     if c < 10:
#         c += 1
#     else:
#         return False
#     for i in range(1,n):
#         char = crossword[0][i]
#         for j in range(1, i):
#             char += crossword[j][i]
#         next_word = lookup(trie, char)
#         if not next_word:
#             return find_words(n, [crossword[0]], trie, c)
#         crossword.append(next_word)
#     return crossword
#
# def build_len_dict(corpus):
#     len_dict = {}
#     len_words = [(len(w), w) for w in corpus]
#     for length, word in len_words:
#         if length in len_dict:
#             len_dict[length].append(word)
#         else:
#             len_dict[length] = [word]
#     return len_dict
#
# def build_trie(words):
#     trie = {}
#     for w in words:
#         insert(trie, w, w)
#     return trie
#
# def insert(trie, key, value):
#     if key:
#         first, rest = key[0], key[1:]
#         if first not in trie:
#             trie[first] = {}
#         insert(trie[first], rest, value)
#     else:
#         trie['word'] = value
#
# def lookup(trie, word):
#     if word:
#         current, rest = word[0], word[1:]
#         if current in trie:
#             return lookup(trie[current], rest)
#         return False
#     else:
#         if not 'word' in trie:
#             next = random.choice(list(trie.keys()))
#             return lookup(trie, next)
#         return trie['word']
#
#
# brown_words = [w.lower() for w in list(set(brown.words())) if len(w) <= 10 and re.search(r'^[a-zA-Z]+$', w)]
# words_words = [w.lower() for w in list(set(words.words())) if len(w) <= 10 and re.search(r'^[a-zA-Z]+$', w)]
# corpus = list(set().union(*[set(brown_words), set(words_words)]))
# len_dict = build_len_dict(corpus)
#
# pprint.pprint(build_crossword(5, len_dict), width=5)

#######################