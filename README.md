# balaboba

[![CI](https://github.com/monosans/balaboba/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/balaboba/actions/workflows/ci.yml)
[![PyPI Downloads](https://img.shields.io/pypi/dm/balaboba?logo=pypi)](https://pypi.org/project/balaboba/)

Wrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).

Asynchronous version [here](https://github.com/monosans/aiobalaboba).

## Disclaimer

The neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.

## Installation

```bash
python -m pip install -U balaboba
```

## Usage example

```python
from balaboba import Balaboba

bb = Balaboba()
text_types = bb.get_text_types(language="en")
response = bb.balaboba("Hello", text_type=text_types[0])
print(response)
```

## License

[MIT](https://github.com/monosans/balaboba/blob/main/LICENSE)
