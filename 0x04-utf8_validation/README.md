# 0x04. UTF-8 Validation

## Overview
This project, **UTF-8 Validation**, is part of the ALX Software Engineering program. The objective is to develop a Python program that verifies whether a given data set represents a valid UTF-8 encoding. This task requires a solid understanding of bitwise operations, the UTF-8 encoding scheme, and list manipulation in Python.

The project will begin on **October 28, 2024, at 6:00 AM** and conclude on **November 1, 2024, at 6:00 AM**. An auto-review will occur at the deadline, and the project will be graded on its accuracy in validating UTF-8 encoded data.

## Requirements
- **Language:** Python (version 3.4.3).
- **OS:** Ubuntu 20.04 LTS.
- **Coding Standards:** Follow PEP 8 style guidelines (version 1.7.x).
- **File Requirements:**
  - Each file must end with a new line.
  - The first line of every file must be `#!/usr/bin/python3`.
  - A `README.md` file is mandatory at the root of the project folder.
  - All files should be executable.

## Key Concepts and Skills
To complete this project, you’ll need knowledge in the following areas:

### Bitwise Operations in Python
- Understanding and using bitwise operators like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
- Applying these operators to validate UTF-8 encoding.

### UTF-8 Encoding Scheme
- Familiarity with the rules of UTF-8 encoding, particularly how characters are encoded into 1 to 4 bytes.
- Recognizing the patterns that determine a valid UTF-8 encoded character.

### Data Representation
- Working with data at the byte level by handling the least significant bits of integers to simulate byte data.

### List Manipulation in Python
- Using lists for data storage and retrieval.
- Iterating over lists, accessing elements, and using list comprehensions.

### Boolean Logic
- Applying logical reasoning to ensure accurate data validation.

## Resources
Here are some helpful resources to deepen your understanding of UTF-8 encoding and Python bitwise operations:

1. **Python Bitwise Operators**: [Python Bitwise Operators Documentation](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
2. **UTF-8 Encoding**: [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
3. **Understanding Unicode and Character Sets**:
   - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
   - [Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)
4. **Python Lists**: [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)

## Project Task
### UTF-8 Validation Function
Write a method that validates if a data set represents a valid UTF-8 encoding:

**Prototype**: `def validUTF8(data)`
- **Input**: `data` (a list of integers)
- **Output**: `True` if `data` is valid UTF-8 encoding; otherwise, return `False`.

#### Example
```python
data = [65]
print(validUTF8(data))  # Expected output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Expected output: False
