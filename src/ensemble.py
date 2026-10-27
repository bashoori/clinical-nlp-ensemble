"""Ensemble decision helpers."""


def majority_vote(predictions: list[int | None]) -> int | None:
    votes = [p for p in predictions if p in (0, 1)]
    if not votes:
        return None

    positives = sum(votes)
    negatives = len(votes) - positives

    if positives == negatives:
        return None

    return 1 if positives > negatives else 0
