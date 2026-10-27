# Methodology

The task is binary LVI classification using report text and a verified
`lvi_label` target.

The rule-based baseline uses phrase patterns and can abstain.
The classical ML baseline uses TF-IDF and Logistic Regression.
The ensemble helper uses majority voting.

Transformer and LLM modules are placeholders only.

Report accuracy, precision, recall, F1-score and a confusion matrix.
Inspect false negatives and possible data leakage. This project is educational
and must not be used to guide patient care.
