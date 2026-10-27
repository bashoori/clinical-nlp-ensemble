"""Flag uncertain or conflicting model predictions."""


def needs_review(
    rule_prediction: int | None,
    model_prediction: int | None,
    probability: float | None = None,
    margin: float = 0.10,
) -> bool:
    if rule_prediction is None or model_prediction is None:
        return True
    if rule_prediction != model_prediction:
        return True
    if probability is not None and abs(probability - 0.5) <= margin:
        return True
    return False
