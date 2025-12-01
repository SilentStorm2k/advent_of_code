# 🎄 SilentStorm2k's Advent of Code Solutions

This repository tracks my solutions and experiments for the annual **Advent of Code (AoC)** programming challenges.

Each day’s puzzle is scaffolded automatically, and inputs are fetched securely using your session token.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SilentStorm2k/advent_of_code.git 
cd advent_of_code 
```

---

### 2. Add your AoC session token

Create a file named `secrets.json` in the root of the project:

```json
{
  "session": "YOUR_SESSION_TOKEN"
}
```

**How to get your session token:**

1. Log in to [https://adventofcode.com](https://adventofcode.com)
2. Open **Developer Tools** in your browser
3. Go to the **Application** tab (or "Storage")
4. Click **Cookies**
5. Copy the value of the `session` cookie

Keep this file local and **never commit it to GitHub**.

---

## 🛠️ Usage

### Create boilerplate + fetch input

This generates a Python starter file for the given day and automatically fetches your puzzle input. This will also create an **empty** example input file that you can populate to test custom examples:

```bash
sh setup.sh <YEAR> <DAY>
```

**Example:**

```bash
sh setup.sh 2025 01
```

---

### Run the solution

Once you've implemented your solution, run:

```bash
sh solve.sh <YEAR> <DAY>
```

This will execute your code and neatly print the answer to the terminal with time taken to run each script.

**Example:**

```bash
sh solve.sh 2025 01
```

---

## 📌 Notes

* All solutions are written in **Python**
* Folder structure is organized by **year/day**
* Your puzzle input are stored under **year/puzzle_input** folder
* Inputs are fetched securely using your session cookie

Happy coding & enjoy AoC! 🎁💻✨
