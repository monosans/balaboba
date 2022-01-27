# balaboba

Обёртка для [Яндекс Балабоба](https://yandex.ru/lab/yalm).

Асинхронная версия [здесь](https://github.com/monosans/aiobalaboba).

## Установка

```sh
python -m pip install balaboba
```

## Примеры использования

### Базовый пример

```python
from balaboba import balaboba

response = balaboba("Привет")
print(response)
```

Вывод: `Привет! Я рад тебя видеть на моём канале. Здесь ты сможешь встретить много интересных аниме, музыки, видео, и многого другого.`

### Варианты стилизации

Функции `balaboba` в качестве аргумента `intro` можно передать желаемый вариант стилизации. Номера всех вариантов стилизации есть в [докстринге](https://github.com/monosans/balaboba/blob/main/balaboba/_balaboba.py#L28). В примере используется 11-й вариант стилизации "Народные мудрости" ([полный код примера](https://github.com/monosans/balaboba/blob/main/examples/style.py)):

```python
response = balaboba("Привет", intro=11)
```

### Свой экземпляр cloudscraper.CloudScraper

Функции `balaboba` в качестве аргумента `session` можно передать экземпляр `cloudscraper.CloudScraper` ([полный код примера](https://github.com/monosans/balaboba/blob/main/examples/client_session.py)):

```python
from cloudscraper import create_scraper

with create_scraper() as session:
    response = balaboba("Привет", session=session)
```

Таким же образом можно передать экземпляр `requests.Session`, но эта возможность существует только для обратной совместимости.

## Дисклеймер с сайта

Нейросеть не знает, что говорит, и может сказать всякое — если что, не обижайтесь. Распространяя получившиеся тексты, помните об ответственности.

## License / Лицензия

[MIT](https://github.com/monosans/balaboba/blob/main/LICENSE)
