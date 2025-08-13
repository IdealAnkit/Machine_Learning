import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('iris.csv')
print("********************* Dataset loaded successfully. *********************")
# print("********************* printing dataset: *********************")
# print(data) # Display the dataset
print("********************* printing first 5 rows: *********************")
print(data.head()) # Display the first 5 rows of the dataset
print("********************* printing last 5 rows: *********************")
print(data.tail()) # Display the last 5 rows of the dataset
print("********************* printing summary statistics: *********************")
print(data.describe()) # Display summary statistics of the dataset
print("********************* printing dataset information: *********************")
print(data.info()) # Display information about the dataset
print("********************* printing column names: *********************")
print(data.columns) # Display the column names of the dataset
print("********************* printing shape of the dataset: *********************")
print(data.shape) # Display the shape of the dataset
print("********************* printing missing values: *********************")
print(data.isnull().sum()) # Check for missing values in the dataset

# Graphical Representations
print("********************* Creating visualizations: *********************")

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

print("********************* Visualizations completed! *********************")
