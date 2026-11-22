# Setup — getting a laptop ready to code Cat-Bot

Do this **once per laptop**. A coach should do Part 1 and supervise Part 2.
Plan on about 30 minutes per laptop the first time.

> **Important — GitHub accounts and age.** GitHub's Terms of Service require
> every account holder to be **13 or older**. Our team members are in 6th
> grade, so **the GitHub account belongs to a coach**, not to the kids.
> The kids still use Git on the team laptops: every commit is labeled with
> the kid's first name (see "Who am I?" below), and a coach's sign-in is what
> uploads ("pushes") the work to GitHub. Nobody under 13 signs in to GitHub.

---

## Part 1 — Coach, one time: create the GitHub home

1. Sign in to <https://github.com> with your own (adult) account.
2. Create a free **organization** for the team (profile picture → *Your
   organizations* → *New organization* → *Free*). Suggested name:
   `thecats-fll-71447`. Add any other adult coaches as owners.
3. In the organization, create a **new repository** named
   `bioglow`. Make it **Public** (free GitHub Pages hosting for the
   website needs a public repository). Don't add a README — we have one.
4. Upload this folder to it. Easiest: on a laptop that has finished Part 2,
   open a terminal in this folder and run:

   ```
   git init -b main
   git add .
   git commit -m "Robot code (Nov 18) + setup. Robot Design & Robot Performance winners!"
   git tag start-2026-11-18
   git remote add origin https://github.com/thecats-fll-71447/bioglow.git
   git push -u origin main --tags
   ```

   The first push asks a coach to sign in to GitHub in the browser (see
   **Signing in to GitHub** at the end of Part 2 for Mac and Linux).
5. Turn on the website: repository **Settings → Pages → Build and deployment →
   Source: Deploy from a branch → Branch: `main`, folder: `/docs` → Save**.
   After a minute or two the site is live at
   `https://thecats-fll-71447.github.io/bioglow/`.
6. Protect `main` (optional but recommended): **Settings → Branches → Add
   branch ruleset** → target `main` → *Require a pull request before merging*.
   Coaches then merge finished work through pull requests.

---

## Part 2 — Each team laptop (Windows, Mac, or Linux)

You need four things: **Git**, **Python 3.10 or newer**, **VS Code**, and
**Bluetooth**. Do step 1 for your kind of computer, then steps 2–6 are the
same everywhere (with small differences called out).

> **Keyboard shortcuts:** this guide says `Ctrl`. On a Mac, use `Cmd` instead
> (`Cmd+Shift+P`, `Cmd+Shift+G`).

### Step 1 — Install the tools

#### Windows

Open **PowerShell** and paste these one at a time (each takes a minute or two):

```powershell
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id Python.Python.3.13 -e
```

Close PowerShell and open it again (so it finds the new programs).

> No `winget`? Download and install from <https://git-scm.com>,
> <https://code.visualstudio.com>, and <https://www.python.org/downloads/>
> (tick **"Add python.exe to PATH"** in the Python installer).

#### macOS

The easiest way is **Homebrew**, the standard Mac installer for developer
tools. Open **Terminal** (Applications → Utilities) and paste:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

When it finishes, it prints **"Next steps"** with two or three commands to
add Homebrew to your PATH. **Run those**, then:

```bash
brew install git python@3.13
brew install --cask visual-studio-code
```

> Rather not use Homebrew? Run `xcode-select --install` (this gives you Git),
> then install Python from <https://www.python.org/downloads/macos/> and VS
> Code from <https://code.visualstudio.com> (drag it into Applications).
> To get the `code` command: open VS Code, press `Cmd+Shift+P`, and run
> **Shell Command: Install 'code' command in PATH**.

#### Linux (Ubuntu, Debian, Linux Mint)

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
```

For VS Code, download the **.deb** file from <https://code.visualstudio.com>
and install it (this also sets up automatic updates):

```bash
sudo apt install ./code_*.deb
```

(or `sudo snap install code --classic` if your system uses Snap).

> **Fedora:** `sudo dnf install git python3`, then the **.rpm** from the VS
> Code website. **Older systems:** Python must be 3.10 or newer — check
> with `python3 --version` (Ubuntu 22.04 and newer are fine).

### Step 2 — Check that everything installed

Open a new terminal (PowerShell on Windows, Terminal on Mac/Linux):

```bash
git --version
code --version
python --version     # Windows
python3 --version    # Mac and Linux
```

Each one should print a version number. Python must say **3.10 or higher**.

### Step 3 — Get the code

1. Open **VS Code**.
2. Press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`), type **Git: Clone**, press Enter.
3. Paste `https://github.com/thecats-fll-71447/bioglow.git`.
4. Pick a folder (for example `Documents/FLL`) and click **Open** when asked.
5. VS Code asks to install the **recommended extensions** (Python) — click **Install**.

### Step 4 — Set up Python for the robot tools

