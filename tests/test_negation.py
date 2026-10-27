from src.rule_based import predict_lvi
from src.ensemble import majority_vote


def test_positive_lvi():
    assert predict_lvi("Lymphovascular invasion is present") == 1


def test_negative_lvi():
    assert predict_lvi("No lymphovascular invasion") == 0


def test_uncertain_lvi():
    assert predict_lvi("LVI cannot be assessed") is None


def test_majority_vote():
    assert majority_vote([1, 1, 0]) == 1
    assert majority_vote([0, 0, 1]) == 0


def test_tied_vote():
    assert majority_vote([1, 0]) is None
