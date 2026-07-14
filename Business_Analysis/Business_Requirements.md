# Business Requirements Document (BRD)

## 1. Functional Requirements

*   **FR-1: Soil Profiling Input:** The system must accept seven input metrics: Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.
*   **FR-2: Target Selection:** The user must be allowed to choose between automatically optimizing for the ML-recommended crop or selecting a specific crop.
*   **FR-3: ML Crop Matcher:** The backend must predict the single most suitable crop using a trained classifier with a confidence score.
*   **FR-4: Deficiency Diagnostics:** The engine must compare current soil inputs against ideal targets and output deficiency/excess warnings.
*   **FR-5: Actionable Guidelines:** The system must generate custom chemical correction suggestions for nitrogen, phosphorus, potash, pH, and water.

---

## 2. Non-Functional Requirements

*   **NFR-1: Recommendation Accuracy:** The ML prediction accuracy must exceed 95% on evaluation splits.
*   **NFR-2: Response Time:** Page transitions and ML predictions must be completed in under 1.5 seconds.
*   **NFR-3: User Interface:** Implement a premium responsive dashboard designed with a dark emerald glassmorphism theme.