In VS Code open a terminal (**Terminal → New Terminal**) and run the commands
for your computer.

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell says *running scripts is disabled*, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Mac and Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You'll see `(.venv)` at the start of the terminal prompt when it's active.
Then press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`) → **Python: Select
Interpreter** → pick the one that says `.venv`. From now on VS Code turns it
on automatically in new terminals.

### Step 5 — Test it (no robot needed)

With `(.venv)` showing in the terminal, this command is the same everywhere:

```bash
python tests/check.py
```

You should see `OK` for every file and `SAME` for every match scenario.
(Or use **Tasks: Run Task → Check code (no robot)**.)

### Step 6 — Send code to the robot

1. Turn on the hub (it already has Pybricks firmware). Make sure the
   computer's **Bluetooth is on**.
2. In VS Code: `Ctrl+Shift+P` → **Tasks: Run Task** → **Load program onto robot**.
   (Or in the terminal: `python tools/load_robot.py`)
3. It lists every Pybricks hub that's turned on nearby, closest first, and
   waits. **Type the number of your hub** and press Enter. Nothing is sent
   until you do, and just pressing Enter cancels.
4. The program stays on the hub. Walk to the table and start it with the
   center button — just like at the qualifier.

**First time on a Mac:** macOS asks *"Visual Studio Code would like to use
Bluetooth."* Click **Allow**. If you clicked Don't Allow by mistake: **System
Settings → Privacy & Security → Bluetooth** → turn on **Visual Studio Code**
(and **Terminal**, if you run commands from Terminal).

**On Linux:** Bluetooth goes through the normal system Bluetooth service
(BlueZ), which desktop Linux already has. If the hub isn't found, check that
Bluetooth is powered on: `bluetoothctl show` should say `Powered: yes`.
Connecting a hub by **USB cable** (optional — not needed for normal use, but
needed for updating firmware) requires permission rules, one time:

```bash
python -m pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

**Lots of hubs in the room?** That's why the loader asks first. Give each
of the team's hubs its own name (for example `CatBot`) so it's easy to pick
from the list. A hub's name is chosen when Pybricks firmware is installed
on it, in Pybricks Code. If two hubs share a name, the list says so; pick by
signal strength (closest is strongest) or turn the other one off.

### Signing in to GitHub (coaches only)

Kids never sign in. When a coach is ready to upload ("push") work:

- **Easiest, on any computer:** push from VS Code (Source Control → **Sync
  Changes**, or `git push` in VS Code's own terminal). VS Code offers
  **Sign in with GitHub** and opens a browser window. Sign in there.
- **Windows** also remembers the sign-in for any terminal (Git Credential Manager).
- **Mac/Linux, pushing from a regular Terminal:** install the GitHub CLI
  (Mac: `brew install gh`; Linux: see <https://cli.github.com>), then run
  `gh auth login` once and `gh auth setup-git`.

---

## Option B — No installs (Pybricks Code website)

The team already knows the Pybricks Code website (<https://code.pybricks.com>,
Chrome or Edge on Windows, Mac, Linux, or a Chromebook). It works with this
repository too:

1. In Pybricks Code, click **Import** and select **all** the `.py` files from
   the `robot` folder (multi-file programs work — `main.py` imports the others).
2. Open `main.py` and run it as usual.
3. **When you're done, export your changed files and copy them back into the
   `robot` folder**, then commit (see WORKFLOW.md).

> **Linux only:** Chrome needs one setting before the website can use
> Bluetooth. Paste `chrome://flags/#enable-experimental-web-platform-features`
> into the address bar, set it to **Enabled**, and restart Chrome.

> **The repository is the official copy.** Code that only lives inside one
> browser's Pybricks Code is one cleared browser away from being gone.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `pybricksdev` can't find the hub | Bluetooth on? Hub on and **not** connected to another laptop or the Pybricks website? Close the Pybricks Code tab. |
| `ImportError: no module named 'run_...'` on the hub | You loaded only one file. Load `main.py` with pybricksdev (it sends every file it imports), or import **all** robot files into Pybricks Code. |
| `git push` asks for a password | A coach signs in through the browser window. Never type a coach password where kids can see it. |
| A task says `.venv` ... not found / not recognized | The tasks use the project's own `.venv`, whichever Python version made it. Do Step 4 in the `bioglow` folder to create it. |
| `check.py` says `CHANGED` | That's fine if you meant to change that run. It's telling you which command is different from the competition code. |
| `check.py` says `ERROR` | Typo or missing import in the file it names — read the message. |
| Mac: hub never shows up | macOS blocked Bluetooth for VS Code or Terminal: **System Settings → Privacy & Security → Bluetooth**, turn it on, then quit and reopen VS Code. |
| Mac/Linux: `python: command not found` | Outside the `.venv`, use `python3`. Inside it (`(.venv)` in the prompt), `python` works. Run `source .venv/bin/activate` to turn it on. |
| Linux: `ensurepip is not available` when making the `.venv` | Install the venv package the message names, e.g. `sudo apt install python3-venv` (or `python3.12-venv`), then try again. |
| Linux: Pybricks Code website says Bluetooth isn't available | Turn on `chrome://flags/#enable-experimental-web-platform-features` and restart Chrome. |
| `code: command not found` | Mac: in VS Code, `Cmd+Shift+P` → **Shell Command: Install 'code' command in PATH**. You can always just open VS Code from the app menu instead. |
