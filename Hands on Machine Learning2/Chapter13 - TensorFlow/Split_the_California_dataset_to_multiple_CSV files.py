from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
import pandas as pd

housing = fetch_california_housing()

X_train_full, X_test, y_train_full, y_test = train_test_split(housing.data,
                                                              housing.target.reshape(-1, 1),
                                                              random_state=42)

X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)

scaler = StandardScaler()

scaler.fit(X=X_train)

X_mean = scaler.mean_

X_std = scaler.scale_

def save_to_multiple_csv_files(data, name_prefix, header=None, n_parts=10):

    housing_dir = os.path.join("datasets", "housing")
    os.makedirs(housing_dir, exist_ok=True)
    path_format = os.path.join(housing_dir, "my_{}_{:02d}.csv")

    filepath = []
    m = len(data)

    for file_idx, row_indices in enumerate(np.array_split(np.arange(m), n_parts)):
        part_csv = path_format.format(name_prefix, file_idx)
        filepath.append(part_csv)
        with open(part_csv, "wt", encoding="utf-8") as f:
            if header is not None:
                f.write(header)
                f.write("\n")
            for row_idx in row_indices:
                f.write(",".join([repr(col) for col in data[row_idx]]))
                f.write("\n")

    return filepath


train_data = np.c_[X_train, y_train]
valid_data = np.c_[X_valid, y_valid]
test_data = np.c_[X_test, y_test]
header_cols = housing.feature_names + ["MedianHouseValue"]
header = ",".join(header_cols)

train_filepaths = save_to_multiple_csv_files(data=train_data, name_prefix="train",
                                             header=header, n_parts=20)

valid_filepaths = save_to_multiple_csv_files(data=valid_data, name_prefix="valid", header=header,
                                             n_parts=10)

test_filepaths = save_to_multiple_csv_files(data=test_data, name_prefix="test", header=header,
                                            n_parts=10)


print(train_filepaths)

print(pd.read_csv(train_filepaths[0]).head())
