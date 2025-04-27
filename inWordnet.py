# Гипонимы, синонимы, антнимы, геперонимы
# с улучшенными характеристиками
# Каширин И.Ю. 22.12.2024

# Обязательно Подключение функций из инструментария Translate

################################################################################
#
# Вычисление всех возможных гипонимов по всем направлениям

def Get_hyponyms_wordnet(word):
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  # Recursively find all hyponyms of a given synset
  def get_vehicle_words(synset):
    vehicle_words = set()
    # Add the lemmas of the current synset to the set
    for lemma in synset.lemmas():
        vehicle_words.add(lemma.name().replace('_', ' '))
    # Recursively add the lemmas of the hyponyms
    for hyponym in synset.hyponyms():
        vehicle_words.update(get_vehicle_words(hyponym))
    return vehicle_words

  s = word+".n.01"
  #print (s)
  # Start with a list of synsets that correspond to word
  try: wn.synset( s )
  except: return []

  initial_vehicle_synsets = [
      wn.synset( s )
    ]

  # Use a set to avoid duplicates
  all_vehicle_words = set()
  for synset in initial_vehicle_synsets:
     all_vehicle_words.update(get_vehicle_words(synset))
     all_vehicle_words_list = sorted(all_vehicle_words)
  return   all_vehicle_words_list


##################################################################################
#*********************************************************************************
# Вычисление всех возможных гипернимов по всем направлениям (синонимам)

def Get_hypernyms_wordnet(word):
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  # Recursively find all hypernyms of a given synset
  def get_vehicle_words(synset):
    vehicle_words = set()
    # Add the lemmas of the current synset to the set
    for lemma in synset.lemmas():
        vehicle_words.add(lemma.name().replace('_', ' '))
    # Recursively add the lemmas of the hypernyms
    for hypernym in synset.hypernyms():
        vehicle_words.update(get_vehicle_words(hypernym))
    return vehicle_words

  s = word+".n.01"

  # Start with a list of synsets that correspond to word
  try: wn.synset( s )
  except: return []

  initial_vehicle_synsets = [
      wn.synset( s )
    ]

  # Use a set to avoid duplicates
  all_vehicle_words = set()
  for synset in initial_vehicle_synsets:
     all_vehicle_words.update(get_vehicle_words(synset))
     all_vehicle_words_list = sorted(all_vehicle_words)
  return   all_vehicle_words_list

#************************************************************************************
#************************************************************************************
# Вычисление одного гипернима уровнем выше

def Get_hypernym_wordnet(word):
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  # Recursively find all hypernyms of a given synset
  def get_vehicle_words(synset):
    result = []
    vehicle_words = set()
    # Add the lemmas of the current synset to the set
    for lemma in synset.lemmas():
        vehicle_words.add(lemma.name().replace('_', ' '))
    # Recursively add the lemmas of the hypernyms
    for hypernym in synset.hypernyms():
        result.append(hypernym.name()[:-5])
        vehicle_words.update(get_vehicle_words(hypernym))
        #break
    #print('res=', result)
    return result                          #(vehicle_words)

  s = word+".n.01"
  #print (s)
  # Start with a list of synsets that correspond to word
  try: wn.synset( s )
  except: return []

  return(get_vehicle_words(wn.synset(s))[0])


  initial_vehicle_synsets = [
      wn.synset( s )
    ]

  # Use a set to avoid duplicates
  all_vehicle_words = set()
  for synset in initial_vehicle_synsets:
     all_vehicle_words.update(get_vehicle_words(synset))
     break
     all_vehicle_words_list = sorted(all_vehicle_words)
  #return   all_vehicle_words_list
  return   all_vehicle_words


######################################################################################
######################################################################################
# Вычисление всей цепочки прямых гипернимов вверх вплоть до понятия "Сущность"

def Get_Hypernyms_wordnet(word):
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  result = []
  def get_vehicle_words(synset):

    vehicle_words = set()
    # Add the lemmas of the current synset to the set
    for lemma in synset.lemmas():
        vehicle_words.add(lemma.name().replace('_', ' '))
    # Recursively add the lemmas of the hyponyms
    for hypernym in synset.hypernyms():
        #print(hypernym.name()[:-5])
        result.append(hypernym.name()[:-5].replace('_', ' '))
        vehicle_words.update(get_vehicle_words(hypernym))

    return result

  s = word+".n.01"
  #print (s)
  # Start with a list of synsets that correspond to word
  try: wn.synset( s )
  except: return []

  return(get_vehicle_words(wn.synset(s)))

