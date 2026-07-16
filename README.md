<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/b/b6/Wikipedia-logo-v2-hi.svg" alt="Hindi Wikipedia Logo" width="130" />
</p>

<h1 align="center">Puspaaamm-bot</h1>

<p align="center">
  <strong>An automated, non-destructive diagnostic tool for identifying orthographical and diacritic discrepancies on Hindi Wikipedia.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Platform-Wikimedia%20Toolforge-006699?style=flat-square&logo=wikipedia&logoColor=white" alt="Platform" />
  <img src="https://img.shields.io/badge/Framework-Pywikibot-339973?style=flat-square&logo=git&logoColor=white" alt="Framework" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License" />
</p>

---

## Executive Summary

`Puspaaamm-bot` is a specialized quality-assurance script designed to parse Hindi Wikipedia articles and flag common typographic, spelling, and *matra* (diacritic) errors. Engineered with a strict **Read-Only / Find-Only** architecture, the script completely eliminates the risk of automated edit conflicts or corruption by generating static local reports for manual editor verification.

---

## Key Architectural Features

* **Advanced Pattern Matching:** Uses optimized regular expressions paired with strict word boundaries (`\b`) to eliminate false positives in proper nouns or complex compound words.
* **Non-Destructive Operation:** Fully compliant with Wikimedia's bot policies. The bot does not possess write privileges in this configuration; it operates exclusively as a diagnostic scanner.
* **Comprehensive Orthographical Coverage:**
  * **Vowel Length Discrepancies:** Detects errors involving short/long vowels ($i$/$ī$ and $u$/$ū$) such as `आशिर्वाद` (incorrect) vs. `आशीर्वाद` (correct).
  * **Anusvara & Consonant Clusters:** Scans for structural spelling mistakes like `उज्वल` vs. `उज्ज्वल`.
  * **Nukta & Semi-Vowels:** Identifies missing or misplaced diacritic marks that alter semantic meaning.

---

## Repository Structure

```filepath
├── find_typos.py         # Primary scanning script containing regex dictionary and execution logic
├── user-config.py        # Pywikibot runtime parameters mapping to the Hindi Wikipedia family
├── user-password.py      # Secure authentication configuration (local execution credentials)
├── requirements.txt      # Project dependency manifest
└── README.md             # Project documentation
