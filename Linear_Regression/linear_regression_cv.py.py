# ---------------------- Import Libraries ----------------------
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, KFold, LeaveOneOut, StratifiedKFold
from sklearn.metrics import r2_score
from sklearn.preprocessing import KBinsDiscretizer

# ---------------------- Load Dataset ----------------------
df = pd.read_csv("sal.csv")   # Make sure sal.csv is in the same folder as this script
print(df.head())

# Features (all columns except last) and Target (last column)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Model
model = LinearRegression()

# ---------------------- (i) Holdout Validation ----------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2_holdout = r2_score(y_test, y_pred)

# ---------------------- (ii) Leave-One-Out Cross Validation (LOOCV) ----------------------
loo = LeaveOneOut()
predictions, actuals = [], []

for train_idx, test_idx in loo.split(X):
    model.fit(X[train_idx], y[train_idx])
    pred = model.predict(X[test_idx])
    predictions.append(pred[0])
    actuals.append(y[test_idx][0])

r2_loocv = r2_score(actuals, predictions)

# ---------------------- (iii) Stratified Cross-Validation ----------------------
# Bin the target variable for stratification
est = KBinsDiscretizer(
    n_bins=3,
    encode='ordinal',
    strategy='quantile',
    quantile_method='linear'   # <-- Added to silence warning
)
y_binned = est.fit_transform(y.reshape(-1, 1)).ravel()

skf = StratifiedKFold(n_splits=3)   # use 3 since dataset is small
r2_stratified_scores = []

for train_idx, test_idx in skf.split(X, y_binned):
    model.fit(X[train_idx], y[train_idx])
    y_pred = model.predict(X[test_idx])
    r2_stratified_scores.append(r2_score(y[test_idx], y_pred))

r2_stratified = np.mean(r2_stratified_scores)

# ---------------------- (iv) K-Fold Cross Validation ----------------------
kf = KFold(n_splits=5, shuffle=True, random_state=42)
r2_kfold_scores = []

for train_idx, test_idx in kf.split(X):
    model.fit(X[train_idx], y[train_idx])
    y_pred = model.predict(X[test_idx])
    r2_kfold_scores.append(r2_score(y[test_idx], y_pred))

r2_kfold = np.mean(r2_kfold_scores)

# ---------------------- Show Results ----------------------
print("Model Accuracy (R² Score):")
print(f"(i) Holdout Validation               : {r2_holdout:.4f}")
print(f"(ii) Leave-One-Out CV (LOOCV)        : {r2_loocv:.4f}")
print(f"(iii) Stratified K-Fold CV           : {r2_stratified:.4f}")
print(f"(iv) K-Fold CV                       : {r2_kfold:.4f}")
