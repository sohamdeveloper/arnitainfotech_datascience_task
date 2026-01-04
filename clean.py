import pandas as pp
df = pp.read_csv("students.csv", sep=';')
df = df.dropna()

df['pass'] = df['G3'].apply(lambda x:1 if x >= 10 else 0)
clean_df = df[['studytime', 'absences', 'G1', 'G2','pass']]

clean_df.to_csv("cleaned-student_performance.csv", index = False)

print("cleaning and labeling successfull")