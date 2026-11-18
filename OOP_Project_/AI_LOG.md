# AI Collaboration Log — Ninja Target Master

**Project:** Ninja Target Master (2D Arcade Target-Shooting Game)  
**Language and framework:** Python 3 and Pygame  
**Team members:** Prasant, Kaung Htet, Shan  
**AI tools:** ChatGPT (OpenAI); Gemini only if actually used

---

## 1. Purpose and Team Responsibilities

This log records how AI assistance was used during the development of Ninja Target Master. It covers the design ideas discussed, prompts or requests made to AI, code and suggestions received, student implementation or revisions, and testing.

**Important disclosure:** The prompts below are reconstructed summaries of the design discussions, not verbatim transcripts. They must not be presented as exact historical messages. The named responsibilities and individual testing descriptions should be confirmed by all three teammates before submission. Where exact AI-generated code is required by the course policy, attach or reference the relevant original chat excerpts.

**Prasant —** Core configuration, level design, and scoreboard encapsulation (`settings.py`, `level.py`, `scoreboard.py`).

**Kaung Htet —** Ninja movement, shuriken behavior, target hierarchy, and collisions (`ninja.py`, `shuriken.py`, `targets.py`).

**Shan —** Main game loop, game states, user interface, integration, and documentation (`Project.py`, `README.md`, `AI_LOG.md`).

---

## 2. AI Collaboration and Development Log

---

### Phase 1 — Project Architecture and Configuration
**Assigned member:** Prasant  
**Files:** `settings.py`, `level.py`

---

#### Prompt 1.1 — Game Settings and Dojo Theme

**Prompt summary (paraphrased):**  
“Our idea is a ninja-themed arcade game set inside a Japanese dojo. I want the screen dimensions, frame rate, and colors kept in a separate `settings.py` file so the rest of the game can reuse them. What constants and structure would you suggest?”

**AI assistance and code received:**  
ChatGPT suggested organizing reusable Pygame settings as constants, including `WIDTH = 960`, `HEIGHT = 640`, `FPS = 60`, and RGB color tuples.

**Student implementation and revisions:**  
The project uses a dojo-inspired palette, including `WALL = (95, 72, 60)`, `WOOD = (145, 105, 75)`, `BEAM = (55, 40, 38)`, and `GOLD = (230, 190, 110)`.

**Validation:**  
The team checked that the game window and dojo background rendered using the shared settings.

---

#### Prompt 1.2 — Level Design and Progression

**Prompt summary (paraphrased):**  
“I want three levels with the same countdown but higher score requirements as the player progresses. My proposed goals are 150, 250, and 350 points within 60 seconds. Would a separate `Level` class be a good way to organize this?”

**AI assistance and code received:**  
ChatGPT suggested a `Level` constructor receiving a level number and using conditional statements to assign the corresponding score goal and time limit.

**Student implementation and revisions:**  
The final `Level` class stores `number`, `time_limit`, and `goal`, using 60 seconds and the three proposed score thresholds.

**Validation:**  
The team checked progression through all three levels during gameplay testing.

---

### Phase 2 — Scoreboard and Encapsulation
**Assigned member:** Prasant  
**File:** `scoreboard.py`

---

#### Prompt 2.1 — Protecting Score and Timer Values

**Prompt summary (paraphrased):**  
“I want danger targets to subtract points, but the score should never become negative. The timer should also stop at zero. I'm thinking of using private-style backing attributes and Python properties. Would getters and setters be suitable here?”

**AI assistance and code received:**  
ChatGPT provided examples of `@property` getters and setters, including nonnegative-value checks such as `if value < 0: value = 0`.

**Student implementation and revisions:**  
The scoreboard uses `_score` and `_time_left` with public `score` and `time_left` properties. A missing `time_left` setter was corrected during debugging.

**Validation:**  
The team checked that penalties did not make the score negative and that the countdown stopped at zero.

---

#### Prompt 2.2 — Accuracy and Score Display

**Prompt summary (paraphrased):**  
“I want the scoreboard to show the score, time remaining, and current goal. It should also calculate shooting accuracy from hits and misses. What is a reliable way to handle accuracy before the player has fired any shurikens?”

**AI assistance and code received:**  
ChatGPT suggested the formula `(hits / (hits + misses)) * 100` and a guard clause returning zero when no shots have been recorded.

**Student implementation and revisions:**  
The scoreboard includes `get_accuracy()` and a HUD showing score, countdown, and level goal.

**Validation:**  
The team checked the HUD and the zero-shot accuracy case during game testing.

---

### Phase 3 — Player Movement and Shuriken Physics
**Assigned member:** Kaung Htet  
**Files:** `ninja.py`, `shuriken.py`

---

#### Prompt 3.1 — Ninja Movement

**Prompt summary (paraphrased):**  
“Our ninja should move with either WASD or the arrow keys, but I want the character to remain within the bottom training area. What movement and boundary-checking approach would work best in Pygame?”

**AI assistance and code received:**  
ChatGPT suggested using `pygame.key.get_pressed()` for continuous movement and boundary clamping to keep the character on screen.

**Student implementation and revisions:**  
The movement boundaries were set to keep the ninja within the intended training area, and the character was drawn using Pygame shapes.

**Validation:**  
The team tested movement in different directions and near the screen boundaries.

---

#### Prompt 3.2 — Mouse-Aimed Shurikens

