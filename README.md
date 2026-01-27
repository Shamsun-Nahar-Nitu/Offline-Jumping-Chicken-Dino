# 🐔 Chicken Runner Game

A fun, retro-style endless runner game inspired by Chrome's offline dinosaur game, but with a cute pixel art chicken!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 About The Game


https://github.com/user-attachments/assets/cf0b9c27-22d9-4228-a163-de453cee0205



Chicken Runner is an endless running game where you control a brave chicken trying to avoid cacti obstacles. The game features:

- **Pixel Art Chicken**: Hand-crafted pixel art character with running animation
- **Progressive Difficulty**: Game speed increases over time
- **Score Tracking**: Keep track of your high scores
- **Smooth Animations**: Scrolling ground, flying clouds, and animated chicken
- **Simple Controls**: Just press SPACE to jump!


## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shamsun-Nahar-Nitu/Offline-Jumping-Chicken-Dino.git
   cd Offline-Jumping-Chicken-Dino
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

## 🎯 How to Play

1. **Start the Game**: Press `SPACE` on the start screen
2. **Jump**: Press `SPACE` to make the chicken jump over cacti
3. **Avoid Obstacles**: Don't let the chicken hit the cacti
4. **Beat Your High Score**: Try to survive as long as possible!

## 📁 Project Structure

The game is organized into modular Python files for clean code architecture:

```
Offline-Jumping-Chicken-Dino/
│
├── main.py              # Main game loop and entry point
├── game_config.py       # Game constants and configuration
├── chicken.py           # Chicken character with pixel art and physics
├── obstacle.py          # Obstacle generation and management
├── ground.py            # Scrolling ground implementation
├── cloud.py             # Background cloud system
├── score.py             # Score tracking and display
└── README.md            # Project documentation
```

### File Descriptions

- **main.py**: Contains the main game loop, event handling, and game state management
- **game_config.py**: Stores all game constants like screen size, colors, speeds, and physics values
- **chicken.py**: Defines the Chicken class with pixel art drawing, jumping physics, and collision detection
- **obstacle.py**: Manages cactus obstacles including spawning, movement, and collision checking
- **ground.py**: Creates the infinite scrolling ground effect using two alternating segments
- **cloud.py**: Handles decorative background clouds with parallax scrolling
- **score.py**: Tracks player score and high score with display formatting

## 🎨 Game Features

### Chicken Character
- Custom pixel art design
- Animated running legs
- Realistic jump physics with gravity
- Collision detection

### Obstacles
- Three types of cacti (small, medium, large)
- Random spawning system
- Increasing difficulty over time

### Visual Effects
- Scrolling ground for movement illusion
- Parallax cloud movement
- Smooth animations at 60 FPS

### Scoring System
- Real-time score updates
- High score tracking
- Score display with leading zeros


## 🎓 Learning Objectives

By studying this code, you'll learn:

1. **Game Development Basics**: Understanding game loops, frame rates, and game states
2. **Pygame Fundamentals**: Working with surfaces, sprites, and rendering
3. **Physics Simulation**: Implementing gravity and jumping mechanics
4. **Animation Techniques**: Creating smooth character animations
5. **Collision Detection**: Checking intersections between game objects
6. **Code Organization**: Structuring a multi-file Python project

## 🎮 Controls

| Key | Action |
|-----|--------|
| `SPACE` | Start Game / Jump / Restart |
| `ESC` or `X` | Quit Game |

## 🔧 Customization

Want to modify the game? Here are some easy tweaks:

### Change Game Speed
In `game_config.py`:
```python
INITIAL_GAME_SPEED = 6  # Change to make game faster/slower
SPEED_INCREMENT = 0.005  # Change how quickly difficulty increases
```

### Modify Jump Height
In `game_config.py`:
```python
JUMP_STRENGTH = -20  # Increase for higher jumps (more negative = higher)
GRAVITY = 1.2  # Decrease for floatier jumps
```

### Adjust Screen Size
In `game_config.py`:
```python
SCREEN_WIDTH = 800  # Change window width
SCREEN_HEIGHT = 400  # Change window height
```

## 🐛 Troubleshooting

### Game won't start
- Make sure Python 3.7+ is installed: `python --version`
- Verify Pygame is installed: `pip show pygame`
- Check all 7 Python files are in the same directory

### Import errors
- Ensure all files are in the same folder
- Check that file names match exactly (case-sensitive)
- Verify no file is empty

### Performance issues
- Lower the FPS in `game_config.py`
- Close other applications
- Update your graphics drivers

## 🤝 Contributing

Contributions are welcome! 

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Shamsun Nahar Nitu**
- GitHub: [@Shamsun-Nahar-Nitu](https://github.com/Shamsun-Nahar-Nitu)

## 🙏 Acknowledgments

- Inspired by Chrome's offline dinosaur game
- Built with Python and Pygame
- Created as a learning project for game development


---

**Happy Gaming! 🎮🐔**

*Remember: The chicken crossed the road... can you help it avoid the cacti?*
