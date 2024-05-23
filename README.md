## Пошаговая инструкция по развертыванию

#### Клонируйте репозиторий:
```bash
git clone https://github.com/VadimRoziznan/ollama
cd ollama
```
#### Создайте виртуальное окружение:
```bash
python3 -m venv env
```
#### Активируйте виртуальное окружение:
```bash
source env/bin/activate
```
#### Установите зависимости проекта:
```bash
pip install -r requirements.txt
```

#### Установите Ollama
[Download Ollama](https://ollama.com/download)

#### Откройте терминал и запустите

`ollama run llama3` или `ollama run llama3:70b`

## Системные требования

| Model | Parameters | Size | RAM | Download |
|---|---|---|---|---|
| Llama-3-8B | 8B | 4.7GB | 16GB | `ollama run llama3` |
| Llama-3-70B | 70B | 40GB | 64GB | `ollama run llama3:70b` |

