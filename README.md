## HFCrypt

Secure your code on Hugging Face Spaces. Encrypt and protect your proprietary machine learning applications.

[GitHub](https://github.com/hfcrypt/hfcrypt) | [Website](https://hfcrypt.github.io/)

This is HFCrypt v2. The legacy (v1) version is available on the `old-v1` branch.

## Usage

```bash
pip install hfcrypt
```

```bash
hfcrypt path_to_your_app output_folder
```

If you plan to push your app to a Hugging Face Space (you will be asked during the process), you can set the output folder to a temporary directory:

```bash
hfcrypt path_to_your_app /tmp/hfcrypt_output
```

## Coming Soon

- GitHub Actions workflow to automatically encrypt your app and push to HF when you push to a repo

## License

MIT