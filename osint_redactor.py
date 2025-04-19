import subprocess
import itertools
import json
import argparse
from pathlib import Path
from typing import List, Dict
from tqdm import tqdm


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Email permutation OSINT tool using holehe.")
    parser.add_argument("--seeds", nargs="+", required=True, help="Seed names (e.g., denni lucas aarti)")
    parser.add_argument("--suffixes", nargs="+", required=True, help="Suffixes to append (e.g., 123 2020 admin)")
    parser.add_argument("--domains", nargs="+", required=True, help="Email domains (e.g., gmail.com protonmail.ch)")
    parser.add_argument("--output", type=Path, default=Path("results_dereacted.json"), help="Output JSON file")
    return parser.parse_args()

def holehe_check(email: str) -> str:
    try:
        result = subprocess.run(
            ["holehe", email],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=10
        )
        return "success" if b'[+]' in result.stdout else "error"
    except Exception:
        return "Error"

def generate_candidates(seeds: List[str], suffixes: List[str]) -> List[str]:
    candidates = []
    for seed in seeds:
        for suffix in suffixes:
            candidates.extend([
                f"{seed}{suffix}",
                f"{seed}.{suffix}",
                f"{seed}_{suffix}"
            ])
        candidates.append(seed)
    return candidates

def test_candidates(seeds: List[str], suffixes: List[str], domains: List[str]) -> List[Dict[str, str]]:
    candidates = generate_candidates(seeds, suffixes)
    total = len(candidates) * len(domains)

    print(f"\n Testing {total} permutations...\n")
    results = []

    for username in tqdm(candidates, desc="Testing emails"):
        for domain in domains:
            email = f"{username}@{domain}"
            status = holehe_check(email)
            results.append({"email": email, "status": status})
    return results

def save_results(results: List[Dict[str, str]], output_file: Path) -> None:
    output_file.write_text(json.dumps(results, indent=2))
    print(f"\n Results saved to {output_file.resolve()}")

def main():
    args = parse_args()
    print(" OSINT De-Redactor Started")

    results = test_candidates(args.seeds, args.suffixes, args.domains)
    save_results(results, args.output)


if __name__ == "__main__":
    main()
