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


# ###########################
# # 4.10 Sort Words by Length
# ###########################

# def sort_words_by_length(words):
#     word_length = [(len(word), word) for word in words]
#     sorted_words = sorted(word_length)
#     sorted_words = [word for (_, word) in sorted_words]
#     return sorted_words
#
# words = ['Das', 'ist', 'das', 'Haus', 'vom', 'Nikolaus']
# print(sort_words_by_length(words))

# ###########################


# #######################################
# # 4.13 Word Length and Number of Vowels
# #######################################

# Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words,
# adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains.
#
# def word_length_vowels(words):
#     word_length_vowels = [(len(word), len(re.sub(r'[^aeiou]', '', word)), word) for word in words]
#     vowel_arrs = [[] for _ in range(max(x[1] for x in word_length_vowels)+1)]
#     num_of_length = len(set([x[0] for x in word_length_vowels]))
#     word_vowels = [vowel_arrs for _ in range(num_of_length)]
#     word_vowels.append(vowel_arrs)
#
#     for length, vowels, word in word_length_vowels:
#         word_vowels[length][vowels].append(word)
#     return word_vowels
#
#
# words = nltk.corpus.brown.words(categories=['hobbies'])
# print(words[100:115])
# print(word_length_vowels(words[100:115]))

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
#     gematria_sum = sum(v for v in [letter_vals[c.lower()] for c in word])
#     return gematria_sum
#
# def find_666(text):
#     gematria_vals = [(w, gematria(w)) for w in text if re.search(r'^[a-zA-Z]+$', w)]
#     count_666 = [(w, val) for (w, val) in gematria_vals if val == 666]
#     return len(count_666), count_666
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
# print('\n The hiffen meaning of your text is: ', decode(text, brown_gematria_lexicon))

# ################


#######################################
# 4.17 Remove frequently occuring words
#######################################
#
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
#
# def built_trie(contents, trie):
#     for word, synonyms in contents:
#         for synonym in synonyms:
#             insert(trie, word, synonym)
#     return trie
#
# def lookup_word_in_lexicon(trie, word):
#     if word[0] in trie:
#         if 'value' in trie[word[0]]:
#             return ', '.join(trie[word[0]]['value'])
#         else:
#             if len(word) > 1:
#                 return lookup_word_in_lexicon(trie[word[0]], word[1:])
#             else:
#                 return "Word wasn't found in the lexicon."
#     else:
#         return "Word wasn't found in the lexicon."
#
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