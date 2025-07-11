# 🔍 gendiff

**gendiff** — это CLI-инструмент на Python для сравнения конфигурационных файлов в форматах JSON и YAML.

---

## Hexlet tests and linter status

[![Actions Status](https://github.com/iRatatuii/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/iRatatuii/python-project-50/actions) [![Python CI](https://github.com/iRatatuii/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/iRatatuii/python-project-50/actions/workflows/pyci.yml) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=iRatatuii_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=iRatatuii_python-project-50) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=iRatatuii_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=iRatatuii_python-project-50) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=iRatatuii_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=iRatatuii_python-project-50) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=iRatatuii_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=iRatatuii_python-project-50) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=iRatatuii_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=iRatatuii_python-project-50) [![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

## 🛠 Клонирование репозитория

Сначала склонируйте репозиторий:

```bash
git clone https://github.com/your-username/gendiff.git
cd gendiff
```

## ⚙️ Установка и запуск

### 🔧 С помощью `uv` и Makefile

Установи зависимости и собери проект:

```bash
make install
```

Запуск CLI-инструмента:

```bash
make gendiff
```

Запуск тестов:

```bash
make test
```

Запуск линтера:

```bash
make lint
```

Сборка пакета:

```bash
make build
```

Локальная установка `.tar.gz`:

```bash
make update
```

Локальная установка `.whl`:

```bash
make package-install
```

---

## 🚀 Использование

```bash
gendiff FILE1 FILE2 [OPTIONS]
```

### Аргументы:

- `FILE1`, `FILE2` — пути к конфигурационным файлам `.json`, `.yaml`, `.yml`
- `-f`, `--format` — формат вывода (`stylish`, `plain`, `json`)

---

## 🧪 Примеры

### 📘 Формат `stylish` (по умолчанию):

```bash
gendiff file1.json file2.json
```

```bash
{
  common: {
    + follow: false
      setting1: value 1
    - setting2: 200
    ...
  }
}
```

---

### 📗 Формат `plain`:

```bash
gendiff file1.json file2.json --format plain
```

```bash
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
...
```
---

### 📗 Формат `json`:

```bash
gendiff file1.json file2.json --format json
```

```json
[
    {
        "key": "common",
        "type": "nested",
        "children": [
            {
                "key": "follow",
                "type": "added",
                "value": false
            },
            {
                "key": "setting1",
                "type": "unchanged",
                "value": "Value 1"
            },
            ...
        ]
    }
]
```

---

## 💡 Возможности

- Поддержка JSON и YAML
- Поддержка вложенных структур
- Вывод в форматах:
  - `stylish`
  - `plain`
  - `json`
- Расширяемая архитектура

---

## 🧪 Тестирование

```bash
make test
```

[![asciicast](https://asciinema.org/a/727275.svg)](https://asciinema.org/a/727275)

---

## 🧼 Линтинг

```bash
make lint
```

[![asciicast](https://asciinema.org/a/727277.svg)](https://asciinema.org/a/727277)

---

## 🎬 Демонстрация работы

Ниже представлены интерактивные демонстрации работы `gendiff` с помощью [Asciinema](https://asciinema.org/).

### Запуск сравнения с форматом stylish (по умолчанию)

```bash
gendiff file1.json file2.json
```

[![asciicast](https://asciinema.org/a/727263.svg)](https://asciinema.org/a/727263)

---

### Запуск сравнения с форматом plain

```bash
gendiff file1.json file2.json --format plain
```

[![asciicast](https://asciinema.org/a/727267.svg)](https://asciinema.org/a/727267)

---

### Запуск сравнения с форматом json

```bash
gendiff file1.json file2.json --format json
```

[![asciicast](https://asciinema.org/a/727274.svg)](https://asciinema.org/a/727274)

---

## 🪪 Лицензия

MIT License
