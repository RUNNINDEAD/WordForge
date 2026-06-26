# 🔐 WordForge

Generate thousands of password variations from one or more keywords.

WordForge is a Python-based password permutation generator that creates realistic password combinations by mixing:

* Different capitalization styles
* Common number patterns
* Special characters
* Reversed words
* Multiple placement combinations

The generated passwords are saved to a text file for further use.

## Features

* Keyword-based password generation
* Multiple capitalization styles
* Common numeric suffixes
* Special character combinations
* Reversed keyword generation
* Duplicate removal
* Randomized output
* Configurable maximum password count

## Installation

```bash
git clone https://github.com/yourusername/WordForge.git
cd WordForge
```

## Usage

Run the script:

```bash
python wordforge.py
```

Example:

```text
Enter keywords separated by commas:
john,dog,football
```

The generated passwords will be saved as:

```text
passwords.txt
```

## Example Output

```text
John123!
john2025@
DOG007#
!Football12
321nhoJ$
```

## Configuration

You can customize:

* Number patterns
* Special characters
* Capitalization styles
* Maximum generated passwords

```python
MAX_PASSWORDS = 1000000
```

## Requirements

* Python 3.x

No external libraries are required.

## Project Structure

```text
WordForge/
│
├── wordforge.py
├── generated_passwords.txt
└── README.md
```

## Disclaimer

This project is intended for educational purposes, password auditing, and authorized security testing only. Use it only on systems and accounts you own or have explicit permission to test.

## License

ZeroScope Solutions License
