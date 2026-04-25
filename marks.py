import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("marks.csv")
print(df)
plt.scatter(df["name"],df["marks"])
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student marks graph")
plt.show()