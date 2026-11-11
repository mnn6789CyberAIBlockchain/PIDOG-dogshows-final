# 🐶 PiDog Interactive AI-Powered Robotic Performer

## PIDOG-dogshows-final

An interactive robotic performance project built using the **SunFounder PiDog**, **Raspberry Pi 5**, Python, coordinated movement, RGB lighting, music playback, and an **Ollama-powered local Large Language Model (LLM)**.

The project transforms PiDog into an interactive robotic performer capable of performing choreographed shows, responding to human interaction, and participating in AI-powered question-and-answer conversations.

---

# 🎯 Project Overview

The goal of this project is to demonstrate multiple capabilities of the SunFounder PiDog platform by combining:

- 🦿 Robotic movement and servo control
- 🎵 Music-based performances
- 💡 RGB lighting effects
- 🐶 Coordinated dance and movement choreography
- 👂 Interactive attention behavior
- 🚶 Human-directed movement
- 🐾 Physical high-five interaction
- 🧠 Local AI integration using Ollama
- 💬 Interactive AI question-and-answer conversations

The final project is designed as a complete robotic performance and interactive demonstration.

---

# 🎬 Final Performance Flow

The complete PiDog performance follows this sequence:

## Part 1 — PiDog Introduction

PiDog introduces its capabilities using movement, head gestures, tail movement, and RGB lighting.

**Demonstrated features:**

- Standing
- Tail wagging
- Head movement
- RGB lighting
- Robotic introduction sequence

---

## Part 2 — Christmas Performance 🎄

PiDog performs a choreographed movement and light show synchronized with Christmas music.

**Demonstrated features:**

- Coordinated movement
- Music playback
- RGB lighting
- Servo choreography

---

## Part 3 — Pokémon Performance ⚡

PiDog performs a second choreographed performance using Pokémon-themed music and movement.

**Demonstrated features:**

- Coordinated movement
- Music playback
- RGB lighting
- Robotic choreography

---

## Part 4 — Interactive Human-PiDog Performance 👏🐾

After the Pokémon performance, PiDog transitions into an interactive sequence with a human interviewer.

### Interaction Flow

```text
Pokémon Performance
        ↓
Human claps
        ↓
PiDog reacts and gains attention
        ↓
Human says: "PiDog, come here!"
        ↓
PiDog walks toward the interviewer
        ↓
Human says: "PiDog, high five!"
        ↓
Right paw high five
        ↓
Left paw high five
        ↓
PiDog celebration
```

This section is designed to demonstrate additional interactive and physical capabilities of PiDog.

---

## Part 5 — AI-Powered Q&A 🧠

After the physical performance, PiDog participates in a live AI-powered question-and-answer session.

The system uses a local **Ollama LLM** to generate PiDog's responses.

Example questions include:

- Who are you?
- What can you do?
- Are you a real dog?
- Can you dance?
- What was your favorite performance?

PiDog can also perform physical reactions while processing and responding to questions.

---

# 🧠 AI Integration

The project integrates **Ollama** as a local AI engine.

PiDog's AI system is designed to provide:

- Natural language responses
- A robotic PiDog personality
- Interactive conversations
- Local AI processing
- No required paid cloud AI API

The AI functionality is handled primarily by:

```text
ai/ollama_brain.py
ai/command_handler.py
ai/pidog_reactions.py
```

---

# 🏗️ Project Structure

```text
PIDOG-dogshows-final/
│
├── app.py
├── pidog_controller.py
├── README.md
├── requirements.txt
│
├── ai/
│   ├── command_handler.py
│   ├── ollama_brain.py
│   └── pidog_reactions.py
│
├── audio/
│   └── music_player.py
│
├── music/
│   ├── christmas_song.wav
│   └── pokemon_song.wav
│
├── shows/
│   ├── introduction_show.py
│   ├── christmas_show.py
│   ├── pokemon_show.py
│   ├── interactive_show.py
│   ├── final_qa.py
│   ├── demo_show.py
│   └── show_manager.py
│
└── tests/
```

---

# ⚙️ Technologies Used

- Python
- Raspberry Pi 5
- SunFounder PiDog
- SunFounder PiDog Python library
- Robot HAT
- Ollama
- Local Large Language Model (LLM)
- WAV audio playback
- Python threading
- Cross-platform audio support

---

# 💻 Running the Project

## Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

## Navigate to the project

```bash
cd PIDOG-dogshows-final
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python app.py
```

---

# 🎵 Cross-Platform Music Support

The project supports music playback on multiple operating systems.

### Windows

Music can play through the laptop speakers using Python's built-in Windows audio support.

### Raspberry Pi / Linux

Music playback uses the Linux audio system and can be routed through the Raspberry Pi's configured audio output.

---

# 🐶 Hardware Requirements

For the full robotic performance, the project is designed to run with:

- Raspberry Pi 5
- SunFounder PiDog
- Robot HAT
- PiDog servo system
- PiDog sensors
- Audio output or speaker

The software can also run in **simulation mode** on a Windows computer when PiDog hardware is not available.

---

## 🐶 Raspberry Pi / PiDog Setup

For real hardware operation, the SunFounder PiDog Python environment and required hardware libraries must be installed on the Raspberry Pi according to the official SunFounder PiDog documentation.

The project automatically detects whether PiDog hardware is available:

- If PiDog is connected, real hardware commands are used.
- If PiDog is unavailable, the application runs in simulation mode.

### Ollama

The AI Q&A system requires Ollama to be running locally:

```bash
ollama serve


# 🧪 Simulation Mode

When the SunFounder PiDog hardware library is not available, the project can display simulated robot actions.

Example:

```text
[SIMULATION] Action: stand
[SIMULATION] Action: forward
[SIMULATION] Light → green
[SIMULATION] Head movement
```

This allows development and testing of the application logic before connecting to the physical robot.

---

# 🎯 Key Learning Objectives

This project demonstrates:

- Python robotics programming
- Servo and robotic movement control
- Raspberry Pi development
- Human-robot interaction
- AI and robotics integration
- Local Large Language Model integration
- Interactive system design
- Audio and movement coordination

---

# 🚀 Future Improvements

Possible future improvements include:

- Real-time voice recognition
- Real sound-direction detection
- Voice commands for PiDog
- Improved sensor-based navigation
- Object recognition using the PiDog camera
- Advanced autonomous behavior
- More AI-driven physical reactions
- Additional interactive performances

---

# 👨‍💻 Author

**Tien Manh Nguyen**

PiDog Final Project

---

# 📝 Project Status

🚧 **Active Development**

The project currently supports:

- PiDog introduction sequence
- Christmas performance
- Pokémon performance
- Interactive human-PiDog sequence
- AI-powered Q&A using Ollama
- Windows simulation mode
- Cross-platform music support

Hardware-specific features will be tested and finalized using the physical SunFounder PiDog and Raspberry Pi 5.
