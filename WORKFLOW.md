# How we work — Git for The Cats

Git is a **time machine for code**. Every time you *commit*, Git takes a
snapshot of the files, with your name and a note about what you did.
You can always go back. Nobody's work gets lost or overwritten.

## Words to know

| Word | What it means |
|---|---|
| **Repository (repo)** | This whole project folder, plus its history. |
| **Commit** | A saved snapshot + a message saying what changed and why. |
| **Branch** | Your own copy of the code to experiment on. |
| **`main`** | The branch with the **competition-ready** code. |
| **Pull** | Download everyone else's new commits. |
| **Push** | Upload your commits to GitHub. |
| **Merge** | Combine a finished branch into `main`. |

## Every session — the 6 steps

All of these buttons are in VS Code's **Source Control** panel (the branch
icon on the left, or `Ctrl+Shift+G`).

### 1. Who am I?
`Ctrl+Shift+P` → **Tasks: Run Task** → **Who am I?** → pick your name.
Now every commit you make is labeled with your name. *(Do this every time
you sit down at a shared laptop!)*

### 2. Get the latest code
Click **⋯ → Pull** (or the 🔄 sync button at the bottom-left).

### 3. Make (or switch to) your branch
Click the branch name at the bottom-left → **Create new branch**.
Name it after the run and what you're fixing:

- `run-b-window` — getting M11 to work every time
- `run-9-roots` — making the roots extend completely
- `blog-konrad-attachments` — a new blog post

Working on the same thing as last time? Click the branch name and pick your
existing branch instead.

### 4. Change, check, test
- Edit the run file you're working on.
- Run **Tasks: Run Task → Check code (no robot)**. Fix any `ERROR`.
- Load it onto the robot and **test on the table**.

### 5. Commit — with a good message
Stage your files (the **+** next to each file), type a message, click **Commit**.

A good commit message says **what you changed, why, and what happened**:

| ✅ Good | ❌ Not helpful |
|---|---|
| `Run B: turn 105 instead of 110 before window. Window down 4/5 tries` | `fixed it` |
| `Run 9: slow roots arm to 150 so it doesn't bounce. Roots complete 3/3` | `changes` |
| `Blog: Thomas's post about the attachment template` | `stuff` |

These messages are our **engineering notebook**. Judges love seeing how you
tested and improved. (Rubric: *"Clear evidence of improvements based on
testing."*)

### 6. Push, and ask for a merge when it's SOLVED
Click **Sync Changes** / **Publish Branch** to push.
When your change passes the **Solved Rule (works 3–5 times in a row)**,
tell a coach. The coach merges your branch into `main`.

---

## Golden rules

1. **Never commit straight to `main`.** Always use a branch.
2. **One run per branch.** Keeps changes small and easy to merge.
3. **Commit often** — every time something works a little better.
4. **Write down numbers** in commit messages: *"3/5"*, *"turned 2° more"*.
5. **Don't delete old code to "save" it in comments.** Git already remembers
   every old version. (That's why our old `# old code` sections moved out.)
6. **If Git shows a "merge conflict," stop and get a coach.** It's normal and
   fixable — two people changed the same lines.

## Coach checklist — merging a branch

1. Kid shows the run working 3–5 times in a row on the table.
2. `python tests/check.py` → no `ERROR`. `CHANGED` should appear **only**
   for the run they meant to change.
3. Merge the pull request on GitHub (or in VS Code: switch to `main`,
   **Branch → Merge Branch…**, pick their branch, push).
4. Before a competition: on `main`, run
   `git tag state-2026-12-12` then `git push --tags`, so you can always get
   back to exactly what ran that day.

## Going back in time (coach)

- See history: Source Control panel → **Timeline** at the bottom, or
  `git log --oneline`.
- Get the starting code back: `git checkout start-2026-11-18 -- robot`
  (or copy the team's original single file from `archive/team-2026-11-18/`).
