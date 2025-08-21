# 📈 Linear Regression Cross-Validation Playground

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

<i>Explore, compare, and visualize linear regression accuracy using four powerful cross-validation techniques!</i>

</div>

---

## 🚀 Overview

This project demonstrates how to evaluate a linear regression model using **Holdout**, **LOOCV**, **Stratified K-Fold**, and **K-Fold** cross-validation strategies in Python. Results are compared using the R² score for each method.

> 🎯 **Goal:** See how different validation strategies impact model accuracy and reliability.

---

## 📁 Project Structure

```
Linear Regression/
├── linear_regression_cv.py.py   # Main script
├── sal.csv                     # Dataset file
├── README.md                   # This documentation
```

---

## 🛠️ Technologies Used

| Python | Pandas | NumPy | scikit-learn |
| :----: | :----: | :---: | :----------: |
|   🐍   |   🐼   |  🔢   |      🤖      |

---

## 📋 Prerequisites

```powershell
pip install pandas numpy scikit-learn
```

---

## 📊 Data & Features

- **Input:** `sal.csv` (all columns except last are features)
- **Target:** Last column in `sal.csv`

---

## 🧑‍💻 How It Works

### 1️⃣ Data Loading & Preparation

```python
df = pd.read_csv("sal.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
```

### 2️⃣ Model Setup

```python
model = LinearRegression()
```

### 3️⃣ Validation Techniques

| Method               | What It Does                       | When To Use              |
| -------------------- | ---------------------------------- | ------------------------ |
| 🟦 Holdout           | Train/test split (80/20)           | Quick baseline           |
| 🟩 LOOCV             | Each sample is tested once         | Small datasets, unbiased |
| 🟨 Stratified K-Fold | Folds preserve target distribution | Imbalanced targets       |
| 🟧 K-Fold            | Random folds, average results      | General purpose          |

---

## 🔬 Workflow Breakdown

<details>
<summary>🔍 <b>Step-by-step process</b></summary>

1. **Holdout Validation**
   - Split data, train, test, compute R²
2. **LOOCV**
   - For each sample: train on all others, test on one
3. **Stratified K-Fold**
   - Bin target, split into stratified folds, train/test
4. **K-Fold**
   - Shuffle, split into 5 folds, train/test
5. **Results**
   - Print R² for each method

</details>

---

## 📈 Output Example

```
Model Accuracy (R² Score):
(i) Holdout Validation               : 0.9123
(ii) Leave-One-Out CV (LOOCV)        : 0.9056
(iii) Stratified K-Fold CV           : 0.9102
(iv) K-Fold CV                       : 0.9087
```

---

## 🧠 Key Insights

- **Holdout**: Fast, but can be sensitive to random splits
- **LOOCV**: Most robust for small datasets
- **Stratified K-Fold**: Best for imbalanced targets
- **K-Fold**: Reliable for general use

---

## 📝 Customization

- Change `n_bins` or `n_splits` in the script to adjust folds/bins
- Replace `sal.csv` with your own dataset (same format)

---

## 📚 References

- [scikit-learn documentation](https://scikit-learn.org/stable/documentation.html)
- [Cross-validation strategies](https://scikit-learn.org/stable/modules/cross_validation.html)

---

<div align="center">

![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Complete-brightgreen?style=for-the-badge&logo=chart-dot-js)
![Validation Methods](https://img.shields.io/badge/Validation-4%20Types-blue?style=for-the-badge&logo=check)
![Code Quality](https://img.shields.io/badge/Code%20Quality-High-yellow?style=for-the-badge&logo=code)

<i>Made with ❤️ for the Machine Learning Community</i>

</div>
