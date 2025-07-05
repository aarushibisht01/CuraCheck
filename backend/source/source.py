
# importing libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
print("np ", np.__version__)
print("pd ", pd.__version__)
print("matplotlib ", sns.__version__)
print("sklearn ", sns.__version__)
print("seaborn ", sns.__version__)
print("mlxtend ", sns.__version__)

#importing dataset
disease_dataset_training = pd.read_csv('./Training.csv')
#checking dataset
disease_dataset_training.head()

train_data = disease_dataset_training.drop(['Unnamed:123'], axis=1)
