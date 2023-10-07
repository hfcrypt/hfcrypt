# HFCrypt

Ever wanted to host something on Hugging Face Spaces but didn't want your code to be public? Look no further HFCrypt! HFCrypt encrypts your code to make your code closed-source! **TL;DR:** HFCrypt allows you to host closed-source apps on Hugging Face Spaces!

## Usage

HFCrypt is simple and easy to use! Just follow the following steps to get started!

### Preparation

Before you convert your app, you'll need to do a couple simple steps to prepare your app.

1. **IMPORTANT:** Set your app's external port to `7860`
   1. In Flask: `app.run('0.0.0.0', port=7860)`

### Conversion

Please place all the files for your app in the `app` folder.

**Make sure your main server file is named `app.py`!**

Then run:

```
python3 hfcrypt.py
```

### Deploy

Upload all the files in the `out` folder (**NOT** the folder itself, *only* the contents of the folder) to your Hugging Face Space.

Then, set the `HFCRYPT_KEY` secret (**NOT variable!**) to the key given in the CLI!

## Approaches

There are several different ways to achieve this:

* Store a GitHub token in Hugging Face Spaces Secrets and set the SDK to Docker. Have the Dockerfile clone from a GitHub private repository using the token. But this requires a GitHub repository and doesn't support large files. ([Forum thread](https://discuss.huggingface.co/t/share-app-url-without-sharing-the-files-and-version/26182))
* Use HFCrypt: Encrypt your source code, and save the key in Hugging Face Spaces

## Todo

* [ ] Allow user to auto-upload to Hugging Face Spaces using CLI

## License

License for the HFCrypt source code coming soon.

The default license for encrypted spaces (feel free to change this) is available [here](HESC.md).