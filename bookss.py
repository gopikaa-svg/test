import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("bookss.csv")
print(df)
# plt.pie(df["sum"],labels=df["students"])
plt.pie(df["AVERAGE"],labels=df["students"],autopct='%1.1f%%')
plt.title("student AVERAGE graph")
plt.show()