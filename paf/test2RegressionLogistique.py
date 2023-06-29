import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_recall_fscore_support

import os 

saved_file_features_train = "C:/Users/lisar/Documents/paf/features_train1.npy"
saved_file_trust_train = "C:/Users/lisar/Documents/paf/trust_train1.npy"

saved_file_trust_test = "C:/Users/lisar/Documents/paf/Data_Trust/30.npy" #on change le numéro pour que ce soit celui de l'interaction test

# On crée un fichier qui concatène les vecteurs de modalités à chaque moment pour toutes les intéractions sauf la test
# On concatène les segments pour chaque interaction    
for interaction in [9, 10, 12, 15, 18, 19, 24, 26, 27, 30]:
    features_concatenes = np.zeros((0,88))
    
    # Lecture des fichiers
    dossier = "C:/Users/lisar/Documents/paf/Data_prosodie/" + str(interaction)
    
    # Liste tous les fichiers dans le dossier
    fichiers = os.listdir(dossier)
    
    # Compte le nombre de fichiers dans la liste
    nombre_fichiers = len(fichiers)
    print("Nombre de fichiers :", nombre_fichiers)
    
    # On fait une boucle sur chaque segment pour les regrouper
    for num_segment in range(nombre_fichiers):
        saved_file = "C:/Users/lisar/Documents/paf/Data_prosodie/" + str(interaction) + "/segment_" + str(num_segment)+".npy"
        
        # On concatène les informations lues dans les fichiers
        vecteur = np.load(saved_file)
        features_concatenes=np.append(features_concatenes,vecteur, axis=0)
    
    np.save("C:/Users/lisar/Documents/paf/segmentsconc" + str(interaction), features_concatenes) 
    print(1)
    print(interaction)

saved_file_features_test = "C:/Users/lisar/Documents/paf/segmentsconc30.npy" #on change le numéro pour que ce soit celui de l'interaction test

# On concatène les interactions
features_concatenes = np.zeros((0, 88))
for interaction in [9, 10, 12, 15, 18, 19, 24, 26, 27]:
    # Lecture des fichiers
    saved_file = "C:/Users/lisar/Documents/paf/segmentsconc" + str(interaction)+".npy"
    
    # On concatène les informations lues dans les fichiers
    vecteur = np.load(saved_file)
    features_concatenes=np.append(features_concatenes,vecteur, axis=0)
    print(2)
    print(interaction)

np.save(saved_file_features_train, features_concatenes) 

# On crée un fichier qui concatène les vecteurs de trust (vecteur qui contient tous les segments) pour toutes les intéractions sauf la 9
trust_concatenes = np.zeros((0,))
for interaction in [9, 10, 12, 15, 18, 19, 24, 26, 27]:
    # Lecture des fichiers
    saved_file = "C:/Users/lisar/Documents/paf/Data_Trust/" + str(interaction)+".npy"
    
    # On concatène les informations lues dans les fichiers
    vecteur = np.load(saved_file)
    print(vecteur.shape)
    trust_concatenes= np.append(trust_concatenes,vecteur, axis=0)
    print(3)
    print(interaction)

np.save(saved_file_trust_train, trust_concatenes) 

X_train = np.load(saved_file_features_train)
y_train = np.load(saved_file_trust_train)
X_test = np.load(saved_file_features_test)
y_test = np.load(saved_file_trust_test)

model = LogisticRegression()

# cross-validation
cv_score = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy').mean()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
recall = precision_recall_fscore_support(y_test, predictions, average='macro')[1]
f1_score = precision_recall_fscore_support(y_test, predictions, average='macro')[2]
print("Cross-validation scores:", cv_score)
print("Mean accuracy:", np.mean(cv_score))
print("Recall:", recall)
print("F1-score:", f1_score)


