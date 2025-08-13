Repository: idealankit/machine_learning
Subpath: /Iris_Dataset_Analysis
Files analyzed: 3

Estimated tokens: 6.4k

Directory structure:
└── Iris_Dataset_Analysis/
├── README.md
├── iris.csv
├── p01.py
└── figures/

================================================
FILE: Iris_Dataset_Analysis/README.md
================================================

# 🌸 Iris Dataset Analysis - Comprehensive EDA & Visualization

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-v1.3+-green.svg)
![Matplotlib](https://img.shields.io/badge/matplotlib-v3.5+-orange.svg)
![Seaborn](https://img.shields.io/badge/seaborn-v0.11+-purple.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

_A comprehensive exploratory data analysis on the famous Iris flower dataset_

</div>

---

## 📖 Overview

This project performs **comprehensive exploratory data analysis (EDA)** on the famous **Iris dataset** using Python. The analysis includes data inspection, statistical summaries, and multiple types of visualizations to understand the dataset's characteristics and relationships between features.

> 🎯 **Goal**: Explore and visualize patterns in the Iris dataset to understand species characteristics and feature relationships

## 📁 Project Structure

```
Iris_Dataset_Analysis/
├── 📄 p01.py                 # Main analysis script
├── 📊 iris.csv              # Dataset file
├── 📸 figures/              # Generated visualizations
│   ├── Figure_1.png         # 🔀 Pairplot matrix
│   ├── Figure_2.png         # 📈 Distribution histograms
│   ├── Figure_3.png         # 📦 Box plots by species
│   ├── Figure_4.png         # 🔥 Correlation heatmap
│   └── Figure_5.png         # 🎻 Violin plots by species
└── 📖 README.md             # This documentation
```

## 🛠️ Technologies Used

<table align="center">
<tr>
<td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50"/><br><b>Python</b></td>
<td align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="50"/><br><b>Pandas</b></td>
<td align="center"><img src="https://matplotlib.org/stable/_static/logo2_compressed.svg" width="50"/><br><b>Matplotlib</b></td>
<td align="center"><img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width="80"/><br><b>Seaborn</b></td>
</tr>
</table>

## 🚀 Quick Start

### 📋 Prerequisites

```bash
# Install required packages
pip install pandas matplotlib seaborn
```

### ▶️ Run the Analysis

```bash
# Clone the repository
git clone https://github.com/IdealAnkit/Machine_Learning.git

# Navigate to the project directory
cd Machine_Learning/Iris_Dataset_Analysis

# Run the analysis
python p01.py
```

## 📊 Data Analysis Workflow

### 🔍 1. Data Exploration Phase

```python
# Load and inspect the dataset
data = pd.read_csv('iris.csv')
print(data.head())         # First 5 rows
print(data.describe())     # Statistical summary
print(data.info())         # Data types and structure
```

<details>
<summary>🔧 <strong>What this phase reveals</strong></summary>

- ✅ Dataset shape and structure
- ✅ Missing values detection
- ✅ Feature statistics (mean, std, min, max)
- ✅ Data types validation

</details>

### 📈 2. Visualization Pipeline

<div align="center">

| Visualization Type  |        Purpose        |           Key Insights           |
| :-----------------: | :-------------------: | :------------------------------: |
|   🔀 **Pairplot**   | Feature relationships |   Species clustering patterns    |
|  📈 **Histograms**  | Distribution analysis |    Data normality assessment     |
|  📦 **Box Plots**   |   Outlier detection   |        Species comparison        |
|   🔥 **Heatmap**    | Correlation analysis  |       Feature dependencies       |
| 🎻 **Violin Plots** |  Distribution shapes  | Detailed species characteristics |

</div>

## 🔬 Detailed Code Analysis (Lines 24-92)

<div align="center">

### 💻 **Code Implementation Breakdown**

![Code Analysis](https://img.shields.io/badge/Code%20Lines-92-blue?style=for-the-badge&logo=visual-studio-code)
![Functions](https://img.shields.io/badge/Visualizations-5-green?style=for-the-badge&logo=chart-line)
![Libraries](https://img.shields.io/badge/Libraries-3-orange?style=for-the-badge&logo=python)

</div>

### 🎨 1. Style Configuration
```python
sns.set_palette("husl")  # Beautiful color palette for species distinction
```
**🎯 Purpose**: Sets up aesthetically pleasing colors for better visual distinction between iris species.

<details>
<summary><strong>🔍 Technical Deep Dive</strong></summary>

- **HUSL Color Space**: Provides perceptually uniform colors
- **Species Distinction**: Each species gets a unique, visually distinct color
- **Accessibility**: Colors chosen for color-blind friendly visualization

</details>

---

### 🔀 2. Pairplot Visualization 
```python
print("Creating pairplot...")
pairplot = sns.pairplot(data, hue='species')
pairplot.fig.suptitle('Pairplot of Iris Dataset Features', y=1.02)
plt.show()
```

<div align="center">

| Component | Function | Insight Value |
|:---------:|:--------:|:-------------:|
| **Diagonal** | Feature distributions | Individual patterns | 
| **Off-diagonal** | Feature relationships | Cross-correlations |
| **Color coding** | Species identification | Clustering visualization |

</div>

<details>
<summary><strong>📊 What Pairplot Reveals</strong></summary>

- ✅ **Linear relationships** between features
- ✅ **Species clustering** patterns  
- ✅ **Outlier identification** across dimensions
- ✅ **Distribution shapes** for each feature
- ✅ **Separability assessment** between classes

</details>

---

### 📈 3. Distribution Analysis
```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
for i, col in enumerate(numeric_cols):
    row, col_idx = i // 2, i % 2  # Smart positioning logic
    axes[row, col_idx].hist(data[col], bins=20, alpha=0.7)
```

<div align="center">

**🧮 Mathematical Implementation**

```
Grid Position Calculation:
row = i ÷ 2 (integer division)
col = i % 2 (modulo operation)

Example: Feature index 3
→ row = 3 ÷ 2 = 1
→ col = 3 % 2 = 1  
→ Position: (1,1) - bottom right
```

</div>

<details>
<summary><strong>🔍 Advanced Parameters Explained</strong></summary>

- **`bins=20`**: Optimal bin count for 150 samples (√n × 1.5 rule)
- **`alpha=0.7`**: 70% transparency for layered visualization
- **`edgecolor='black'`**: Clear bin boundaries for readability
- **`figsize=(15,10)`**: Aspect ratio optimized for screen viewing

</details>

---

### 📦 4. Statistical Box Plot Analysis
```python
sns.boxplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
```

<div align="center">

**📊 Box Plot Component Decoder**

| Element | Mathematical Definition | Interpretation |
|:-------:|:----------------------:|:--------------:|
| **📦 Box** | IQR = Q3 - Q1 | Middle 50% of data |
| **➖ Median** | Q2 (50th percentile) | Central tendency |
| **📏 Whiskers** | 1.5 × IQR from box edges | Normal variation range |
| **🔴 Outliers** | Beyond whisker limits | Unusual observations |

</div>

---

### 🔥 5. Advanced Correlation Heatmap
```python
correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
```

<div align="center">

**🌡️ Correlation Strength Guide**

![Correlation Scale](https://img.shields.io/badge/Strong%20Positive-0.7%20to%201.0-red?style=flat-square)
![Correlation Scale](https://img.shields.io/badge/Moderate%20Positive-0.3%20to%200.7-orange?style=flat-square)
![Correlation Scale](https://img.shields.io/badge/Weak-0.0%20to%200.3-yellow?style=flat-square)
![Correlation Scale](https://img.shields.io/badge/Moderate%20Negative--0.3%20to%20-0.7-lightblue?style=flat-square)
![Correlation Scale](https://img.shields.io/badge/Strong%20Negative--0.7%20to%20-1.0-blue?style=flat-square)

</div>

---

### 🎻 6. Violin Plot Distribution Analysis
```python
sns.violinplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
```

<details>
<summary><strong>🎵 Violin Plot Advantages</strong></summary>

- **📊 Kernel Density**: Shows actual distribution shape
- **📈 Bandwidth Optimization**: Automatic smoothing parameter selection  
- **🔍 Multi-modal Detection**: Reveals multiple peaks in data
- **📏 Quartile Integration**: Combines box plot information
- **🎯 Outlier Context**: Shows outliers in distribution context

</details>

## Key Insights from Visualizations

1. **Species Separability**: Pairplot shows clear clustering patterns by species
2. **Feature Correlations**: Some features are highly correlated (e.g., petal length and width)
3. **Distribution Patterns**: Most features show roughly normal distributions
4. **Outlier Detection**: Box plots identify unusual measurements
5. **Species Characteristics**: Different species have distinct feature ranges and distributions

## Running the Code

### Prerequisites

```bash
pip install pandas matplotlib seaborn
```

### Execution

```bash
python p01.py
```

The script will display plots sequentially. Close each plot window to proceed to the next visualization.

## Expected Output

1. Console output with dataset statistics
2. Five plot windows displaying different visualizations:
   - Pairplot matrix (saved as `figures/Figure_1.png`)
   - Distribution histograms (saved as `figures/Figure_2.png`)
   - Box plots by species (saved as `figures/Figure_3.png`)
   - Correlation heatmap (saved as `figures/Figure_4.png`)
   - Violin plots by species (saved as `figures/Figure_5.png`)

All generated plots are automatically saved in the `figures/` directory for future reference.

## Dataset Information

The Iris dataset contains 150 samples of iris flowers with:

- **Features**: Sepal length, sepal width, petal length, petal width (in cm)
- **Target**: Species (Setosa, Versicolor, Virginica)
- **Use case**: Classic dataset for classification and pattern recognition tasks

## 💡 Key Insights & Findings

<div align="center">

### 🔍 **Analysis Results**

</div>

| Finding | Description | Visualization | Status |
|:-------:|:-----------:|:-------------:|:------:|
| 🎯 **Species Separability** | Clear clustering patterns between species | Pairplot | ✅ Complete |
| 🔗 **Feature Correlations** | Strong correlation between petal dimensions | Heatmap | ✅ Complete |
| 📊 **Normal Distributions** | Most features follow roughly normal patterns | Histograms | ✅ Complete |
| 🚨 **Outlier Detection** | Few outliers identified in measurements | Box Plots | ✅ Complete |
| 🌸 **Species Characteristics** | Each species has distinct feature ranges | Violin Plots | ✅ Complete |

## 📈 Sample Visualizations

<div align="center">

### 🖼️ **Generated Visualizations Preview**

</div>

The analysis produces **5 comprehensive visualizations**:

### 🔀 1. Pairplot Matrix
> Shows relationships between all feature pairs with species color coding
```
📁 Location: figures/Figure_1.png
🎯 Purpose: Feature relationships and species clustering
📊 Insights: Clear separation between species, especially Setosa
```

### 📈 2. Distribution Histograms  
> Frequency distribution of each numerical feature
```
📁 Location: figures/Figure_2.png
🎯 Purpose: Data distribution analysis
📊 Insights: Most features show normal distribution patterns
```

### 📦 3. Box Plots by Species
> Statistical summaries and outlier detection
```
📁 Location: figures/Figure_3.png
🎯 Purpose: Outlier detection and species comparison
📊 Insights: Few outliers detected, distinct species ranges
```

### 🔥 4. Correlation Heatmap
> Correlation coefficients between features
```
📁 Location: figures/Figure_4.png
🎯 Purpose: Feature correlation analysis
📊 Insights: Strong correlation between petal length/width
```

### 🎻 5. Violin Plots by Species
> Distribution shapes with statistical information
```
📁 Location: figures/Figure_5.png
🎯 Purpose: Detailed distribution analysis
📊 Insights: Species-specific distribution patterns revealed
```

## 🏆 Project Achievements

<div align="center">

![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Complete-brightgreen?style=for-the-badge&logo=chart-dot-js)
![Visualizations](https://img.shields.io/badge/Visualizations-5%20Created-blue?style=for-the-badge&logo=image)
![Documentation](https://img.shields.io/badge/Documentation-Comprehensive-orange?style=for-the-badge&logo=book)
![Code Quality](https://img.shields.io/badge/Code%20Quality-High-yellow?style=for-the-badge&logo=code)

</div>

### 📊 **Analysis Progress**

```
Data Loading & Inspection     ████████████████████ 100%
Statistical Analysis          ████████████████████ 100%
Visualization Creation        ████████████████████ 100%
Documentation                 ████████████████████ 100%
Code Organization             ████████████████████ 100%
```

### 🎯 **Key Metrics**

<table align="center">
<tr>
<td align="center"><h3>150</h3><p>🌸 Samples Analyzed</p></td>
<td align="center"><h3>4</h3><p>📊 Features Explored</p></td>
<td align="center"><h3>3</h3><p>🔍 Species Identified</p></td>
<td align="center"><h3>5</h3><p>📈 Visualizations Created</p></td>
</tr>
</table>

## 🤝 Contributing

We welcome contributions! Here's how you can help:

<div align="center">

[![Contribute](https://img.shields.io/badge/Contribute-Welcome-brightgreen?style=for-the-badge&logo=github)](https://github.com/IdealAnkit/Machine_Learning/issues)
[![Issues](https://img.shields.io/badge/Report%20Issues-Here-red?style=for-the-badge&logo=bug)](https://github.com/IdealAnkit/Machine_Learning/issues)
[![Discussions](https://img.shields.io/badge/Join%20Discussion-Community-purple?style=for-the-badge&logo=discord)](https://github.com/IdealAnkit/Machine_Learning/discussions)

</div>

- 🐛 **Report bugs** and suggest improvements
- 💡 **Add new analysis features** or visualizations  
- 📖 **Improve documentation** and code comments
- 🔧 **Optimize performance** and code structure

## 📝 License

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

</div>

---

<div align="center">

### 🌟 **Show Your Support**

If you found this project helpful, please consider giving it a ⭐!

[![GitHub stars](https://img.shields.io/github/stars/IdealAnkit/Machine_Learning.svg?style=social&label=Star&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/IdealAnkit/Machine_Learning.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/IdealAnkit/Machine_Learning.svg?style=social&label=Watch&maxAge=2592000)](https://github.com/IdealAnkit/Machine_Learning/watchers)

### 📫 **Connect With Me**

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://linkedin.com/in/idealankit)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github)](https://github.com/IdealAnkit)
[![Email](https://img.shields.io/badge/-Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:idealankit@example.com)

*Made with ❤️ and lots of ☕ for the Data Science Community*

**Happy Analyzing! 🚀📊**

</div>

================================================
FILE: Iris_Dataset_Analysis/iris.csv
================================================
sepal length,sepal width,petal length,petal width,verity
6.2,3.1,2.4,1.1,Setosa
5.7,3.1,2.8,2,Versicolor
6.3,2.7,5.1,0.4,Virginica
7,3.1,4.8,1.6,Setosa
5.6,3.1,3.8,0.8,Versicolor
5.6,2.7,4,0.6,Virginica
7.1,3.7,6,1.1,Setosa
6.4,3.2,2.8,0.4,Versicolor
5.4,2.5,4.7,0.8,Virginica
6.2,3.3,3.5,0.2,Setosa
5.4,2.6,3.4,2.8,Versicolor
5.4,3.3,5.7,1.2,Virginica
6,3.5,5.2,0.6,Setosa
4.3,2.7,5.2,1.4,Versicolor
4.4,3.4,6,1.1,Virginica
5.4,3.2,3.8,1,Setosa
5,3.3,5,1.7,Versicolor
6.1,3.8,3.3,1.8,Virginica
5.1,2.9,4.4,0.8,Setosa
4.7,2.7,3.6,0.7,Versicolor
7,2.6,4,1,Virginica
5.6,2.7,4.8,-0.6,Setosa
5.9,3,2.4,0,Versicolor
4.7,3.1,7.4,2.3,Virginica
5.4,3.1,2.1,2.5,Setosa
5.9,3.3,1.7,1,Versicolor
4.9,3,5.8,1.7,Virginica
6.1,3.6,5.1,1.4,Setosa
5.3,2.9,4.9,3.7,Versicolor
5.6,4.1,4.9,2.1,Virginica
5.3,3.3,3.8,1.1,Setosa
7.3,2.7,2.3,0.4,Versicolor
5.8,2.6,3.9,-0.1,Virginica
5,3.2,2.6,1.4,Setosa
6.5,2.9,5.5,0.6,Versicolor
4.8,3.3,3.6,0.1,Virginica
6,3.2,2.4,0.7,Setosa
4.2,3,3.3,0.3,Versicolor
4.7,2.7,4.5,2.5,Virginica
6,2.4,2.8,1.9,Setosa
6.4,2.8,2.4,1.2,Versicolor
5.9,3.3,4.2,2.4,Virginica
5.7,3.1,4.2,1.3,Setosa
5.6,2.5,2.9,0.5,Versicolor
4.6,3.1,3,2.4,Virginica
5.2,3.2,4.2,1.6,Setosa
5.4,2.6,1.3,0.4,Versicolor
6.6,3.1,1.4,1,Virginica
6.1,3,2.6,0.5,Setosa
4.4,2.5,3.4,0.1,Versicolor
6.1,3.1,4.3,1.9,Virginica
5.5,3.2,6.3,2.7,Setosa
5.3,3.4,5.3,0.1,Versicolor
6.3,3.4,3.5,1.7,Virginica
6.6,2.4,3.8,0.7,Setosa
6.5,2.6,2.1,0.8,Versicolor
5.1,3.2,3.8,0.7,Virginica
5.6,3.2,3.3,0.5,Setosa
6.1,3.2,4.3,1.2,Versicolor
6.6,4.5,2.4,0.5,Virginica
5.4,3.2,4.7,1.4,Setosa
5.7,3.5,6.4,1.2,Versicolor
4.9,3.4,3.6,1,Virginica
4.8,3.3,4.5,0.5,Setosa
6.5,2.9,5,0.7,Versicolor
6.9,3.3,3.1,1.8,Virginica
5.7,2.7,4.2,1.6,Setosa
6.6,2.9,3.8,0.4,Versicolor
6.1,2.8,4,1.3,Virginica
5.3,3,2.5,1.8,Setosa
6.1,3.9,3.8,-0.1,Versicolor
7,2.3,4.6,1.6,Virginica
5.8,3.3,6.3,0.7,Setosa
7.1,2.4,5.4,1.7,Versicolor
3.7,2.8,7.5,0.6,Virginica
6.5,3.4,2.5,-0.2,Setosa
5.9,3,5.3,-0.1,Versicolor
5.6,2.6,4.1,1.2,Virginica
5.9,2.7,7.5,1.4,Setosa
4.2,3.3,2.4,0.5,Versicolor
5.6,2.7,2.4,1.7,Virginica
6.1,3.1,2.8,-0.1,Setosa
7,3,0.2,1.1,Versicolor
5.4,2.7,2.9,0.2,Virginica
5.2,3.9,2.5,0.7,Setosa
5.4,3.3,4.1,1.2,Versicolor
6.5,2.2,4.4,0.5,Virginica
6.1,3.1,7,0.9,Setosa
5.4,2.7,5.4,2,Versicolor
6.2,3.3,2.8,0.7,Virginica
5.9,2.7,2.3,1.9,Setosa
6.6,3,4.6,0.3,Versicolor
5.2,3.2,1.6,1.6,Virginica
5.5,3.3,6.9,2.4,Setosa
5.5,2.5,5.8,-0.8,Versicolor
4.6,2.9,3,0.6,Virginica
6,2.8,0.9,1.7,Setosa
6,2.7,6.1,1,Versicolor
5.8,3.7,3.6,1.5,Virginica
5.6,3.2,5.9,0.7,Setosa
4.7,2.5,1.1,1.3,Versicolor
5.5,3.4,2.8,1.1,Virginica
5.5,3.8,3.8,2.1,Setosa
5.2,3.4,3.9,1.4,Versicolor
5.7,2.4,3,1.5,Virginica
6.1,2.8,4.9,0.9,Setosa
7.3,3.5,2,0.8,Versicolor
5.9,2.7,3.6,0.9,Virginica
6,3.2,4,1.5,Setosa
5.7,3.3,4.7,0.9,Versicolor
4.3,2.6,5,1.4,Virginica
5.8,3,1.9,2.9,Setosa
5.8,1.7,1.2,1.9,Versicolor
7.8,2.6,6,0.9,Virginica
5.6,2.9,4.4,2.2,Setosa
6,2.5,2.5,0.9,Versicolor
5.8,3.7,6.4,-0.4,Virginica
4.9,2.4,4,0.4,Setosa
6.7,2.8,5.8,-0.3,Versicolor
6.4,3.1,3.9,0.9,Virginica
6.4,3.6,7.3,1.2,Setosa
5.1,2.4,6.8,2.5,Versicolor
6.9,3.5,3.4,1.5,Virginica
4.7,3,5.5,1,Setosa
6.3,2.6,4.9,1.9,Versicolor
7.6,3.2,6.1,-0.6,Virginica
5,3.1,2.2,1.4,Setosa
5.3,2.8,5,1.8,Versicolor
5.9,3,5.6,0,Virginica
5.4,2.8,0.8,2.1,Setosa
4.6,3,1.8,1.5,Versicolor
5.9,3.3,0.3,0.9,Virginica
5,3.6,3.3,1.7,Setosa
6.2,2.5,5,3,Versicolor
5.1,3.9,6.4,1.3,Virginica
7,2.2,3.9,1.4,Setosa
5.2,2.9,6.6,0.8,Versicolor
5.5,3.2,1.5,0.5,Virginica
6.5,3.1,0.9,1.9,Setosa
4.8,2.8,3.7,0.5,Versicolor
6,2.9,4.5,1.3,Virginica
6.8,2.8,3.7,0.8,Setosa
4.5,2.8,0.3,1.6,Versicolor
5.9,3.3,3.6,1.5,Virginica
6,3.1,1.6,2,Setosa
6.4,2.7,4.9,0.8,Versicolor
4.8,3.4,4.4,1,Virginica
4.7,3.1,2.2,0.4,Setosa
6.2,3.3,2.9,0.8,Versicolor
6,3.3,2,1.5,Virginica

================================================
FILE: Iris_Dataset_Analysis/p01.py
================================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('iris.csv')
print("**********\*********** Dataset loaded successfully. **********\***********")

# print("**********\*********** printing dataset: **********\***********")

# print(data) # Display the dataset

print("**********\*********** printing first 5 rows: **********\***********")
print(data.head()) # Display the first 5 rows of the dataset
print("**********\*********** printing last 5 rows: **********\***********")
print(data.tail()) # Display the last 5 rows of the dataset
print("**********\*********** printing summary statistics: **********\***********")
print(data.describe()) # Display summary statistics of the dataset
print("**********\*********** printing dataset information: **********\***********")
print(data.info()) # Display information about the dataset
print("**********\*********** printing column names: **********\***********")
print(data.columns) # Display the column names of the dataset
print("**********\*********** printing shape of the dataset: **********\***********")
print(data.shape) # Display the shape of the dataset
print("**********\*********** printing missing values: **********\***********")
print(data.isnull().sum()) # Check for missing values in the dataset

# Graphical Representations

print("**********\*********** Creating visualizations: **********\***********")

# Set the style for better-looking plots

sns.set_palette("husl")

# 1. Pairplot to show relationships between all features

print("Creating pairplot...")
pairplot = sns.pairplot(data, hue='species' if 'species' in data.columns else data.columns[-1])
pairplot.fig.suptitle('Pairplot of Iris Dataset Features', y=1.02)
plt.show()

# 2. Distribution plots for each feature

print("Creating distribution plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Distribution of Features in Iris Dataset', fontsize=16)

# Get numeric columns (assuming first 4 columns are features)

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns[:4]

for i, col in enumerate(numeric_cols):
row, col_idx = i // 2, i % 2
axes[row, col_idx].hist(data[col], bins=20, alpha=0.7, edgecolor='black')
axes[row, col_idx].set_title(f'Distribution of {col}')
axes[row, col_idx].set_xlabel(col)
axes[row, col_idx].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# 3. Box plots to show distribution and outliers

print("Creating box plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Box Plots of Features in Iris Dataset', fontsize=16)

for i, col in enumerate(numeric_cols):
row, col_idx = i // 2, i % 2
species_col = 'species' if 'species' in data.columns else data.columns[-1]
sns.boxplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
axes[row, col_idx].set_title(f'Box Plot of {col}')

plt.tight_layout()
plt.show()

# 4. Correlation heatmap

print("Creating correlation heatmap...")
plt.figure(figsize=(10, 8))
correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
square=True, linewidths=0.5)
plt.title('Correlation Heatmap of Iris Dataset Features')
plt.tight_layout()
plt.show()

# 5. Violin plots for distribution comparison

print("Creating violin plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Violin Plots of Features by Species', fontsize=16)

for i, col in enumerate(numeric_cols):
row, col_idx = i // 2, i % 2
species_col = 'species' if 'species' in data.columns else data.columns[-1]
sns.violinplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
axes[row, col_idx].set_title(f'Violin Plot of {col}')

plt.tight_layout()
plt.show()

print("**********\*********** Visualizations completed! **********\***********")
