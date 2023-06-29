import numpy as np

# Charger les données à partir du fichier .npy
data = np.load("chemin/vers/fichier.npy")

# Utiliser les données selon vos besoins
print(data)

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("https://www.stat4decision.com/telecom.csv")

data["Churn?"] = data["Churn?"].astype('category')

# on définit x et y
# y correspond au trust 
# x correspond au vecteur des modalités à chaque moment 
# y correspond au trust à chaque moment 
# on définit x (vecteur des vecteurs de modalités )
# on lit les fichiers : saved_file="C:/Users/lisar/Documents/paf/Data_prosodie/"+str(interaction)+"/segment_"+str(num_segment)
# pour y on lit les fichiers : saved_file2="C:/Users/lisar/Documents/paf/Data_Trust/"+str(interaction)
y = data["Churn?"].cat.codes
# on ne prend que les colonnes quantitatives
x = data.select_dtypes(np.number).drop(["Account Length",
                                        "Area Code"],axis=1)