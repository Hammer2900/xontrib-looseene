<p align="center">
  <b>xontrib-history-looseene</b><br>
  A smart, lightning-fast, and feature-rich history backend for the <a href="https://xon.sh">xonsh shell</a>.
</p>

<p align="center">
  <a href="https://github.com/Hammer2900/xontrib-looseene/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Hammer2900/xontrib-looseene" alt="License"></a>
  <a href="https://pypi.org/project/xontrib-history-looseene/"><img src="https://img.shields.io/pypi/v/xontrib-history-looseene" alt="PyPI"></a>
</p>

**Looseene** transforms your shell history into a mini search engine. It replaces xonsh's standard history with a compressed, inverted-index backend, enabling instant and relevant search results, even across massive command logs.

![Looseene UI](assets/looseene-screenshot.png)

### 🚀 Features

*   **Interactive Search (`Ctrl+R`):** A powerful full-screen UI to navigate, search, and manage your history.
*   **Command Execution Counts:** Automatically tracks how often you run each command, helping you find your most-used tools.
*   **Custom Comments:** Annotate commands with comments for context (`F3` in UI or `hs-comment` command).
*   **Prefix Search & Highlighting:** Find commands by typing parts of a word (e.g., `dist` finds `distribution`), with matches highlighted in yellow.
*   **Smart & Fast:** Uses the **BM25** ranking algorithm to find the most *relevant* commands, not just the most recent. Data is stored in compressed binary segments using `mmap`, `zlib`, and `struct` for instant access.
*   **Pure Python:** No C-extensions or heavy dependencies. It just works.

## 📦 Installation

Open xonsh and run:
```xsh
xpip install xontrib-history-looseene
```

## ⚙️ Configuration

To activate the backend, add this line to your `.xonshrc` file (e.g., `~/.config/xonsh/rc.xsh`):
```python
xontrib load looseene
```
Restart your shell. You should see a message `Looseene: History backend loaded...`.

## ⌨️ Usage

### Interactive Search (`Ctrl+R`)

Press **`Ctrl+R`** to open the interactive search window. What you've already typed on the command line will be used as the initial search query.

*   **Type** to search in real-time.
*   **Up/Down Arrows** to navigate results.
*   **Enter** to select a command and place it on your command line.
*   **F3** to add or edit a comment for the selected command.
*   **Ctrl+C / Esc** to exit; the text you typed in the search bar will be preserved on your command line.

### Adding Comments

You can annotate commands with comments for better context, either interactively or from the command line.

1.  **Interactively (F3):** Press `F3` while in the `Ctrl+R` menu to open a dialog and add a comment to the selected command.
2.  **Via CLI:** Use the `hs-comment` alias.

```xsh
# Usage: hs-comment <partial_command_to_find> "<your comment>"
hs-comment "docker-compose up" "start project services"
```

### CLI Search

You can also search directly from the command line without the UI:
```xsh
# Full command
hsearch "docker run"

# Alias
hs "git commit"
```

### Maintenance (Compaction)

Looseene stores history in small "segments" on disk for fast writing. Over time, these can accumulate. To merge all segments into a single, optimized file and finalize metadata (counts and comments):
```xsh
history-compact
```
*Recommendation: Run this command occasionally to keep performance high.*

## 🛠 Technical Details

*   **Storage:** `~/.local/share/xonsh/looseene_history`
*   **Index Structure:** Inverted index with delta-encoded postings lists.
*   **Backend:** Custom implementation inheriting from `xonsh.history.base.History`.

## 🛠 Development & Testing

Looseene is designed to be lightweight and dependency-free. You can verify the core search engine logic using only the Python standard library.

### Running Core Tests (Zero Dependencies)
No need to install `pytest`. Simply run the test script directly with Python:

```bash
python3 tests/test_native.py
```

### Running Integration Tests
If you have `pytest` and `xonsh` installed and want to run the full suite (including xontrib loading tests):

```bash
pytest
```

## 🤝 Contributing

Contributions are welcome!
1. Fork the repo.
2. Install in editable mode: `xpip install -e .`
3. **Ensure tests pass**: `python3 tests/test_native.py`
4. Submit a Pull Request.

## 📄 License
MIT License.
