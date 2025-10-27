# Michael Snake Game 🎮

A **challenging Snake game** built from scratch in Python using **Pygame**. Designed for clarity, originality, and fun — perfect for learning or showcasing your Python game development skills.

---

## 🧩 Features
- **Smooth grid-based gameplay** with scalable difficulty.
- **Two food types**:
  - 🍏 Normal Food — +1 score, normal growth.
  - ⚡ Speed Food — +2 score, temporary speed boost.
- **Level progression:** more obstacles appear as you score higher.
- **Autopilot mode (A*)** — watch the snake find food on its own.
- **High score persistence** saved locally.
- **Clean, class-based architecture** for easy expansion.
- **Pause (P)**, **Restart (R)**, and **Autopilot toggle (A)** controls.

---

## 🧠 Controls
| Key | Action |
|-----|--------|
| ⬆️ / ⬇️ / ⬅️ / ➡️ | Move the snake |
| **P** | Pause / Resume |
| **R** | Restart game |
| **A** | Toggle autopilot (AI mode) |
| **ESC** | Quit game |

---

## 🏗️ Installation & Run

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/michael-snake-game.git
cd michael-snake-game
```

### 2. Install dependencies:
```bash
pip install pygame
```

### 3. Run the game:
```bash
python michael_snake_game.py
```

---

## 📈 Scoring & Levels
| Item | Points | Effect |
|------|---------|---------|
| Normal Food | +1 | Normal growth |
| Speed Food | +2 | Temporary speed boost |

Every **5 points**, the game increases in difficulty with new obstacle placements.

---

## 🧠 Autopilot Mode
Toggle **Autopilot (A)** to let the AI control the snake using **A* pathfinding**. It dynamically calculates a safe path toward the nearest food while avoiding walls and obstacles.

---

## 💾 High Score
Your high score is automatically saved locally in `michael_snake_highscore.txt` and loaded every session.

---

## 🧱 Project Structure
```
├── michael_snake_game.py   # Main game script
├── michael_snake_highscore.txt  # Auto-generated after play
└── README.md                # You are here
```

---

## 🚀 Future Ideas
- Add **sound effects** and background music 🎵
- Introduce **different maps or maze patterns** 🧱
- Implement **multiplayer or LAN mode** 🕹️
- Add **skins and themes** 🎨

---

## 🧑‍💻 Author
**Michael** — Python developer passionate about creating clean, challenging, and educational code.

📫 *Feel free to fork, contribute, or suggest improvements!*

---

## 🪪 License
This project is released under the **MIT License**. You are free to use, modify, and distribute it with attribution.

---

**Enjoy the game — and challenge yourself to beat your high score! 🐍**
