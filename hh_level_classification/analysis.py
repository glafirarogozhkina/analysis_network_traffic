import matplotlib.pyplot as plt
import pandas as pd

from preprocessing import filter_it_roles, define_level


def plot_class_balance() -> None:
    df = pd.read_csv("../hh_pipeline/data/hh.csv")

    it_df = filter_it_roles(df)
    it_df["level"] = it_df.apply(define_level, axis=1)
    it_df = it_df.dropna(subset=["level"])

    counts = it_df["level"].value_counts()

    plt.figure(figsize=(6, 4))
    counts.plot(kind="bar")
    plt.title("Class balance: junior / middle / senior")
    plt.xlabel("Level")
    plt.ylabel("Number of resumes")
    plt.tight_layout()

    plt.savefig("class_balance.png")
    plt.close()


if __name__ == "__main__":
    plot_class_balance()

