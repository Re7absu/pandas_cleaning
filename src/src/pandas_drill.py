import pandas as pd

# create table
students = pd.DataFrame({
    "name": ["Sara", "Ahmed", "Mona", "Ali", "Nora"],
    "age": [22, 25, 21, 24, 23],
    "score": [90, 75, 95, 60, 88]
})


#print(students["score"])

#print(students[["name","score"]])

#print(students.index)

#print(students.dtypes)

#print(students.loc[2])
#print(students.loc[2,"score"])

#print(students.iloc[0]) : يعتمد ع رقم الصف والعامود 
#print(students.iloc[1,2])

#print(students[["name","age"]])

#print(students[students["score"]>80])

#print(students[(students["score"]>=80) & (students["age"]>=22)])
print(students.loc[students["score"] > 80, ["name", "score"]])