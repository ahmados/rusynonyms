## ru_synonyms
Russian words synonyms and antonyms.


## Install
```
pip install git+https://github.com/ahmados/rusynonyms.git
```

## Usage
```
from ru_synonyms import AntonymsGraph, SynonymsGraph

# Initialize both synonyms and antonyms graph
sg = SynonymsGraph()
ag = AntonymsGraph()

# Sample input word
word = "хорошо"

# Check whether word in graph or not.
assert sg.is_in_dictionary(word)

# Print first found synonym
print(next(sg.get_list(word)))

# Check whether word in graph or not.
assert ag.is_in_dictionary(word)

# Print first found antonym
print(next(ag.get_list(word)))

>> впору
>> нет
```

## Что?
Это кастомные классы и два adjlist файла для извлечения синонимов и антонимов слов русского языка. Прошу упоминать репозиторий и автора если будете использовать эти ресурсы.

## Автор
Sumekenov Akhmad, sumekenov@gmail.com, t.me/sumekenov 
