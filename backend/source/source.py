
# importing libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split, GridSearchCV
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from mlxtend.plotting import plot_confusion_matrix

#ignore warnings
import warnings
warnings.filterwarnings('ignore')

#checking versions
# print("np ", np.__version__)
# print("pd ", pd.__version__)
# print("matplotlib ", plt.matplotlib.__version__)
# import sklearn
# print("sklearn ", sklearn.__version__)
# print("seaborn ", sns.__version__)
# import mlxtend
# print("mlxtend ", mlxtend.__version__)

#importing dataset
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
training_path = os.path.join(script_dir, 'Training.csv')
disease_dataset_training = pd.read_csv(training_path)
#checking dataset
# print("Columns in training dataset:", disease_dataset_training.columns.tolist())
# print("Dataset shape:", disease_dataset_training.shape)
# disease_dataset_training.head()

train_data = disease_dataset_training.copy()
# Remove any unnamed columns that might exist
unnamed_cols = [col for col in train_data.columns if 'Unnamed' in col]
if unnamed_cols:
    # print(f"Dropping unnamed columns: {unnamed_cols}")
    train_data = train_data.drop(unnamed_cols, axis=1)
train_data.isnull().sum()

# copy to see corelations
copy = train_data.copy()
copy = copy.drop(['prognosis'], axis=1)

# correlation check
# plt.style.use('fivethirtyeight')
# plt.figure(figsize=(150,150))
# sns.heatmap(copy.corr(), annot=True, fmt=".2f", cmap='viridis')
# plt.show()

x_train = train_data.drop(['prognosis'], axis = 1)
y_train = train_data['prognosis']

scale = MinMaxScaler()
scale.fit(x_train)

# importing testing dataset 
testing_path = os.path.join(script_dir, 'Testing.csv')
test_data = pd.read_csv(testing_path)
# test_data.head()

x_test = test_data.drop(['prognosis'], axis=1)
y_test = test_data['prognosis']

scale2 = MinMaxScaler()
scale2.fit(x_test)

# ML algorithin K-NeighboursClassifier
clf_knn = KNeighborsClassifier()
parametrs_knn = {'n_neighbors':[1,3,5,7,9,11], 'metric':['euclidean','manhattan','chebyshev']}
grid_clf_knn = GridSearchCV(clf_knn, parametrs_knn, cv = 6, n_jobs = -1)
grid_clf_knn.fit(x_train,y_train)

model_knn = grid_clf_knn.best_estimator_
y_pred_knn = model_knn.predict(x_test)

# cm_knn = confusion_matrix(y_test, y_pred_knn)
# print('Confusion matrix for model ' f'{model_knn} : \n', cm_knn)
# ac_knn = accuracy_score(y_test, y_pred_knn)
# print("Accuracy score for model" f'{model_knn} : ', ac_knn)
# cr_knn = classification_report(y_test, y_pred_knn)
# print("classification_report for mofel" f'{model_knn}: \n', cr_knn)

# cm_knn = confusion_matrix(y_test, y_pred_knn)
# fig, ax = plot_confusion_matrix(conf_mat = cm_knn, show_absolute = True, colorbar = True, cmap = 'Wistia', figsize=(12,12))
# plt.title("CM for Diseases Model")
# plt.show()

print(model_knn.score(x_train, y_train))

print(model_knn.score(x_test, y_test))