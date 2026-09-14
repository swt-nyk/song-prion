import argparse
import json
from pathlib import Path
from src.pipeline import analyze_proteome

def main():
    parser = argparse.ArgumentParser(description="Scan proteomes for prion-like domains and intrinsic disorder.")
    parser.add_argument("fasta", type=str, help="Path to input FASTA file")
    parser.add_argument("-w", "--window-size", type=int, default=80, help="Sliding window size (default: 80)")
    parser.add_argument("-o", "--output", type=str, default="results.json", help="Output JSON path")
    args = parser.parse_args()

    results = analyze_proteome(args.fasta, window_size=args.window_size)

    output_path = Path(args.output)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Analysis complete for {len(results)} sequence(s). Output saved to {output_path}")

if __name__ == "__main__":
    main()
