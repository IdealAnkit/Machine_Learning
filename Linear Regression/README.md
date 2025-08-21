# 🧮 Linear Regression Cross-Validation Analysis

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-v1.3+-green.svg)
![NumPy](https://img.shields.io/badge/numpy-v1.21+-yellow.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

<i>A comprehensive evaluation of linear regression using four cross-validation strategies</i>

</div>

---

## � Overview

This project demonstrates **linear regression** model evaluation using four popular cross-validation techniques in Python:

- **Holdout Validation**
- **Leave-One-Out Cross Validation (LOOCV)**
- **Stratified K-Fold Cross Validation**
- **K-Fold Cross Validation**

Each method's accuracy is compared using the R² score.

> 🎯 **Goal:** Understand how different validation strategies affect model reliability and accuracy.

---

## 📁 Project Structure

```
Linear_Regression/
├── linear_regression_cv.py.py   # Main analysis script
├── sal.csv                     # Dataset (YearsExperience, Salary)
├── README.md                   # This documentation
```

---

## 🛠️ Technologies Used

<table align="center">
<tr>
<td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50"/><br><b>Python</b></td>
<td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="50"/><br><b>Pandas</b></td>
<td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="50"/><br><b>NumPy</b></td>
<td align="center"><img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width="50"/><br><b>scikit-learn</b></td>
</tr>
</table>

---

## ⚡ Quick Start

### 📋 Prerequisites

```powershell
pip install pandas numpy scikit-learn
```

### ▶️ Run the Analysis

```powershell
# Clone the repository
git clone https://github.com/IdealAnkit/Machine_Learning.git

# Navigate to the project directory
cd Machine_Learning/Linear_Regression

# Run the analysis
python linear_regression_cv.py.py
```

---

## 📊 Data & Features

- **Input:** `sal.csv` (YearsExperience as feature)
- **Target:** Salary (last column)

---

## � Analysis Workflow

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

| Method               | Description                        | Best Use Case            |
| -------------------- | ---------------------------------- | ------------------------ |
| 🟦 Holdout           | Train/test split (80/20)           | Quick baseline           |
| 🟩 LOOCV             | Each sample is tested once         | Small datasets, unbiased |
| 🟨 Stratified K-Fold | Folds preserve target distribution | Imbalanced targets       |
| 🟧 K-Fold            | Random folds, average results      | General purpose          |

---

## 🧩 Step-by-Step Breakdown

<details>
<summary>🔍 <b>Detailed process</b></summary>

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

## 📈 Sample Output

```
Model Accuracy (R² Score):
(i) Holdout Validation               : 0.9123
(ii) Leave-One-Out CV (LOOCV)        : 0.9056
(iii) Stratified K-Fold CV           : 0.9102
(iv) K-Fold CV                       : 0.9087
```

---

## 💡 Key Insights

- **Holdout**: Fast, but can be sensitive to random splits
- **LOOCV**: Most robust for small datasets
- **Stratified K-Fold**: Best for imbalanced targets
- **K-Fold**: Reliable for general use

---

## �️ Customization

- Change `n_bins` or `n_splits` in the script to adjust folds/bins
- Replace `sal.csv` with your own dataset (same format)

---

## 🏆 Achievements & Metrics

<table align="center">
<tr>
<td align="center"><h3>10</h3><p>�️ Samples Analyzed</p></td>
<td align="center"><h3>1</h3><p>📊 Feature Used</p></td>
<td align="center"><h3>4</h3><p>🔎 Validation Methods</p></td>
<td align="center"><h3>1</h3><p>🤖 Model Type</p></td>
</tr>
</table>

---

## �📚 References

- [scikit-learn documentation](https://scikit-learn.org/stable/documentation.html)
- [Cross-validation strategies](https://scikit-learn.org/stable/modules/cross_validation.html)

---

## 🤝 Contributing

We welcome contributions! You can help by:

- 🐞 Reporting bugs and issues
- 💡 Suggesting improvements
- 📈 Adding new validation methods or datasets
- 📝 Improving documentation

---

<div align="center">

![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Complete-brightgreen?style=for-the-badge&logo=chart-dot-js)
![Validation Methods](https://img.shields.io/badge/Validation-4%20Types-blue?style=for-the-badge&logo=check)
![Code Quality](https://img.shields.io/badge/Code%20Quality-High-yellow?style=for-the-badge&logo=code)

### ⭐ **Show Your Support**

If you found this project helpful, please give it a ⭐ on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/IdealAnkit/Machine_Learning.svg?style=social&label=Star&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/IdealAnkit/Machine_Learning.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/IdealAnkit/Machine_Learning.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/watchers)

<i>Made with ❤️ and ☕ for the Machine Learning Community</i>

</div>
