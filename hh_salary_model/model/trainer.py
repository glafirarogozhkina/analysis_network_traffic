from pathlib import Path

import joblib
import numpy as np
from sklearn.linear_model import LinearRegression


def train(x_path: str, y_path: str) -> None:
    """
    Обучает линейную регрессию и сохраняет модель в resources/.
    """
    X = np.load(x_path, allow_pickle=True)
    y = np.load(y_path, allow_pickle=True)

    model = LinearRegression()
    model.fit(X, y)

    resources_dir = Path(__file__).resolve().parent.parent / "resources"
    resources_dir.mkdir(exist_ok=True)

    model_path = resources_dir / "model.joblib"
    joblib.dump(model, model_path)

