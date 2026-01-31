import sys

from model.predictor import predict


def main() -> None:
    if len(sys.argv) != 2:
        raise ValueError("Использование: python app.py path/to/x_data.npy")

    x_path = sys.argv[1]
    salaries = predict(x_path)

    for value in salaries:
        print(float(value))


if __name__ == "__main__":
    main()

