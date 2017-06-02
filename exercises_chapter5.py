import nltk, re, pprint
from nltk.corpus import brown

# #######################
# # 5.11 Affix Tagger
# #######################

# help(nltk.AffixTagger)
# brown_tagged_sents = brown.tagged_sents(categories=['news', 'hobbies'])
# brown_sents = brown.sents(categories=['news', 'hobbies'])
# size = int(len(brown_tagged_sents) * 0.9)
# train_sents = brown_tagged_sents[:size]
# test_sents = brown_tagged_sents[size:]
#
# bigram_tagger = nltk.BigramTagger(train_sents)
# affix_tagger = nltk.AffixTagger(train_sents, affix_length=-3, min_stem_length=1, backoff=bigram_tagger)
#
# print(affix_tagger.tag_sents(brown_sents[0:10]))
# print(bigram_tagger.evaluate(test_sents))
# print(affix_tagger.evaluate(test_sents))

# #######################


# ###############################################
# # 5.13 String Formatting with dictonary values
# ###############################################
# from datetime import date
#
# date = {'day': date.today().day,
#         'month': date.today().month,
#         'year': date.today().year}
# print('Today is the {day}.{month}.{year}'.format(**date))
# print('Today is the {year}-{month}-{day}'.format(**date))

# ###############################################


# ###############################################
# # 5.15 String Formatting with dictonary values
# ###############################################

brown_tagged_words = brown.tagged_words()

# 1)  Nouns that are more often uses in plural than singular
# singular_nouns = [n[0] for n in brown_tagged_words if n[1] == 'NN']
# plural_nouns = [n[0] for n in brown_tagged_words if n[1] == 'NNS']
#
# cfdist = nltk.ConditionalFreqDist()
#
# for n in singular_nouns:
#     condition = 'singular'
#     cfdist[condition][n] += 1
#
# for n in plural_nouns:
#     condition = 'plural'
#     cfdist[condition][n[0:-1]] += 1
#
# more_plural = list(n for n in set(singular_nouns + plural_nouns) if cfdist['plural'][n] > cfdist['singular'][n])
# tuples = list((m+'s', cfdist['plural'][m], m, cfdist['singular'][m]) for m in more_plural)
# print(sorted(tuples, key=lambda m:m[3], reverse=True))

# 2) Word with the highest number of distinct tags
#
# cfdist = nltk.ConditionalFreqDist(set(brown_tagged_words))
#
# word_with_most_tags= sorted(((w[0], len(cfdist[w[0]].most_common())) for w in set(brown_tagged_words)), key=lambda x:x[1], reverse=True)[0]
# print(cfdist[word_with_most_tags[0]].most_common())
# nltk.help.brown_tagset()

# 3) 
# 4)

# ###############################################