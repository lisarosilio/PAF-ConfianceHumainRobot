import numpy as np
from sklearn.linear_model import LogisticRegression
import os 
saved_file_features_train = "C:/Users/lisar/Documents/paf/features_train1"
saved_file_trust_train = "C:/Users/lisar/Documents/paf/trust_train1"

saved_file_trust_test = "C:/Users/lisar/Documents/paf/Data_Trust/9"

# on crée un fichier qui concatène les vecteurs de modalités à chaque moment pour toutes les intéractions sauf la 9
# on concatène les segments pour chaques intéractions    
for interaction in [9,10,12,15,18,19,24,26,27,30]:
        features_concatenes =[]
        # lecture des fichiers : 
        # on récupère le nombre de segments pour chaque intéraction 
        dossier = "C:/Users/lisar/Documents/paf/Data_prosodie/"+str(interaction) 
        # Liste tous les fichiers dans le dossier
        fichiers = os.listdir(dossier)
        # Compte le nombre de fichiers dans la liste
        nombre_fichiers = len(fichiers)
        print("Nombre de fichiers :", nombre_fichiers)
        # on fait une boucle sur chaque segments pour les regrouper
        for num_segment in range(nombre_fichiers) :
            saved_file="C:/Users/lisar/Documents/paf/Data_prosodie/"+str(interaction)+"/segment_"+str(num_segment)
        # on concatène les informations lues dans les fichiers
            vecteur = np.load(saved_file)
            features_concatenes.append(vecteur)
        np.save("C:/Users/lisar/Documents/paf/segmentsconc"+str(interaction) , features_concatenes) 
        print(1)
        print(interaction)
saved_file_features_test = "C:/Users/lisar/Documents/paf/segmentsconc9"
# on concatène les intéractions 
features_concatenes =[]
for interaction in [10,12,15,18,19,24,26,27,30]:
    # lecture des fichiers : 
    saved_file="C:/Users/lisar/Documents/paf/segmentsconc"+str(interaction)
    # on concatène les informations lues dans les fichiers
    vecteur = np.load(saved_file)
    features_concatenes.append(vecteur)
    print(2)
    print(interaction)
np.save(saved_file_features_train, features_concatenes) 
# on crée un fichier qui concatène les vecteurs de trust ( vecteur qui contient tous les segments ) pour toutes les intéractions sauf la 9
trust_concatenes =[]
for interaction in [10,12,15,18,19,24,26,27,30]:
    # lecture des fichiers : 
    saved_file="C:/Users/lisar/Documents/paf/Data_Trust/"+str(interaction)
    # on concatène les informations lues dans les fichiers
    vecteur = np.load(saved_file)
    trust_concatenes.append(vecteur)
    print(3)
    print(interaction)
np.save(saved_file_trust_train, trust_concatenes) 

X_train = np.load(saved_file_features_train)
y_train = np.load(saved_file_trust_train)
X_test = np.load(saved_file_features_test)
y_test = np.load(saved_file_trust_test )

model = LogisticRegression()
print(4)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(accuracy)
