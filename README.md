# analysis_network_traffic
# HH Pipeline

Пайплайн обработки данных hh.ru с использованием паттерна
Chain of Responsibility.

Проект загружает CSV-файл с резюме, обрабатывает данные и сохраняет
результат в формате `.npy`, готовом для дальнейшего анализа и обучения моделей.


## Запуск

Из папки `hh_pipeline` выполните:

```bash
python app.py path/to/hh.csv
