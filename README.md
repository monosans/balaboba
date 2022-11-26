# balaboba

[![CI](https://github.com/monosans/balaboba/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/balaboba/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/balaboba/main.svg)](https://results.pre-commit.ci/latest/github/monosans/balaboba/main)
[![codecov](https://codecov.io/gh/monosans/balaboba/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/balaboba)

Wrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).

Asynchronous version [here](https://github.com/monosans/aiobalaboba).

## Disclaimer

The neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.

## Installation

```bash
python -m pip install balaboba
```

## Usage example

```python
from balaboba import Balaboba

bb = Balaboba()
text_types = bb.get_text_types(language="en")
text_type = text_types[0].number
response = bb.balaboba("Hello", intro=text_type)
print(response)
```

## License

[MIT](https://github.com/monosans/balaboba/blob/main/LICENSE)
