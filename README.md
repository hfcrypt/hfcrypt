# :lock: HFCrypt

## For :hugs: HF Spaces

Ever wanted to host something on Hugging Face Spaces but didn't want your code to be public? Look no further HFCrypt! HFCrypt encrypts your code to make your code closed-source! **TL;DR:** HFCrypt allows you to host closed-source apps on Hugging Face Spaces! It even allows you to host additional resources, including large AI models, all in one file bundle with compression!

Curious to see how it works? Check out the [live demo](https://huggingface.co/spaces/mrfakename/hfcrypt-demo)!

## :newspaper_roll: News + Updates

October 12, 2023: Removed the port `7860` requirement, open-sourced demo app (located in `app` directory).

## :teacher: How it works

1. HFCrypt reads your app from the `app` directory.
2. The app is bundled into a single `.hfc` (HFCrypt) file, using the ZIP file format. This means that not only is the app encrypted, but it is also compressed.
3. The HFCrypt Bundle is encrypted using Fernet encryption and a random key. The random key is displayed in the CLI.
4. Create a new space, with any SDK.
5. Place the encryption key in Hugging Face Spaces Secrets, under the `HFCRYPT_KEY` variable name.
6. Upload the contents of the `out` directory to the Hugging Face Space.
7. Building takes slightly longer than normal. On build, the bundle is decrypted using the key.

## :warning: Security Note

This package uses Fernet encryption *and may be cracked with a brute-force attack.* Please do not store highly sensitive code using HFCrypt. We are not liable for loss of code or if it is exposed.

## :rocket: Quickstart

On Unix/macOS/Linux-based systems, simply run:

```bash
python3 -m pip install cryptography && python3 -c "$(curl -fsSL https://raw.githubusercontent.com/hfcrypt/hfcrypt/main/hfcrypt.py)"
```

In your project directory (with the `app` folder)

## :pen: Usage

HFCrypt is simple and easy to use! Just follow the following steps to get started!

### :computer: Installation

```sh
git clone https://github.com/hfcrypt/hfcrypt
python3 -m pip install -r requirements.txt
```

### :computer_mouse: Preparation

Before you convert your app, you'll need to do a couple simple steps to prepare your app.

### :arrow_right: Conversion

Please place all the files for your app in the `app` folder.

**Make sure your main server file is named `app.py`!**

Make sure the host is `0.0.0.0`

Then run:

```
python3 hfcrypt.py
```

### :cloud: Deploy

Upload all the files in the `out` folder (**NOT** the folder itself, *only* the contents of the folder) to your Hugging Face Space.

Then, set the `HFCRYPT_KEY` secret (**NOT variable!**) to the key given in the CLI!

## :thought_balloon: Approaches

There are several different ways to achieve this:

* Store a GitHub token in Hugging Face Spaces Secrets and set the SDK to Docker. Have the Dockerfile clone from a GitHub private repository using the token. But this requires a GitHub repository and doesn't support large files. ([Forum thread](https://discuss.huggingface.co/t/share-app-url-without-sharing-the-files-and-version/26182))
* Use HFCrypt: Encrypt your source code, and save the key in Hugging Face Spaces

## :heavy_check_mark: Todo

* [ ] Allow user to auto-upload to Hugging Face Spaces using HF CLI
* [ ] Implement SimpleSplit for large file uploads
* [ ] Add decryption CLI
* [ ] Allow CLI usage
* [ ] Add GitHub Actions example

## :spiral_notepad: Notes

* This package uses Fernet encryption *and may be cracked with a brute-force attack.* Please do not store highly sensitive code using HFCrypt. We are not liable for loss of code or if it is exposed.
* This package **will increase build time.**
* You are responsible for complying with Hugging Face's terms of service.

## :sunglasses: Real-Life Implementations

* [Text-to-Speech with Tortoise (on CPU - VERY slow)](https://huggingface.co/spaces/mrfakename/hfcrypt-tts-saas) by [@fakerybakery](https://github.com/fakerybakery)
* Want yours added? Please create an Issue on GitHub!

## :memo: Credits

* Main Developer: [@fakerybakery](https://github.com/fakerybakery)

## :scroll: License + Disclaimer

License for the HFCrypt source code coming soon.

The default license for encrypted spaces (feel free to change this) is available [here](HESC.md). It's just a modified version of the MIT license that says you can't reverse-engineer it or modify it. It also has a disclaimer.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**Copyright &copy; 2023. All rights reserved. Redistribution is subject to the license of HFCrypt.**

*All trademarks belong to their respective owners. This independent open-sourced project is not affiliated with Hugging Face in any way.*
