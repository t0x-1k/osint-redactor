# OSINT De-Redactor

A Python CLI tool to generate potential email addresses from seed usernames and test them across domains using [holehe](https://github.com/megadose/holehe) for OSINT investigations.

---

## Features

- Generates permutations of usernames using custom **seeds** and **suffixes**
- Appends to user-defined **email domains**
- Validates the existence of those emails using `holehe`
- Outputs results to a structured JSON file
- CLI-driven and highly configurable

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/osint-dereactor.git
cd osint-dereactor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python osint_de_redactor.py
```

> Make sure `holehe` is installed:
>
> ```bash
> pip install holehe
> ```

---

## 🛠️ Usage

Run the script with custom inputs via command-line arguments:

```bash
python osint_de_redactor.py \
  --seeds denni lucas aarti \
  --suffixes 123 2020 admin \
  --domains gmail.com protonmail.ch \
  --output results.json
```

### Arguments

| Argument       | Type     | Description                                 |
|----------------|----------|---------------------------------------------|
| `--seeds`      | List     | Base usernames (e.g., `aarti denni`)        |
| `--suffixes`   | List     | Suffixes to append (e.g., `123 admin`)      |
| `--domains`    | List     | Email domains (e.g., `gmail.com`)           |
| `--output`     | Path     | Output file for JSON results (default: `results_dereacted.json`) |

---

## 🧪 Output

The tool saves results as JSON like:

```json
[
  {
    "email": "denni123@gmail.com",
    "status": "✅"
  },
  {
    "email": "lucas.admin@protonmail.ch",
    "status": "❌"
  }
]
```

- ✅ indicates an active account (according to holehe)
- ❌ means not found or unavailable
- `Error` indicates a timeout or subprocess issue

---

## Example

```bash
python osint_de_redactor.py \
  --seeds adam aartik \
  --suffixes 01 1989 \
  --domains hotmail.com beaconite.edu.pk
```

---

## Notes & Warnings

- `holehe` must be installed and working.
- Some services might rate-limit or block too many requests.
- Always use responsibly and within legal limits.

---

## 📄 License

MIT © 2025 YourName

---

## Acknowledgments

- [holehe](https://github.com/megadose/holehe) for email enumeration
- [tqdm](https://github.com/tqdm/tqdm) for progress bars





