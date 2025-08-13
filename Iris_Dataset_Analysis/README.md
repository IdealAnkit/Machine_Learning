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

## Detailed Visualization Section (Lines 24-92)

### 1. Style Configuration (Lines 26-27)

```python
sns.set_palette("husl")
```

- Sets the color palette to "husl" (Hue-Saturation-Lightness) for better visual distinction
- Provides aesthetically pleasing colors for different species in plots

### 2. Pairplot Visualization (Lines 29-32)

```python
print("Creating pairplot...")
pairplot = sns.pairplot(data, hue='species' if 'species' in data.columns else data.columns[-1])
pairplot.fig.suptitle('Pairplot of Iris Dataset Features', y=1.02)
plt.show()
```

**Purpose**: Creates a matrix of scatter plots showing relationships between all feature pairs

- **What it shows**:
  - Diagonal: Distribution histograms for each feature
  - Off-diagonal: Scatter plots between feature pairs
  - Color coding by species for pattern identification
- **Why it's useful**: Helps identify correlations, clusters, and separability between species

### 3. Distribution Histograms (Lines 34-48)

```python
print("Creating distribution plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Distribution of Features in Iris Dataset', fontsize=16)

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns[:4]

for i, col in enumerate(numeric_cols):
    row, col_idx = i // 2, i % 2
    axes[row, col_idx].hist(data[col], bins=20, alpha=0.7, edgecolor='black')
    axes[row, col_idx].set_title(f'Distribution of {col}')
    axes[row, col_idx].set_xlabel(col)
    axes[row, col_idx].set_ylabel('Frequency')
```

**Purpose**: Shows frequency distribution of each numerical feature

- **Technical Details**:
  - Creates 2x2 subplot grid
  - `numeric_cols`: Automatically selects first 4 numeric columns
  - `enumerate()`: Provides both index and column name
  - `row, col_idx = i // 2, i % 2`: Calculates subplot position using integer division
  - `bins=20`: Divides data into 20 intervals
  - `alpha=0.7`: Sets transparency for better visual appeal
- **Why it's useful**: Identifies data distribution patterns (normal, skewed, bimodal)

### 4. Box Plots (Lines 50-61)

```python
print("Creating box plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Box Plots of Features in Iris Dataset', fontsize=16)

for i, col in enumerate(numeric_cols):
    row, col_idx = i // 2, i % 2
    species_col = 'species' if 'species' in data.columns else data.columns[-1]
    sns.boxplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'Box Plot of {col}')
```

**Purpose**: Displays statistical summaries and outliers for each feature by species

- **What box plots show**:
  - Box: Interquartile range (25th to 75th percentile)
  - Line in box: Median (50th percentile)
  - Whiskers: Data range (excluding outliers)
  - Dots: Outliers beyond 1.5 × IQR
- **Species comparison**: Shows how feature distributions differ between iris species
- **Why it's useful**: Identifies outliers and compares feature distributions across species

### 5. Correlation Heatmap (Lines 63-70)

```python
print("Creating correlation heatmap...")
plt.figure(figsize=(10, 8))
correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=0.5)
plt.title('Correlation Heatmap of Iris Dataset Features')
```

**Purpose**: Visualizes correlation coefficients between all numerical features

- **Technical Details**:
  - `correlation_matrix`: Calculates Pearson correlation coefficients (-1 to +1)
  - `annot=True`: Shows correlation values in each cell
  - `cmap='coolwarm'`: Blue for negative, red for positive correlations
  - `center=0`: Centers colormap at zero correlation
  - `square=True`: Makes cells square-shaped
- **Interpretation**:
  - Values close to +1: Strong positive correlation
  - Values close to -1: Strong negative correlation
  - Values close to 0: No linear correlation
- **Why it's useful**: Identifies which features are related and might be redundant

### 6. Violin Plots (Lines 72-82)

```python
print("Creating violin plots...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Violin Plots of Features by Species', fontsize=16)

for i, col in enumerate(numeric_cols):
    row, col_idx = i // 2, i % 2
    species_col = 'species' if 'species' in data.columns else data.columns[-1]
    sns.violinplot(data=data, x=species_col, y=col, ax=axes[row, col_idx])
    axes[row, col_idx].set_title(f'Violin Plot of {col}')
```

**Purpose**: Combines box plot information with distribution shape

- **What violin plots show**:
  - Width: Data density at different values
  - White dot: Median
  - Thick black line: Interquartile range
  - Shape: Distribution curve (like a rotated histogram)
- **Advantages over box plots**: Shows complete distribution shape, not just summary statistics
- **Why it's useful**: Reveals distribution patterns (e.g., bimodal, skewed) that box plots miss

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
  #   M a c h i n e _ L e a r n i n g 
   
   
