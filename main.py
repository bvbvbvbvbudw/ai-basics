import pandas as pd


data = {
    "Surname": ["a", "b", "c"],
    "Name": ["Ivan", "Petro", "Sidor"],
    "Birthday": ["1990-01-01", "1985-05-15", "1995-12-31"],
    "Weight": [75.5, 68.2, 80.0],
    "Insurance": [True, False, True]
}
df = pd.DataFrame(data)
print(df.info())