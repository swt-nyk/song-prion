from pathlib import Path
from typing import List, Dict, Any
from src.ingest import parse_fasta
from src.predictors import scan_qn_density, calculate_papa_score

def analyze_proteome(fasta_path: str | Path, window_size: int = 80) -> List[Dict[str, Any]]:
    records = parse_fasta(fasta_path)
    results = []

    for record in records:
        seq = record["sequence"]
        qn_results = scan_qn_density(seq, window_size=window_size)
        papa_results = calculate_papa_score(seq, window_size=window_size)

        results.append({
            "id": record["id"],
            "description": record["description"],
            "length": record["length"],
            "qn_windows": qn_results,
            "papa_windows": papa_results
        })

    return results