**Prompt summary (paraphrased):**  
“I want the ninja to throw a shuriken toward wherever the player clicks. The projectile should travel at a consistent speed even when the cursor is close to or far from the ninja. What calculation would you recommend?”

**AI assistance and code received:**  
ChatGPT suggested calculating a direction vector, dividing by its length to normalize it, and multiplying by the chosen speed. It also discussed guarding against zero-distance division.

**Student implementation and revisions:**  
The `Shuriken` class uses direction components `dx` and `dy`, speed, drawing logic, and an off-screen check.

**Validation:**  
The team tested shooting in multiple directions and removing shurikens that left the screen.

---

### Phase 4 — Target Classes and Collision Detection
**Assigned member:** Kaung Htet  
**File:** `targets.py`

---

#### Prompt 4.1 — Target Types and Inheritance

**Prompt summary (paraphrased):**  
“I want four kinds of targets: a normal target worth 10 points, a faster target worth 20, a golden bonus target worth 50, and a danger target worth minus 20. I also want the design to demonstrate abstraction, inheritance, and polymorphism. What class hierarchy would you suggest?”

**AI assistance and code received:**  
ChatGPT explained Python's `ABC` and `@abstractmethod` features and suggested a shared interface with `draw()` and `get_points()` methods.

**Student implementation and revisions:**  
`BaseTarget` defines the abstract interface. `Target` and `FastTarget` inherit directly from it; `GoldenTarget` and `DangerTarget` inherit from `Target`, reusing its movement and collision behavior.

**Validation:**  
The team tested the four target types and their different scoring effects during gameplay.

---

#### Prompt 4.2 — Collision Detection

**Prompt summary (paraphrased):**  
“Since the shurikens and targets are approximately circular, I want hits to register when their visible areas touch. Would comparing the distance between their centers with their combined radii be a suitable method?”

**AI assistance and code received:**  
ChatGPT suggested a circle-to-circle collision check using Euclidean distance and the condition `distance <= target.radius + shuriken.radius`.

**Student implementation and revisions:**  
The `is_hit()` methods use the circle-distance approach. The target radii are 28 for normal, 20 for fast, 24 for golden, and 26 for danger.

**Validation:**  
The team tested hits against moving targets, including direct hits and near-edge contact.

---

### Phase 5 — Game Loop and Integration
**Assigned member:** Shan  
**File:** `Project.py`

---

#### Prompt 5.1 — Connecting the Classes and Game States

**Prompt summary (paraphrased):**  
“We now have separate classes for the ninja, projectiles, targets, scoreboard, and levels. I want one `Game` class to coordinate them. The game should have menu, playing, paused, and result states. How would you organize event handling and screen updates?”

**AI assistance and code received:**  
ChatGPT suggested a Pygame main loop, event handling through `pygame.event.get()`, and conditional behavior based on `self.state`.

**Student implementation and revisions:**  
`Game` coordinates the modules, handles target creation and collisions, and draws the dojo, menu, pause, and result screens. Controls include ENTER to start, P to pause or resume, SPACE to advance after winning, R to restart, and ESC to exit.

**Validation:**  
The team completed a final gameplay checklist covering 13 functions, including movement, shooting, scoring, pausing, restarting, progression, victory, and exit.

---

## 3. Collaborative Debugging and Troubleshooting Log

The following table summarizes the issues discussed during development, the AI assistance received, and how the resulting changes were checked. Items described as preventive checks are not necessarily errors that occurred during execution.

| Issue / Module | Assigned member | Problem or risk | AI assistance | Revision and validation |
|:---|:---|:---|:---|:---|
| **Missing `time_left` setter** (`scoreboard.py`) | Prasant | Updating `time_left` raised an `AttributeError` because its setter was missing or incorrectly placed. | Explained the `@property` and `@time_left.setter` pattern. | Corrected the setter to clamp negative time to zero; confirmed the countdown worked. |
| **Zero-shot accuracy** (`scoreboard.py`) | Prasant | Calculating accuracy before any shots could cause division by zero. | Suggested checking whether `hits + misses == 0` before dividing. | Added the zero-attempt guard; checked initial accuracy without a crash. |
| **Zero-length direction vector** (`shuriken.py`) | Kaung Htet | Clicking at the projectile's starting point could cause division by zero during normalization. | Explained the need for a zero-distance guard. | Included a zero-distance check; tested firing toward different cursor positions. |
| **Missing `Level` import** (`Project.py`) | Shan | Refactoring `Level` into `level.py` caused `NameError: name 'Level' is not defined`. | Identified the missing module import. | Added `from level import Level`; confirmed the game started. |

---

## 4. Final Disclosure and Validation

AI was used for programming suggestions, class organization, examples of Python/Pygame code, debugging, explanations of OOP concepts, and assistance with project documentation and the UML diagram. The team incorporated and reviewed AI-assisted suggestions as part of the game development process.

The final project contains seven Python source files, `README.md`, `AI_LOG.md`, and a simplified UML class diagram. The team reported successful completion of 13 gameplay tests. Syntax checks also passed for all seven Python files.

**Academic integrity note:** This log summarizes the collaboration and does not substitute for an exact prompt/code transcript if the instructor requires one. Before submission, the team should confirm the assigned authorship, specific individual revisions, any use of Gemini, and each validation statement. Include the original AI prompts and received code excerpts where required.
