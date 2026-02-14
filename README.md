# House of Developers - Falppy Bird Hackathon 🎮

Our first hackathon project! A Flappy Bird game with cool crypto stuff—each player gets a unique avatar that gets hashed (blockchain vibes).

## What Does It Do?

Play Flappy Bird against other players. Your avatar is randomly generated and hashed with SHA-256, which stores it in the database so you're verified every time you log in. Basically our attempt at building a blockchain vibe into a game.

## Features

- User login/registration
- Procedurally generated avatars for each player
- SHA-256 hashing (blockchain energy ⛓️)
- Track scores and compete against others
- MySQL database to store everything

## Project Files

- **Falppy Mario.py** - The game itself
- **HackathonEncrypt.py** - Hashing the avatars (SHA-256)
- **HackatonImageGenerator.py** - Making random unique avatars
- **input_inp.py** - Login stuff
- **HashToIMG.py** - Storing hashes in the database

## Requirements

### Dependencies
```
pygame
Pillow (PIL)
mysql-connector-python
hashlib (built-in)
```

### Database
- MySQL Server (localhost)
- Default credentials: user="root", password="tiger"
- Database name: test1

### Game Assets
The project expects the following image files in the `images/` directory:
- `pipe2.png` - Pipe obstacles
- `bg4.jpg` - Background image
- `bird.png` - Player sprite
- `base2.png` - Ground sprite
- Additional image variants for visual variety

## Installation
How to Run

**Prerequisites:**
- Python 3.x
- MySQL server running locally
- `pip install pygame pillow mysql-connector-python`

**Setup:**
1. Make sure MySQL is running with user "root" and password "tiger"
2. Add game assets to the `images/` folder
3. Run: `python "Falppy Mario.py"`

**Playing:**
1. Enter username and password
2. Pick someone to compete against
3. Try to beat their high score!

## Cool Parts

The blockchain idea: your avatar → hash → stored forever in DB. It's like a mini blockchain where your avatar is immutably linked to your account via a cryptographic hash.

---

Made for our first hackathon! 🚀
