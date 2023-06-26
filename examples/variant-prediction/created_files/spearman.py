import pandas as pd

from scipy.stats import spearmanr

df = pd.read_csv("Ranganathan2015wt_output.csv")
df["esm1v_t33_650M_UR90S_ALL"] = (df["esm1v_t33_650M_UR90S_1"] + df["esm1v_t33_650M_UR90S_2"] + df["esm1v_t33_650M_UR90S_3"] + df["esm1v_t33_650M_UR90S_4"] + df["esm1v_t33_650M_UR90S_5"]) / 5

df1 = df[["2500_1"]]
df2 = df[["esm1v_t33_650M_UR90S_ALL"]]

rho, p = spearmanr(df1, df2)

print(rho)

"""
df3 = df[["Unnamed: 0.1", "2500", "Unnamed: 0", "esm1v_t33_650M_UR90S_ALL"]]

df1 = df1.sort_values("2500", ascending = False)
df2 = df2.sort_values("esm1v_t33_650M_UR90S_ALL", ascending = False)
print(df1)
print(df2)
"""


# df.to_csv("df_new_output.csv", sep = ",")