from pathlib import Path
from typing import List, Dict
from Bio import SeqIO

def parse_fasta(file_path: str | Path) -> List[Dict[str, str]]:
    
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"FASTA file not found: {file_path}")

    records = []
    for record in SeqIO.parse(path, "fasta"):
        clean_seq = "".join([aa for aa in str(record.seq).upper() if aa in "ACDEFGHIKLMNPQRSTVWY"])
        records.append({
            "id": record.id,
            "description": record.description,
            "sequence": clean_seq,
            "length": len(clean_seq)
        })
    return records
