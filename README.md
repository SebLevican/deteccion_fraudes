# Data Exploration and Preprocessing for Fraud Detection

This project focuses on the exploration, preprocessing, and visualization of data related to fraud detection in financial applications. Below is an outline of the process:

## Library Installation

The following Python libraries are used:

- **Pandas**: For data manipulation and analysis.
- **Seaborn and Matplotlib**: For data visualization.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For implementing machine learning models.
- **Imbalanced-learn**: For handling class imbalance in data.
- **Pickle**: For saving and loading Python objects.
- **Scipy**: For performing statistical tests.

Additionally, custom functions for generating plots and training models are contained in the `fx_graficos_fraude.py` and `fx_modelos.py` files.

## Process Overview

1. **Data Loading:**
   - The main dataset `Base.csv` is loaded, and a preview of the dataframe is printed.

2. **Handling Missing Values:**
   - Specific values (-1) are replaced with `NaN` in certain columns.
   - Columns with too many missing values are removed.
   - Records with `NaN` values are eliminated.

3. **Data Transformation:**
   - Numeric classes are converted to strings to facilitate the visualization and processing of categorical variables.
   - Data types are adjusted, such as converting `float` variables to `int` where appropriate.

4. **Exploratory Data Analysis (EDA):**
   - Bar plots and box plots are generated to analyze the distribution of categorical and numerical variables.
   - The dataset is statistically described for both categorical and numerical variables.

5. **Visualization:**
   - Custom functions are used to generate subplots that allow for the visualization of multiple variables in a single graph.
   - Graphs are described and titled to facilitate data interpretation.

6. **Numerical Variable Analysis:**
   - Numerical variables with fewer than 12 unique values and more than 12 unique values are separately identified and analyzed.
   - Graphs are generated to better visualize the distribution of these variables.

## Results

After preprocessing, the original dataset, which contained 1 million records, was significantly reduced due to the elimination of null values. The final result is a dataframe with a considerable percentage of valid data ready for further analysis and modeling.

This process is crucial to ensure that the subsequent machine learning model is trained with clean and representative data.

## Considerations

- This analysis was conducted while ignoring library warnings.
- The plots are configured using the `Seaborn` style and the `Set2` color palette.

For more details on the implementation of machine learning models or the graphic functions used, refer to the `fx_graficos_fraude.py` and `fx_modelos.py` files.
