import pandas as pd

exportation = pd.read_csv("2020_export_value_from_each_customs.csv", header=0, index_col=0)

print(exportation)

percentile = [(1544101314 / 13800075242),
              (6674773304 / 13800075242),
              (2550413664 / 13800075242),
              (3030786960 / 13800075242),
              100]

print(percentile)
