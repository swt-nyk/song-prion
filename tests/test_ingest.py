import pytest
from src.predictors import scan_qn_density, calculate_papa_score

def test_qn_density_calculation():
    test_seq = "QQQQNNNN" * 10  
    scores = scan_qn_density(test_seq, window_size=80)

    assert len(scores) == 1
    assert scores[0]["qn_fraction"] == 1.0

def test_short_sequence():
    test_seq = "ACDEF"
    scores = scan_qn_density(test_seq, window_size=80)
    assert len(scores) == 0
