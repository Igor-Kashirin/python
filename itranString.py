
from deep_translator import GoogleTranslator

# is_cyrillic(char) ������ �������� ����������
import sys 

if sys.version_info >= (3, 0): 
 import re
else:
 import regex as re
 
# ������� ����� �� ���������� ����
def to_eng(str):
  return GoogleTranslator(source='auto', target='en').translate(text=str)


# ������� �� ������� ���� ���� � ����� - ������
def to_rus(str):
  return GoogleTranslator(source='auto', target='ru').translate(text=str)

# ���������� �� ������ ������ ����, ��������� ������ �� ����
def extract_alphabetic_words(text):
  #words = re.findall(r'\b[a-zA-Z]+\b', text)                   # \b - ������� �����, [a-zA-Z]+ - ���� ��� ����� ����
  words = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b', text)     # ����� ��������� ���� ��������
  return words

# ������� �� ������� ���� ������ ���������� ���� ����
def  listTranslateToRus(sourceList):
  string = ','.join(sourceList)
  string = to_rus(string)
  text = string.split(',')
  return (text)

# ��������������� ������� AttrDict � ������
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
  s = s.replace('_', '-')              # ���������� ����� ����� _ ������� ��������������� ����� �����
  s = s[:-1]                           # �������� '\n' � ����� ������
  return(s)

# ������� ��������� �����

# �������� �� ������ ����, ���������� �������, ��������� ����������� ����������� char_range
def remove_words_with_chars(word_list, char_range):
    pattern = f"[{char_range}]" # ������� ������ �� ������ ��������� ���������
    return [word for word in word_list if not re.search(pattern, word)]

# �������� ����, ��������� ���������
# ���� � �����: ������ ����
def remove_latin_words_regex(word_list):
    return [word for word in word_list if not re.search(r"[a-zA-Z_]", word)]

# ������ � ������ ���� � �������� char_to_replace �� ����� � �������� replacement
def replace_char(word_list, char_to_replace, replacement):
    return [re.sub(r"{}+".format(re.escape(char_to_replace)), replacement, word) for word in word_list]

# �������� ������ �� ������
def dublicate_delete(list):
  temp = []
  for x in list:
    if x not in temp:
       temp.append(x)
  return  temp
