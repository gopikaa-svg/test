import pandas as pd
data={
    "calories":[400,300,200],
    "duration": [50,40,30]
}
df=pd.DataFrame(data)
print(df)

print(df.loc[0])

import pandas as pd
data={
    "students":['a','b','c','d','e','f','g','h','i','j'],
    "marks":[90,91,92,93,94,95,96,97,98,99]
}
df=pd.DataFrame(data)
print(df)
print(df.loc[6])
print(df.loc[7])