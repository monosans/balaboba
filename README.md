# balaboba

Модуль для взаимодействия с [Яндекс Балабоба](https://yandex.ru/lab/yalm).

Асинхронная версия [здесь](https://github.com/monosans/aiobalaboba).

## Установка

```sh
python -m pip install balaboba
```

Или просто скопируйте [код](https://github.com/monosans/balaboba/blob/main/balaboba/__init__.py) себе.

## Пример использования

### Базовый пример

Используется стандартный вариант стилизации, для запроса создаётся новый экземпляр requests.Session:

```python
from balaboba import balaboba

response = balaboba("Привет")
print(response)
```

Вывод: `Привет! Я рад тебя видеть на моём канале. Здесь ты сможешь встретить много интересных аниме, музыки, видео, и многого другого.`

### Продвинутый пример

Используется 11-ый вариант стилизации "Народные мудрости", для запроса используется существующий экземпляр requests.Session:

```python
from balaboba import balaboba
from requests import Session

with Session() as session:
    response = balaboba("Привет", intro=11, session=session)
print(response)
```

## Дисклеймер с сайта

Нейросеть не знает, что говорит, и может сказать всякое — если что, не обижайтесь. Распространяя получившиеся тексты, помните об ответственности.

## License / Лицензия

[MIT](LICENSE)
