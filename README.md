# Python TOTP 2FA Tool

This is a simple Python tool for generating and verifying TOTP-based two-factor authentication (2FA) codes using the `pyotp` library.

It allows you to:
- Generate a new shared secret (16 characters)
- Display the current 6-digit TOTP code
- Test a user-entered 2FA code against the generated or provided shared secret

## Features

Random shared secret generation  
TOTP code generation (6-digit PIN)  
Verification of user input against current TOTP code  

## Requirements

- Python 3.6+
- `pyotp` package

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python your_script_name.py
```

You will be prompted to either:

1. **Generate** a new shared secret (which will immediately display a valid TOTP code)  
2. **Test** an existing shared secret by entering it manually and verifying a TOTP code

## Example

```
Would you like to generate a new shared secret or test an existing one? (1 = generate, 2 = test): 1
Randomly generated shared secret (16 characters): Xk8T2...
Your current TOTP code is: 123456
```

## Notes

- TOTP codes change every 30 seconds.
- For production use, it is recommended to store secrets securely and optionally display a QR code to scan with an authenticator app (e.g. Google Authenticator, Authy).

## License

MIT – feel free to use and modify.