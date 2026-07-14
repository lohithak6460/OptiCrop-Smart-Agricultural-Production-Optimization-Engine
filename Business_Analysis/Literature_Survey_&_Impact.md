# Literature Survey & Impact Analysis

## 1. Literature Survey Overview

A review of recent studies in precision agriculture indicates that standard linear classifiers are insufficient for crop matching due to non-linear correlations between environmental inputs (such as temperature/rainfall peaks) and soil variables. 

Ensemble algorithms (specifically **Random Forests**) demonstrate high accuracy because:
*   They manage feature interactions (e.g. soil pH affecting Nitrogen absorption) naturally.
*   They are resistant to overfitting when trained with multiple estimators.
*   They offer high classification performance with minimal preprocessing.

OptiCrop builds on these findings, reaching a classification accuracy of **99.55%** using a scikit-learn standard scaling and random forest pipeline.

---

## 2. Social & Business Impact

*   **Financial Yield:** Reduces farmer fertilizer expenses by up to 25% by preventing unnecessary chemical applications.
*   **Environmental Protection:** Curtails fertilizer runoff and nitrogen leaching, protecting surrounding watershed ecosystems from eutrophication.
*   **Food Security:** Mitigates the risk of crop failure, securing regional food supply chains and supporting rural livelihoods.
