"""Load an approved local CSV dataset."""

from pathlib import Path
import pandas as pd


def load_dataset(path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    return pd.read_csv(file_path)
