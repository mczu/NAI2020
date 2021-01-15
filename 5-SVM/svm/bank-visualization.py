import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

banknote_data = pd.read_csv("banknote_authentication.csv")
y = banknote_data['Class']
X = banknote_data.drop('Class',axis=1)
sns.pairplot(banknote_data, hue="Class",palette="bright")
plt.show()