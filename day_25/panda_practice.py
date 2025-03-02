import pandas

# Create Dataframe
data = {
    'name' : ['alice', 'bob', 'charlie', 'david'],
    'age' : [20, 22, 19, 21],
    'score' : [85, 80, 88, 92]
}

df = pandas.DataFrame(data)
print(df)
print(" ")

# access columns - dot notation
ages = df.age
# print(ages)

# access column - bracket notation
scores = df["score"]
# print(scores)


# access columns - dot notation (specific column element)
ages = df.age[1]
# print(ages)

# access column - bracket notation (specific column element)
scores = df["score"][1]
# print(scores)


# access rows
row = df.iloc[0]
# print(row)
# print(type(row))

row = df.loc[0]
# print(row)

# print
temp = df[df.age == df.age.max()]
print(temp)

temp = df[df.age == 20]
print(temp)

temp = df[df.name == "bob"]
print(temp)