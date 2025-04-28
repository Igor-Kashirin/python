#********************************** РАБОТА С WORDNET **********************************
#                                                                                     *
#              Отладчик можно найти в файле WordNetSynonymsStabilVers.ipynb           *
#                                                                                     *
#**************************************************************************************
#

#  Получение наиболее вероятной "леммы" из WordNet. Не всегда идеально.

# Слова, схожие по словообразованию
# Возвращает список потенциально связанных слов по словообразованию
# (не гарантирует, что это именно derivationally related forms).
# Удаление дублей из списка
def dublicate_delete(list):
  temp = []
  for x in list:
    if x not in temp:
       temp.append(x)
  return  temp


def get_wordnet_lemma(word):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  nltk.download('wordnet', quiet=True)

  from nltk.corpus import wordnet
  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer



  lemmatizer = WordNetLemmatizer()
  synsets = wordnet.synsets(word)
  if synsets:
        # Выбираем первый синсет (может быть улучшено с помощью более сложной логики выбора)
        lemma = synsets[0].lemmas()[0].name()
        return lemma
  else:
        return None # Слово не найдено в WordNet

# Получение синонимов с помощью WordNet с параметром "не переводить для скорости"
def get_synonyms_wordnet(word, translate = 0): # return (synonyms, result_rus)
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  nltk.download('wordnet', quiet=True)

  from nltk.corpus import wordnet
  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer



  lemmatizer = WordNetLemmatizer()
  synonyms = []
  result_rus = []
  synsets = wordnet.synsets(word)
  if not synsets:
    return 0,0

  for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

  # result: the list of synonyms
  synonyms = dublicate_delete(synonyms)
  synonyms = replace_char(synonyms, '_', ' ')
  if translate:
     result = listTranslateToRus(synonyms)
     result_rus = remove_words_with_chars(result, "a-zA-Z_")
     result_rus = dublicate_delete(result_rus)
  
  return (synonyms, result_rus)




# Recursively find all hyponyms of a given synset


def Get_hyponyms_wordnet(word):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
  from io import StringIO
  import sys

  save_stdout = sys.stdout
  result = StringIO()
  sys.stdout = result
  
  import nltk
  from nltk.corpus import wordnet as wn

  nltk.download('wordnet', quiet=True)
  nltk.download('omw-1.4', quiet=True) # Linux
  
  sys.stdout = save_stdout
  
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

# Получение гипернимов с помощью WordNet
def get_hypernyms_wordnet(word, language = 'en'):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  nltk.download('wordnet', quiet=True)

  from nltk.corpus import wordnet
  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer
  
  from nltk.corpus import wordnet as wn


  res = ''
  list_ = []
  rus = []
  s = ''

  for ss in wn.synsets(word):
     t = ss.hypernyms()
     for s_ in t:
       list_.append(s_.name())
  #print(list_)
  total = list()
  for el in list_:
   s = el

   if '.n.01' in s:
     start = s.find('\'') + 1   # +1 чтобы не включать сам символ [
     end = s.rfind('.n')        # rfind возвращает позицию с конца строки
     substring = s[start:end]

     #print(substring)
     if substring.find(".") != -1:
        list_ = substring.split(".")


     substring = substring.replace('_',' ')
     total.append(substring)
  if language == 'ru': rus = listTranslateToRus(total)
  return(total, rus)

# Получение гипонимов с помощью WordNet
def get_hyponyms_wordnet(word, language = 'en'):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  from nltk.corpus import wordnet as wn
  nltk.download('wordnet', quiet=True)
  nltk.download('omw-1.4', quiet=True) # Linux

  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer


  res = ''
  list_ = []
  rus = []
  s = ''

  for ss in wn.synsets(word):
     t = ss.hyponyms()
     for s_ in t:
       list_.append(s_.name())
  #print(list_)
  total = list()
  for el in list_:
   s = el

   if '.n.01' in s:
     start = s.find('\'') + 1   # +1 чтобы не включать сам символ [
     end = s.rfind('.n')        # rfind возвращает позицию с конца строки
     substring = s[start:end]

     #print(substring)
     if substring.find(".") != -1:
        list_ = substring.split(".")


     substring = substring.replace('_',' ')
     total.append(substring)
  if language == 'ru': rus = listTranslateToRus(total)
  return(total, rus)


# Замена в списке слов с символом char_to_replace на слова с символом replacement
def replace_char(word_list, char_to_replace, replacement):
    return [re.sub(r"{}+".format(re.escape(char_to_replace)), replacement, word) for word in word_list]


def get_potential_derivationally_related(word, translate = 0):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  nltk.download('wordnet', quiet=True)

  from nltk.corpus import wordnet
  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer



  lemmatizer = WordNetLemmatizer()
  related_forms = set()
  result_rus = []                              # Можетбыть set() ?
  for synset in wordnet.synsets(word):
      for lemma in synset.lemmas():
          related_forms.add(lemma.name())
          # Попытка получить производные формы (не гарантирует корректность):
          related_forms.add(lemmatizer.lemmatize(lemma.name(), pos='n')) # Существительные
          related_forms.add(lemmatizer.lemmatize(lemma.name(), pos='v')) # Глаголы
          related_forms.add(lemmatizer.lemmatize(lemma.name(), pos='a')) # Прилагательные
          related_forms.add(lemmatizer.lemmatize(lemma.name(), pos='r')) # Наречия

  related_forms = dublicate_delete(related_forms)
  related_forms = replace_char(related_forms, '_', ' ')
  if translate:
     result = listTranslateToRus(related_forms)
     result_rus = remove_words_with_chars(result, "a-zA-Z_")
     result_rus = dublicate_delete(result_rus)
  return related_forms, result_rus
  #return list(related_forms)

#
# Преобразование глагола в список однокоренных существительных
# Вход:   Исходный глагол/деепричастие
# Выход:  Список существительных
#
def verb_to_nouns(verb_word, translate = 0):
  from itranString import (
                          to_eng, to_rus, extract_alphabetic_words, listTranslateToRus,
                          AttrDictToString, remove_words_with_chars, remove_latin_words_regex,
                          replace_char, dublicate_delete )
 
  import nltk
  nltk.download('wordnet', quiet=True)

  from nltk.corpus import wordnet
  from nltk.stem import WordNetLemmatizer
  import sys 

  if sys.version_info >= (3, 0): 
    import re
  else:
    import regex as re

  nltk.download('omw-1.4', quiet=True) # Обязательно для WordNetLemmatizer

  verb_word = verb_word.lower()

  lemmatizer = WordNetLemmatizer()
  set_of_related_nouns = set()
  result = []
  result_rus = []
  wn = wordnet
  for lemma in wn.lemmas(wn.morphy(verb_word, wn.VERB), pos="v"):
        for related_form in lemma.derivationally_related_forms():
            for synset in wn.synsets(related_form.name(), pos=wn.NOUN):
                if wn.synset('person.n.01') in synset.closure(lambda s:s.hypernyms()):
                    set_of_related_nouns.add(synset.name())
  for word in set_of_related_nouns:
          #print(to_rus(word))
          del_tail = word.split('.')[0]
          result.append(del_tail)
  if translate:
      result_rus = listTranslateToRus(result)

      result_rus = remove_words_with_chars(result_rus, "a-zA-Z_")
      result_rus = dublicate_delete(result_rus)                         # Удаление дубликатов
  

  return (result, result_rus)
