
from deep_translator import GoogleTranslator

# is_cyrillic(char) Символ является кириллицей
import sys 

if sys.version_info >= (3, 0): 
 import re
else:
 import regex as re
 
# Перевод слова на английский язык
def to_eng(str):
  return GoogleTranslator(source='auto', target='en').translate(text=str)


# Перевод на русский язык вход и выход - строки
def to_rus(str):
  return GoogleTranslator(source='auto', target='ru').translate(text=str)

# Извлечение из строки списка слов, состоящих только из букв
def extract_alphabetic_words(text):
  #words = re.findall(r'\b[a-zA-Z]+\b', text)                   # \b - границы слова, [a-zA-Z]+ - одна или более букв
  words = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b', text)     # Слова сдефисами тоже выделять
  return words

# Перевод на русский язык списка английских слов слов
def  listTranslateToRus(sourceList):
  string = ','.join(sourceList)
  string = to_rus(string)
  text = string.split(',')
  return (text)

# Конвертирование объекта AttrDict в строку
def AttrDictToString(attr_dict):
  from io import StringIO
  import sys
  import re

  tag_list = []
  save_stdout = sys.stdout
  result = StringIO()
  sys.stdout = result
  print(attr_dict)
  sys.stdout = save_stdout
  #tag_list.append(result.getvalue())
  s = result.getvalue()
  s = s.replace('_', '-')              # Двусловные слова через _ сделать словосочетанием через дефис
  s = s[:-1]                           # Удаление '\n' в конце строки
  return(s)

# ФУНКЦИИ ОБРАБОТКИ СТРОК

# Удаление из списка слов, содержащих символы, описанные регулярными выражениями char_range
def remove_words_with_chars(word_list, char_range):
    pattern = f"[{char_range}]" # Создаем шаблон на основе заданного диапазона
    return [word for word in word_list if not re.search(pattern, word)]

# Удаление слов, набранных латиницей
# Вход и выход: списки слов
def remove_latin_words_regex(word_list):
    return [word for word in word_list if not re.search(r"[a-zA-Z_]", word)]

# Замена в списке слов с символом char_to_replace на слова с символом replacement
def replace_char(word_list, char_to_replace, replacement):
    return [re.sub(r"{}+".format(re.escape(char_to_replace)), replacement, word) for word in word_list]

# Удаление дублей из списка
def dublicate_delete(list):
  temp = []
  for x in list:
    if x not in temp:
       temp.append(x)
  return  temp
