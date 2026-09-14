import pytest
from src.pipeline import analyze_proteome

def test_analyze_proteome(tmp_path):
    fasta_file = tmp_path / "sample.fasta"
    fasta_file.write_text(
        ">seq1 Sample Protein\n"
        "QQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNNQQQQNNNN\n"
    )

    results = analyze_proteome(fasta_file, window_size=80)

    assert len(results) == 1
    assert results[0]["id"] == "seq1"
    assert len(results[0]["qn_windows"]) == 1
    assert len(results[0]["papa_windows"]) == 1
    assert len(results[0]["disorder_windows"]) == 1
