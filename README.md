# Parkinson's Disease Classification using DEGs from Microarray Data

This project demonstrates how to identify **differentially expressed genes (DEGs)** from microarray transcriptomics data and use them to build machine learning models that classify **Parkinson’s Disease (PD) vs. Healthy Controls**.

- Dataset: [GSE7621](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7621)
- Techniques: Limma DEG analysis, normalization, feature selection
- Models: Logistic Regression, LDA, QDA, SVM
- Metrics: Accuracy, F1-score, ROC-AUC, Confusion Matrix
- Goal: Build interpretable models that highlight biologically relevant gene features for PD detection

## Workflow Overview

1. **Data Acquisition**  
   - Downloaded microarray data from GEO (GSE7621)
   - Preprocessed to ensure quality and consistency

2. **Differential Expression Analysis**  
   - Applied `limma` to identify DEGs between PD and normal groups
   - Used log fold change and adjusted p-values to filter significant genes

3. **Feature Selection & Modeling**  
   - Selected DEGs as features for ML models
   - Trained Logistic Regression, LDA, QDA, SVM with cross-validation and GridSearchCV

4. **Model Evaluation**  
   - Evaluated performance using Accuracy, F1-score, ROC-AUC
   - Visualized confusion matrix and ROC curves

5. **Interpretation**  
   - Analyzed feature importance to identify key genes contributing to PD classification
   - Obtain confusion matrices for a more comprehensive evaluation.
   - Investigate model coefficients to understand which DEGs contribute most to classification.

## Results

The best-performing model (logistic regression) achieved:

- **Accuracy**: 93%
- **F1-score**: 0.92
- **Top 5 features**: GAS1, P2RX7, DNAJB6, THAP2, PPP4R2. These genes are involved in neuroinflammtory response (P2RX7), neuroprotection (GAS1), and peptide-binding chaperon (DNAJB6). Further investigation can be conducted from these genes.

## What I Learned

- How to perform DEG analysis on microarray data using R (`limma`) and Python
- Cross-discipline application: combining biological knowledge with ML modeling
- The importance of feature selection and model interpretability in biomedical datasets

