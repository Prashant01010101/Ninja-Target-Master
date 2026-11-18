# Ninja Target Master

**Object-Oriented Programming (OOP) Project**

## 1. Project Overview

Ninja Target Master is a 2D arcade-style target-shooting game developed using Python and Pygame. The player controls a ninja inside a Japanese-inspired dojo and throws shurikens at moving targets to earn points.

The objective is to reach the required score before the timer runs out. The game contains three levels with different target types, speeds, and score requirements.

The project demonstrates object-oriented programming principles, including abstraction, inheritance, polymorphism, and encapsulation.

## 2. Game Features

- Ninja movement using WASD or arrow keys.
- Mouse-controlled shuriken throwing.
- Moving targets with collision detection.
- Four target types with different appearances and point values.
- Three levels with increasing difficulty.
- Score and countdown timer.
- Hit, miss, and accuracy tracking.
- Main menu, pause screen, and result screen.
- Restart and level progression.

## 3. Requirements

- Python 3
- Pygame

Install Pygame using:

```bash
python3 -m pip install pygame
```

## 4. How to Run the Game

1. Download or extract the project folder.
2. Open a terminal in the folder containing `Project.py`.
3. Install Pygame if it is not already installed.
4. Run:

```bash
python3 Project.py
```

The game window will open with the main menu. Press **Enter** to begin.

## 5. Game Controls

| Key / Action | Function |
|---|---|
| W / Up Arrow | Move up |
| S / Down Arrow | Move down |
| A / Left Arrow | Move left |
| D / Right Arrow | Move right |
| Left Mouse Click | Throw shuriken toward the cursor |
| Enter | Start from the main menu |
| P | Pause or resume |
| R | Restart from Level 1 |
| Space | Advance after completing Level 1 or 2 |
| Esc | Exit the game |

## 6. Gameplay Rules

The player must hit moving targets to earn enough points before the countdown reaches zero.

### Target Types

| Target | Appearance | Points |
|---|---|---:|
| Normal Target | Wooden bullseye | +10 |
| Fast Target | Blue target | +20 |
| Golden Target | Gold target | +50 |
| Danger Target | Red warning target | −20 |

The score cannot fall below zero.

### Levels

| Level | Required Score | Time Limit |
|---|---:|---:|
| Level 1 | 150 | 60 seconds |
| Level 2 | 250 | 60 seconds |
| Level 3 | 350 | 60 seconds |

Level 1 introduces normal targets. Level 2 introduces faster targets and bonus golden targets. Level 3 introduces danger targets.

The player wins a level by reaching the required score before time runs out. Completing Level 3 finishes the game.

If time runs out before the score goal is reached, the player loses and can restart.

## 7. Project Structure

```text
OOP Project/
├── Project.py
├── settings.py
├── ninja.py
├── shuriken.py
├── targets.py
├── scoreboard.py
├── level.py
├── README.md
├── AI_LOG.md
└── docs/
    └── class-diagram.png
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `Project.py` | Main `Game` class, event handling, game loop, and screens |
| `settings.py` | Window dimensions, FPS, and colors |
| `ninja.py` | Ninja movement and drawing |
| `shuriken.py` | Shuriken movement, drawing, and screen boundaries |
| `targets.py` | Target classes, movement, drawing, collision detection, and scoring values |
| `scoreboard.py` | Score, timer, hit/miss tracking, accuracy, and HUD |
| `level.py` | Level number, score goal, and time limit |
| `docs/class-diagram.png` | UML class diagram showing class relationships |

## 8. Object-Oriented Programming Concepts

### Abstraction

The `BaseTarget` class uses Python's `ABC` and `@abstractmethod` to define required methods, including `draw()` and `get_points()`.

### Inheritance

`Target` and `FastTarget` inherit from `BaseTarget`.

`GoldenTarget` and `DangerTarget` inherit from `Target`, allowing them to reuse existing movement and collision logic.

### Polymorphism

Different target classes implement `draw()` and `get_points()` differently.

The `Game` class can call the same methods on different target objects without needing separate drawing and scoring code for each type.

### Encapsulation

The `ScoreBoard` class uses internal attributes such as `_score` and `_time_left`, together with Python `@property` getters and setters.

The setters prevent the score and remaining time from becoming negative.

### Modular Programming

The classes are organized into separate Python modules according to their responsibilities. The main `Game` class imports and coordinates these modules.

## 9. UML Class Diagram

The UML class diagram is located at:

`docs/class-diagram.png`

It illustrates the project's classes, methods, attributes, inheritance relationships, and associations.

## 10. AI Assistance

ChatGPT was used during development to assist with understanding OOP concepts, planning class structure, debugging errors, organizing modules, and preparing documentation.

The development process and AI assistance are documented separately in `AI_LOG.md`.