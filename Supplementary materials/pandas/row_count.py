# How do I get the row count of a Pandas DataFrame?

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(2 * 3).reshape(2, 3))
print(df)

print()

perfplot.save(
    "out.png",
    setup=lambda n: pd.DataFrame(np.arange(n * 3).reshape(n, 3)),
    n_range=[2**k for k in range(25)],
    kernels=[
        lambda df: len(df.index),
        lambda df: df.shape[0],
        lambda df: df[df.columns[0]].count(),
    ],
    labels=["len(df.index)", "df.shape[0]", "df[df.columns[0]].count()"],
    xlabel="Number of rows",
)

# Source: https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
