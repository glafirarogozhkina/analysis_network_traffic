# HH Data Processing & Salary Prediction

Репозиторий содержит два проекта:

1. Пайплайн обработки сырых данных hh.ru  
2. Регрессионную модель для предсказания зарплат

Проекты используются последовательно:  
результат первого задания является входом для второго.

---

## HH Pipeline (обработка данных)

Проект расположен в папке `hh_pipeline/`.

Пайплайн загружает CSV-файл с резюме hh.ru, обрабатывает данные и сохраняет
результат в формате `.npy`, готовом для дальнейшего анализа и обучения моделей.

### Входные данные

- CSV-файл с резюме hh.ru

### Запуск

Перейдите в папку пайплайна:

```bash
cd hh_pipeline

Запустите обработку:

python app.py path/to/hh.csv

Результат

После выполнения будут созданы файлы:
x_data.npy — encoded feature matrix
y_data.npy — target vector (зарплата, float, рубли)

Файлы используются во втором задании.

What the pipeline does
ReaderHandler — читает CSV-файл
CleanerHandler — очищает данные
SalaryParserHandler — парсит зарплату из текста
SplitterHandler — разделяет данные на X и y
EncoderHandler — one-hot кодирует категориальные признаки
SaverHandler — сохраняет x_data.npy и y_data.npy

Реализация выполнена с использованием паттерна Chain of Responsibility.

Salary Regression Model
Проект расположен в папке hh_salary_model/.
Модель обучается на данных, полученных из hh_pipeline,
и используется для предсказания зарплат.

Установка зависимостей

cd hh_salary_model
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Обучение модели
Обучение выполняется один раз:
python -c "from model.trainer import train; train('../hh_pipeline/x_data.npy', '../hh_pipeline/y_data.npy')"

После обучения веса сохраняются в:
hh_salary_model/resources/model.joblib

Предсказание зарплат
Вывести список зарплат в stdout (в рублях, float):
python app.py path/to/x_data.npy
