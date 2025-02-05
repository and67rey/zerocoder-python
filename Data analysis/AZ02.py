import pandas as pd

data = {
    'students' : ['Alice', 'Bob', 'Clara', 'Dan', 'Eve', 'Frank', 'Gene', 'Harold', 'John', 'Ken'],
    'math' : [3, 4, 4, 5, 4, 3, 4, 5, 4, 3],
    'physics' : [4, 4, 3, 5, 5, 4, 3, 4, 5, 4],
    'biology' : [5, 4, 4, 4, 4, 5, 4, 3, 5, 4],
    'chemistry' : [5, 5, 3, 4, 5, 4, 3, 4, 4, 5],
    'astronomy' : [4, 4, 4, 5, 5, 4, 4, 5, 5, 4],
}

df = pd.DataFrame(data)

df.set_index('students', inplace=True)

print(df.head())
print()
print(df.describe())
print()
print('Средние оценки:')
print(f" по математике - {df['math'].mean()}")
print(f" по физике - {df['physics'].mean()}")
print(f" по биологии - {df['biology'].mean()}")
print(f" по химии - {df['chemistry'].mean()}")
print(f" по астрономии - {df['astronomy'].mean()}")
print()
print('Медианные оценки:')
print(f" по математике - {df['math'].median()}")
print(f" по физике - {df['physics'].median()}")
print(f" по биологии - {df['biology'].median()}")
print(f" по химии - {df['chemistry'].median()}")
print(f" по астрономии - {df['astronomy'].median()}")
print()

Q1_math = df['math'].quantile(0.25)
Q3_math = df['math'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f'Значение Q1 по математике - {Q1_math}')
print(f'Значение Q3 по математике - {Q3_math}')
print(f'Значение IQR по математике - {IQR_math}')

print()
print('Стандартные отклонения:')
print(f" по математике - {df['math'].std()}")
print(f" по физике - {df['physics'].std()}")
print(f" по биологии - {df['biology'].std()}")
print(f" по химии - {df['chemistry'].std()}")
print(f" по астрономии - {df['astronomy'].std()}")





