import pandas as pd

df = pd.read_excel('sheets/assignment_1_results.xlsx')
df.columns.ravel()
print(df.columns.ravel())