################################################################################
#
# Вычисление одного уроовня гипонимов
def get_lhyponyms_wordnet(word):
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  # Recursively find all hyponyms of a given synset
  def get_vehicle_words(synset):
    vehicle_words = set()
    # Add the lemmas of the current synset to the set
    for lemma in synset.lemmas():
        vehicle_words.add(lemma.name().replace('_', ' '))
    # Recursively add the lemmas of the hyponyms
    for hyponym in synset.hyponyms():
        #print (hyponym.name()[0:-5].replace('_', ' '))
        vehicle_words.add(hyponym.name()[0:-5].replace('_', ' '))
        #vehicle_words.update(get_vehicle_words(hyponym))
    return vehicle_words

  s = word+".n.01"
  #print (s)
  # Start with a list of synsets that correspond to word
  try: wn.synset( s )
  except: return []

  initial_vehicle_synsets = [
      wn.synset( s )
    ]

  # Use a set to avoid duplicates
  all_vehicle_words = set()
  for synset in initial_vehicle_synsets:
     all_vehicle_words.update(get_vehicle_words(synset))
     all_vehicle_words_list = sorted(all_vehicle_words)
  return   all_vehicle_words_list

####################################################################################
#             Получение сининимов и антонимов первого уровня
#
def Get_SymAnt_wordnet(word):
  import nltk
  from nltk.corpus import wordnet
  synonyms = []
  antonyms = []

  for syn in wordnet.synsets(word):
	  for l in syn.lemmas():
		  synonyms.append(l.name().replace('_', ' '))
		  if l.antonyms():
			  antonyms.append(l.antonyms()[0].name().replace('_', ' '))
  return synonyms, antonyms

#################################################################################
#            Вычисление синонимов по уровню семантического сходства
#                      (медленная процедура)
def syn(word, lch_threshold=3.0):
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)
    res = []
    for net1 in wn.synsets(word):
        for net2 in wn.all_synsets():
            try:
                lch = net1.lch_similarity(net2)
            except:
                continue
            # The value to compare the LCH to was found empirically.
            # (The value is very application dependent. Experiment!)
            if lch >= lch_threshold:
              if not net1.name()[0:-5] == word:
                #yield (net1.name()[0:-5], net2, lch)
                res.append(net1.name()[0:-5].replace('_',' '))
    return res

'''Synonym generator using NLTK WordNet Interface: http://www.nltk.org/howto/wordnet.html
    'ss': synset
    'hyp': hyponym
    'sim': similar to
    'ant': antonym
    'also' also see

'''

def get_all_synsets(word, pos=None):
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)

    res = set()
    for ss in wn.synsets(word):
      if ss.pos() == pos or pos == None:
        for lemma in ss.lemma_names():
             res.add(lemma.replace('_',' '))
            #yield (lemma, ss.name())
    return res

def get_all_hyponyms(word, pos=None):
    from nltk.corpus import wordnet as wn
    res = set()
    for ss in wn.synsets(word, pos=None):
      if ss.pos() == pos or pos == None:
            for hyp in ss.hyponyms():
                for lemma in hyp.lemma_names():
                  res.add(lemma.replace('_',' '))
                    #yield (lemma, hyp.name())
    return res

def get_all_similar_tos(word, pos=None):
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)
    res = set()
    for ss in wn.synsets(word):
      if ss.pos() == pos or pos == None:
            for sim in ss.similar_tos():
                for lemma in sim.lemma_names():
                  res.add(lemma.replace('_',' '))
                    #yield (lemma, sim.name())
    return res

def get_all_antonyms(word, pos=None):
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)
    res = set()
    for ss in wn.synsets(word, pos=None):
      if ss.pos() == pos or pos == None:
        for sslema in ss.lemmas():
           for lemma in sslema.antonyms():
              res.add(lemma.name().replace('_',' '))
                    #yield (antlemma.name(), antlemma.synset().name())
    return res

def get_all_also_sees(word, pos=None):
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)
    res = set()
    for ss in wn.synsets(word):
      if ss.pos() == pos or pos == None:
            for also in ss.also_sees():
                for lemma in also.lemma_names():
                  res.add(lemma.replace('_',' '))
                    #yield (lemma, also.name())
    return res


def print_all_synonyms(word, pos=None):
    from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
    import nltk
    from nltk.corpus import wordnet as wn
    nltk.download('wordnet', quiet=True)
    from deep_translator import GoogleTranslator
    print ("{:<25}{:<35}{:<15}".format('English word', "Русский перевод", 'Вид ассоциации'))
    print('-'*120)

    for x in get_all_synsets(word, 'n'):
      #print(x, to_rus(x), 'synonym')
      print ("{:<25}{:<35}{:<15}".format(x, to_rus(x), 'synonym'))
    print('-'*120)
    for x in get_all_hyponyms(word, 'v'):
        #print(x, to_rus(x), 'hyponym')
        print ("{:<25}{:<35}{:<15}".format(x, to_rus(x), 'hyponym'))
    print('-'*120)
    for x in get_all_similar_tos(word, pos):
        #print(x, to_rus(x), 'sim')
        print ("{:<25}{:<35}{:<15}".format(x, to_rus(x), 'sim'))

    print('-'*120)
    for x in get_all_antonyms(word, pos):
        #print(x, to_rus(x), 'antonym')
        print ("{:<25}{:<35}{:<15}".format(x, to_rus(x), 'antonym'))
    print('-'*120)
    for x in get_all_also_sees(word, pos):
        #print(x, to_rus(x), 'also')
        print ("{:<25}{:<35}{:<15}".format(x, to_rus(x), 'also'))

# Проверка
#print_all_synonyms('attack')