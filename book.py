import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("book.csv")
print(df)
plt.pie(df["biology"],labels=df["students"])
plt.pie(df["physics"],labels=df["biology"])
plt.pie(df["chemistry"],labels=df["physics"])
plt.pie(df["maths"],labels=df["chemistry"])
plt.title("student marks graph")
plt.show()