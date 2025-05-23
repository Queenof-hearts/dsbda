import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)
# ----
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
# -----
import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)
# -----
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
# ------
n_num = [1, 2, 3, 4, 5]
n = len(n_num)

get_sum = sum(n_num)
mean = get_sum/n

print("Mean / Average is : " + str(mean))
# -----
n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2-1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is : " + str(median))
# ------
from collections import Counter

n_num = [1, 2, 3, 4, 5, 5]
n = len(n_num)

data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is/are : " + ', '.join(map(str,mode))
print(get_mode)
# ------
import pandas as pd

df = pd.DataFrame({'A' : ['a', 'b', 'c', 'c', 'a', 'b'],
                   'B' : [0, 1, 1, 0, 1, 0]}, dtype = "category")
df.dtypes
# -----
print(df)

print(df.groupby(['A']). count().reset_index())
# ------
import pandas as pd

df = pd.DataFrame({'A' : ['a', 'b', 'c', 'c', 'a', 'b'],
                   'B' : [0, 1, 1, 0, 1, 0],
                   'C' : [7, 8, 9, 5, 3, 6]})

df['A'] = df['A'].astype('category')

print(df)

print(df.groupby(['A', 'B']).mean().reset_index())
# -----
import pandas as pd

data = pd.read_csv(r"D:\College\TE\SEM-2\Practical\DSBDA\3\Iris.csv")

print('Iris-setosa')
setosa= data['Species'] == 'Iris-setosa'
print(data[setosa].describe())

print('\nIris-versicolor')
versicolor= data['Species'] == 'Iris-versicolor'
print(data[versicolor].describe())

print('\nIris-virginica')
virginica = data['Species'] == 'Iris-virginica'
print (data[virginica].describe())

