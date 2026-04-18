# Piggy-Latin-Translator 🐷

A robust, edge-case-sensitive Pig Latin translator designed to solve the common syntax errors and rule-breaking found in standard implementations.

## Purpose
While many Pig Latin translators exist, they often fail at complex linguistic nuances. This project focuses on **accuracy** and **preservation**, ensuring that the rules of the language game are followed without breaking the visual structure of the original text.

## Key Features
- **Consonant Cluster Awareness:** Correctly handles multi-consonant onsets (e.g., 'string' becomes 'ingstray', not 'tringsay').
- **The "Y" Paradox:** Contextually treats 'y' as a vowel when it follows a consonant (e.g., 'rhythm' or 'my').
- **Formatting Preservation:** Maintains original capitalization and keeps punctuation at the end of the translated word.
- **Vowel Logic:** Standardizes the use of the `-way` suffix for words starting with a, e, i, o, or u.

## Translation Logic
1. **Vowel Start:** If a word starts with `a, e, i, o, u`, the suffix `-way` is appended.
2. **Consonant Start:** All letters before the first vowel (including 'y' if it acts as the vowel) are moved to the end, followed by `-ay`.
3. **Punctuation:** Non-alphabetic characters are handled separately to ensure they don't get scrambled into the middle of the word.

## Examples
| Input | Output | Note |
| :--- | :--- | :--- |
| Apple | Appleway | Starts with vowel |
| School | Oolschay | Consonant cluster (sch) |
| Rhythm | Ythmrhay | 'Y' acting as vowel |
| Hello! | Ellohay! | Punctuation integrity |

## Future Roadmap
- [ ] Support for bulk translation via `.txt` files.
- [ ] A reverse translator (Pig Latin to English).
- [ ] Integration with a simple web interface.
