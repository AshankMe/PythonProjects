import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix
data = pd.read_csv(r'C:\Users\ashan\OneDrive\Documents\GitHub\PythonProjects\Machine_Learning\iris.csv')
print(data)

print(data.info())
print(data.shape)
print(data.head(20))
print(data.tail(20))
print(data.describe())
cormatrix = data.corr()
plt.subplots = data.corr()
sns.heatmap(cormatrix, annot = True)
plt.show()
data.plot(kind = 'kde', subplots = True, layout = (2,2), sharex = False, sharey = False)
plt.show()
scatter_matrix(data, diagonal='hist')
scatter_matrix(data, diagonal='kde')
plt.show()
array = data.values
print(array)