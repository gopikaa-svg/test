import matplotlib.pyplot as plt
import numpy as np
students=["arun","varun","tharun","priya","anu"]
marks=[98,95,94,92,90]
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student vs mark")
plt.scatter(students,marks)
plt.grid()
plt.show()
