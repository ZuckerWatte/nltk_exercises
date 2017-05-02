import nltk

# #################
# # 2.23 Zipf's Law
# #################
# from nltk.book import *
# import matplotlib.pyplot as plt
# import random
#
# def zipfs_plot(texts):
#     for text in texts:
#         freqdist = FreqDist(text)
#         most_common = freqdist.most_common(200)
#         print(most_common)
#         plt.plot([x[1] for x in most_common], range(1,201))
#         #plt.xscale('log')
#     plt.show()
#
# def random_string():
#     string = ''
#     for i in range(50000):
#         string += random.choice("abcdefghijk ")
#     print(string)
#     tokens = [t for t in string.split(' ') if not t == '']
#     return tokens
#
# #zipfs_plot([text1, text2, text3])
# zipfs_plot([text1])
# zipfs_plot([random_string()])
# #################


# #####################
# ## 2.25 find language
# #####################
# from nltk.corpus import udhr
#
# def find_languages(string):
#     languages = [l for l in udhr.fileids() if 'Latin1' in l]
#     languages_for_str = list()
#     for lang in languages:
#         if string.lower() in [w.lower() for w in udhr.words(lang)]:
#             languages_for_str.append(lang)
#     return languages_for_str
#
# print(find_languages('the'))

# #####################


# ###############################################
# # 2.26 branching factor noun hypernym hierarchy
# ###############################################
# from nltk.corpus import wordnet as wn
# all_synsets = wn.all_synsets('n')
#
# def average_hyponyms(sum_hyponyms, counter, synsets):
#     for synset in synsets:
#         counter += 1
#         sum_hyponyms += len(synset.hyponyms())
#     return [sum_hyponyms, counter]
#
#
# average = average_hyponyms(0, 0, all_synsets)
# print(average[0]/average[1])
# ################################################


# ########################
# ## 2.27 average polysemy
# ########################
# from nltk.corpus import wordnet as wn
#
# def average_polysemy(kind):
#     all_synsets = wn.all_synsets(kind)
#     average = polysemies(all_synsets, 0, 0, kind)
#     print(average)
#     print(average[0] / average[1])
#
# def polysemies(synsets, sum_polysemies, counter, kind):
#     for synset in synsets:
#         for name in synset.lemma_names():
#             counter += 1
#             sum_polysemies += len(wn.synsets(name, kind))
#     return [sum_polysemies, counter]
#
# average_polysemy('n')
# average_polysemy('v')
# average_polysemy('a')
# average_polysemy('r')
# ########################


# ######################
# # 2.28 word similarity
# ######################
# from nltk.corpus import wordnet as wn
#
# def path_similarity(word_pairs, dict):
#     for word_pair in word_pairs:
#         first = wn.synset('{0}.n.01'.format(word_pair[0]))
#         second = wn.synset('{0}.n.01'.format(word_pair[1]))
#         sim = first.path_similarity(second)
#         dict[word_pair] =  sim
#     sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
#     print([x[0][0] + ' - ' + x[0][1] + ': ' + str(x[1]) for x in sorted_dict])
#
#
# word_pairs = [('car', 'automobile'), ('gem', 'jewel'), ('journey', 'voyage'), ('boy', 'lad'), ('coast', 'shore'),
#                  ('asylum', 'madhouse'), ('magician', 'wizard'), ('midday', 'noon'), ('furnace', 'stove'), ('food', 'fruit'),
#                  ('bird', 'cock'), ('bird', 'crane'), ('tool', 'implement'), ('brother', 'monk'), ('lad', 'brother'),
#                  ('crane', 'implement'), ('journey', 'car'), ('monk', 'oracle'), ('cemetery', 'woodland'), ('food', 'rooster'),
#                  ('coast', 'hill'), ('forest', 'graveyard'), ('shore', 'woodland'), ('monk', 'slave'), ('coast', 'forest'),
#                  ('lad', 'wizard'), ('chord', 'smile'), ('glass', 'magician'), ('rooster', 'voyage'), ('noon', 'string')]
# path_similarity(word_pairs, {})
# ######################
