# 🎨 Color Sequence Game

> A CLI memory game built in Python where you memorize color sequences against the clock — with progressive difficulty, a countdown timer, and a persistent top-5 leaderboard.

**Built with Python · Colorama · File I/O**

---

## 🎮 How to Play

1. A sequence of colors appears on screen
2. You have a few seconds to memorize it before it disappears
3. Type the sequence back correctly to advance
4. Every 3 rounds the difficulty increases — longer sequences, less time
5. 3 wrong answers and it's game over

---

## 📊 Difficulty Scaling

| Rounds | Sequence Length | Time to Memorize | Score Bonus |
|---|---|---|---|
| 1 – 3 | 3 colors | 3 seconds | 100 pts |
| 4 – 6 | 4 colors | 3 seconds | 150 pts |
| 7 – 10 | 5 colors | 2 seconds | 200 pts |
| 11 – 15 | 6 colors | 2 seconds | 300 pts |
| 16+ | 6 colors | 1.5 seconds | 400 pts |

Beat round 10 to unlock **Endless Mode** — where the timer drops to 1.5 seconds and every round is worth maximum points.

---

## 🚀 Setup

### Prerequisites
- Python 3.6+
- pip

### Installation

```bash
git clone https://github.com/AngelNandayapa/color-sequence-game.git
cd color-sequence-game
pip install -r requirements.txt
```

### Run

```bash
python SecuenciaColores.py
```

> **Note for Windows users:** colorama handles terminal colors automatically — no extra setup needed.
> **Note for Linux/Mac users:** Run from a native terminal (GNOME Terminal, iTerm2, etc.) for best color rendering.

---

## 🗂️ Project Structure

```
color-sequence-game/
├── SecuenciaColores.py   # Main game logic
├── requirements.txt      # Dependencies
├── scores.txt            # Auto-generated leaderboard (created on first run)
└── README.md
```

---

## 🧠 Features

- **6 colors** — rojo, verde, azul, amarillo, morado, celeste
- **Countdown timer** — 3-2-1-GO before each sequence
- **Progressive difficulty** — sequence length and bonus points increase every 3 rounds
- **Endless mode** — unlocked after beating round 10
- **Persistent leaderboard** — top 5 scores saved to `scores.txt` between sessions
- **Input validation** — handles empty names and malformed score entries gracefully

---

## 💡 What I Learned Building This

- Dictionary mapping for color-to-ANSI-code translation
- List manipulation with `shuffle()` and slicing
- File I/O with append and read modes for persistent data
- Sorting tuples with `lambda` functions
- Terminal color rendering with colorama across platforms
- Defensive programming — input validation, edge case handling, safe file initialization

---

## 👤 Author

**Angel Nandayapa**
AI Automation Engineer · Software Developer
Tecnológico de Monterrey — Computer Technologies Engineering

[LinkedIn](https://linkedin.com/in/angelnandayapa) · [GitHub](https://github.com/AngelNandayapa)
