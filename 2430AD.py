import requests
import re
import seaborn as sns


def brick_lang(string):  #brick lanf translator
  return re.sub(r"([у|е|ы|а|о|э|я|и|ю|У|Е|Ы|А|О|Э|Я|И|Ю])", r"\1к\1", string)


def three_word_sent(text):
  return re.findall(r"(\b[А-ЯA-Z]\w+?\b)[ |.|,](\b\w+?\b)[ |.|,](\b\w+?\b)[.|!|?]",text)


URL = "https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD"
references = requests.get(URL).text
numbers = re.findall(r"\b\d+\b", references)
print(numbers)

a_words = re.findall(r"\b\w*?[a|A]+\w*?\b", references)
print(a_words)

exclam_sent = re.findall(r"[A-Z][^\.|\?|!]*?!", references)
print(exclam_sent)

words_len = [len(word) for word in list(dict.fromkeys(re.findall(r"\b\w+?\b", references)))]
print(words_len)
sns.displot(x=words_len, bins=[i for i in range(1,max(words_len))])

string = "Бог умер: теперь хотим мы, чтобы жил сверхчеловек."  #example
brick_lang(string)
URL = "https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD"
text = requests.get(URL).text
print(three_word_sent(text))