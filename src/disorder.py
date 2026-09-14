from typing import List, Dict, Any

DISORDER_PROPENSITY = {
    'P': 1.00, 'E': 0.78, 'S': 0.70, 'Q': 0.61, 'K': 0.59,
    'A': 0.45, 'G': 0.44, 'D': 0.41, 'T': 0.41, 'R': 0.39,
    'N': 0.28, 'H': 0.23, 'V': -0.14, 'L': -0.21, 'I': -0.23,
    'F': -0.24, 'Y': -0.27, 'W': -0.33, 'M': -0.37, 'C': -0.72
}

def calculate_disorder_score(sequence: str, window_size: int = 80) -> List[Dict[str, Any]]:
    results = []
    seq_len = len(sequence)

    if seq_len < window_size:
        return results

    for i in range(seq_len - window_size + 1):
        window = sequence[i : i + window_size]
        score = sum(DISORDER_PROPENSITY.get(aa, 0.0) for aa in window) / window_size

        results.append({
            "start": i + 1,
            "end": i + window_size,
            "disorder_score": round(score, 4)
        })
    return results
