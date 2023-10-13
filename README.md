# :lock: HFCrypt

**Warning:** This project isn't quite working yet.

Ever wanted to host something on Hugging Face Spaces but didn't want your code to be public? Look no further HFCrypt! HFCrypt encrypts your code to make your code closed-source! **TL;DR:** HFCrypt allows you to host closed-source apps on Hugging Face Spaces!

Curious to see how it works? Check out the [live demo](https://huggingface.co/spaces/mrfakename/hfcrypt-demo)!

## :warning: Security Note

This package uses Fernet encryption *and may be cracked with a brute-force attack.* Please do not store highly sensitive code using HFCrypt. We are not liable for loss of code or if it is exposed.

## :pen: Usage

HFCrypt is simple and easy to use! Just follow the following steps to get started!

### - :computer: Installation

```sh
git clone https://github.com/hfcrypt/hfcrypt
python3 -m pip install -r requirements.txt
```

### - :computer_mouse: Preparation

Before you convert your app, you'll need to do a couple simple steps to prepare your app.

1. **IMPORTANT:** Set your app's external port to `7860`
   1. In Flask: `app.run('0.0.0.0', port=7860)`

### - :arrow_right: Conversion

Please place all the files for your app in the `app` folder.

**Make sure your main server file is named `app.py`!**

Then run:

```
python3 hfcrypt.py
```

### - :cloud: Deploy

Upload all the files in the `out` folder (**NOT** the folder itself, *only* the contents of the folder) to your Hugging Face Space.

Then, set the `HFCRYPT_KEY` secret (**NOT variable!**) to the key given in the CLI!

## :thought_balloon: Approaches

There are several different ways to achieve this:

* Store a GitHub token in Hugging Face Spaces Secrets and set the SDK to Docker. Have the Dockerfile clone from a GitHub private repository using the token. But this requires a GitHub repository and doesn't support large files. ([Forum thread](https://discuss.huggingface.co/t/share-app-url-without-sharing-the-files-and-version/26182))
* Use HFCrypt: Encrypt your source code, and save the key in Hugging Face Spaces

## :heavy_check_mark: Todo

* [ ] Allow user to auto-upload to Hugging Face Spaces using CLI

## :spiral_notepad: Notes

* This package uses Fernet encryption *and may be cracked with a brute-force attack.* Please do not store highly sensitive code using HFCrypt. We are not liable for loss of code or if it is exposed.
* This package **will increase build time.**
* You are responsible for complying with Hugging Face's terms of service.

## :scroll: License

License for the HFCrypt source code coming soon.

The default license for encrypted spaces (feel free to change this) is available [here](HESC.md). It's just a modified version of the MIT license that says you can't reverse-engineer it or modify it. It also has a disclaimer.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
