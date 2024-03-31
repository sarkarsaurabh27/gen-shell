
<h1 align="center">🔍🐚 Gen-Shell</h1>

<p align="center">
    Leverage AI to generate shell commands from plain English.
</p>

<p align="center">
    <img src="https://img.shields.io/github/stars/yourusername/gen-shell?style=for-the-badge" alt="stars" />
    <img src="https://img.shields.io/github/issues/yourusername/gen-shell?style=for-the-badge" alt="issues" />
    <img src="https://img.shields.io/github/forks/yourusername/gen-shell?style=for-the-badge" alt="forks" />
    <img src="https://img.shields.io/github/license/yourusername/gen-shell?style=for-the-badge" alt="license" />
</p>

<!-- <p align="center">
    <img src='https://yourimageurl.gif' alt='Gen-Shell in action'>
</p> -->

## 📘 What is Gen-Shell?

Gen-Shell is a command-line interface (CLI) tool that uses the power of OpenAI's GPT-4 to interpret plain English descriptions of tasks and generate the corresponding shell commands. Inspired by projects like [Zsh Codex](https://github.com/tom-doerr/zsh_codex) and [Codex-CLI by Microsoft](https://github.com/microsoft/Codex-CLI?tab=readme-ov-file), Gen-Shell aims to make the command line more accessible and efficient.

## 🚀 Features

- **AI-Powered**: Utilizes OpenAI's GPT-4 for intelligent command generation.
- **Cross-Platform**: Compatible with various Unix-based shells including Bash and Zsh.
- **User-Friendly**: Easy-to-use for both beginners and experienced users.

## 📦 Installation

### Prerequisites

- Python 3.6+
- OpenAI API key

### Steps

1. **Clone the repository**

    ```sh
    git clone https://github.com/yourusername/gen-shell.git
    cd gen-shell
    ```

2. **Setup virtual environment (Optional)**

    ```sh
    python -m venv env
    source env/bin/activate  # Unix/macOS
    env\Scripts\activate  # Windows
    ```

3. **Install Gen-Shell**

    ```sh
    pip install -e .
    ```

4. **Environment Configuration**

    Set your OpenAI API key in your environment:

    ```sh
    export OPENAI_API_KEY="Your_OpenAI_API_Key"
    ```

## 🔨 Usage

To use Gen-Shell, run:

```sh
gen-shell 'your task description here'
```

**Example**:

```sh
❯ gen-shell 'how to check which service is running on port 6463'
Learn More: https://ss64.com/osx/lsof.html
Run Command: `lsof -i :6463`? (Y/n): y
COMMAND     PID   USER   FD   TYPE             DEVICE SIZE/OFF  NODE NAME
Discord   90173   root  56u   IPv4 0x99fa38dd484a062d      0t0  TCP localhost:6463 (LISTEN)

❯ gen-shell 'how to list all running processes'
. . .
```

## ⚙️ Advanced Setup

### Key Binding

Bind Gen-Shell to a key combination for quick access:

1. Open your `.inputrc` file in your home directory (create it if it does not exist).
2. Add a line to bind a key combination to your command, like so:
```sh
"\e[24~":"get-agent\n"
```
3. Apply the changes by either restarting your terminal or running `bind -f ~/.inputrc`.

## 🤝 Contributing

Contributions are welcome! Please see our [contribution guidelines](CONTRIBUTING.md) for more details.

## 📜 License

Gen-Shell is released under the MIT License. See [LICENSE](LICENSE) for details.

## 💡 Inspiration

This project is inspired by:

- [Zsh Codex](https://github.com/tom-doerr/zsh_codex)
- [Codex-CLI by Microsoft](https://github.com/microsoft/Codex-CLI?tab=readme-ov-file)

---

<p align="center">
    Made with ❤️ by [Your Name]
</p>
