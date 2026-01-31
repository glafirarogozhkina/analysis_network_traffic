from pathlib import Path

import joblib
import numpy as np


def predict(x_path: str) -> np.ndarray:
    """
    Загружает модель и возвращает предсказанные зарплаты.
    """
    X = np.load(x_path, allow_pickle=True)

    model_path = Path(__file__).resolve().parent.parent / "resources" / "model.joblib"
    model = joblib.load(model_path)

    predictions = model.predict(X)
    return predictions

