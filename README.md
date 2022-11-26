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

# Get text types
intros = bb.intros(language="en")

# Get the first text type
intro = intros[0].number

# Print Balaboba's response to the "Hello" query
response = bb.balaboba("Hello", intro=intro)
print(response)
```

## License

[MIT](https://github.com/monosans/balaboba/blob/main/LICENSE)
