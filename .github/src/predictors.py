from typing import List, Dict, Any

PAPA_PROPENSITY = {
    'F': 0.118, 'W': 0.108, 'Y': 0.106, 'Q': 0.088, 'N': 0.087,
    'M': 0.035, 'C': 0.012, 'H': -0.003, 'A': -0.016, 'I': -0.027,
    'G': -0.032, 'V': -0.040, 'S': -0.041, 'T': -0.042, 'L': -0.063,
    'R': -0.076, 'D': -0.098, 'E': -0.112, 'P': -0.144, 'K': -0.165
}

def scan_qn_density(sequence: str, window_size: int = 80) -> List[Dict[str, Any]]:
    
    results = []
    seq_len = len(sequence)

    if seq_len < window_size:
        return results

    for i in range(seq_len - window_size + 1):
        window = sequence[i : i + window_size]
        qn_count = window.count('Q') + window.count('N')
        qn_fraction = qn_count / window_size
        
        results.append({
            "start": i + 1,
            "end": i + window_size,
            "qn_count": qn_count,
            "qn_fraction": round(qn_fraction, 4)
        })
    return results

def calculate_papa_score(sequence: str, window_size: int = 80) -> List[Dict[str, Any]]:
    
    results = []
    seq_len = len(sequence)

    if seq_len < window_size:
        return results

    for i in range(seq_len - window_size + 1):
        window = sequence[i : i + window_size]
        score = sum(PAPA_PROPENSITY.get(aa, 0.0) for aa in window) / window_size

        results.append({
            "start": i + 1,
            "end": i + window_size,
            "papa_score": round(score, 4)
        })
    return results
