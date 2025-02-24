# README

This repository contains a basic workflow for analyzing microarray transcriptomics data ([GSE7621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7621)) 
to identify differentially expressed genes (DEGs) and using those DEGs for machine learning classification tasks.

## Overview

1. **Data Acquisition**: Microarray transcriptomics data is collected, usually in the form of raw or processed gene expression matrices/\.
2. **Differential Expression Analysis**:
- Perform normalization and quality control steps (e.g., removing outliers, batch correction).
- Use statistical methods (e.g., `limma`) to identify DEGs between the group of interest (e.g., PD vs. normal).
- Filter DEGs based on log fold-change, adjusted p-values, or other relevant criteria.
3. **Feature Selection**: The DEGs serve as candidate features for downstream machine learning models.  

4. **Machine Learning**:
- Split data into features (DEG expression values) and labels (PD vs. normal).
- Evaluate multiple classification algorithms (e.g., Logistic Regression, SVM etc.,) via cross-validation.
- Find the better model and Fine-tune model hyperparameters (e.g., using GridSearchCV).
- Assess performance with accuracy, F1-score, ROC-AUC, and other relevant metrics.
5. **Result Interpretation**:
- Obtain confusion matrices for a more comprehensive evaluation.
- Investigate model coefficients or feature importance to understand which DEGs contribute most to classification.
