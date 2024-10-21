
# Simplified DES Encryption/Decryption Script

A Python implementation of a simplified version of the Data Encryption Standard (DES) algorithm for encrypting and decrypting hexadecimal numbers. The program performs encryption using a provided key and also offers the option to decrypt the result back to its original form.

## Features
- **Hexadecimal to Binary Conversion**: Converts the hexadecimal input to binary format.
- **Binary to Hexadecimal Conversion**: Converts binary back to hexadecimal after encryption.
- **Simplified DES Process**: Utilizes functions like Initial Permutation (IP), Expansion, S-box, and Final Permutation (Inverse IP) to simulate DES rounds.
- **Key Generation**: Generates subkeys using left shifts for each encryption round.

## Requirements
- Python 3.x

## How to Run

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the script**:
   ```bash
   python3 des.py
   ```

4. **Provide inputs when prompted**:
   - Enter a **hexadecimal number** to encrypt.
   - Enter a **key** (also in hexadecimal format).

5. **View the output**:
   - The script will display the encrypted result.
   - You will then be asked whether you want to decrypt the result. Enter 'y' to decrypt and view the original input.

## Example Usage
```bash
your hexadecimal number: 
3A4F
your key: 
A1B2
# Encrypted Output:
FA1D
decrypt as well?: (y/n)
y
# Decrypted Output:
3A4F
```

## Key Functions

- `hex_to_bin(number)`: Converts a hexadecimal number to binary.
- `bin_to_hex(number)`: Converts a binary number to hexadecimal.
- `encrypt_des(plain, key)`: Encrypts a plain text using DES algorithm.
- `decrypt_des(cypher, key)`: Decrypts a cypher text back to plain text.
- Various helper functions like `ip()`, `pc1()`, `xorr()`, `f()` simulate key steps in the DES encryption process.

## Issues
- Cannot run in low-light conditions.
- Depth sensing is not implemented, so the head position must remain fixed.
- Glasses may cause interference due to light reflections on the monitor.

## Author
**Md. Rafid Haque**  
ID: 1700 420 72  
E-mail: rafidhaque@iut-dhaka.edu
