import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# df = pd.read_table('./resources/chipotle.tsv')
# print(df.head())

users = pd.read_table('./resources/u.user', sep='|')
# print(users.head())
occ_summary = users.occupation.value_counts()
# print(occ_summary)
occ_summary.plot(kind='barh', figsize=(15, 10), color='#006600')

plt.show()