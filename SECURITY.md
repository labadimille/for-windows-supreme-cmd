## Security policy

If you believe you have found a security vulnerability in this project, please
follow these steps:

1. Do not create a public issue with the vulnerability details.
2. Email the project owner at labad@example.local with a clear description and
   steps to reproduce. Include proof-of-concept if available.
3. Rotate any leaked API keys immediately and replace them in
   `config/api_keys.json` (do not commit the real keys).

Sensitive files (such as `config/api_keys.json`) must never be committed to
public repositories. This repo includes `config/api_keys.example.json` as a
template for local configuration.
