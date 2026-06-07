# Assignment 3 — Django ChatterBot Terminal Client

A terminal chat client built with Django and [ChatterBot](https://docs.chatterbot.us/). Type messages in the terminal and receive bot replies in an interactive loop.

## Requirements

- Python 3.9–3.12
- Dependencies listed in [`requirements.txt`](requirements.txt)

## Project Structure

```
Assignment 3/
├── manage.py
├── chatbot_project/          # Django settings and ChatterBot config
├── terminal_chat/            # Bot factory and management commands
│   ├── bot.py
│   └── management/commands/
│       ├── chat.py           # Interactive terminal chat
│       └── trainbot.py       # Corpus training
└── requirements.txt
```

## Setup

Open PowerShell and run:

```powershell
cd "D:\Assignments\UCAssignments\AIClass\Assignment 3"

# Create a virtual environment (skip if .venv already exists)
python -m venv .venv

# Activate the virtual environment — required before running manage.py
.\.venv\Scripts\Activate.ps1

# Install dependencies (Django, ChatterBot, corpus, spaCy model, etc.)
pip install -r requirements.txt

# Create ChatterBot database tables
python manage.py migrate django_chatterbot

# Train the bot from the English corpus (run once; takes ~1–2 minutes)
python manage.py trainbot
```

If PowerShell blocks the activation script:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

When the venv is active, your prompt shows `(.venv)` at the beginning.

## Running the Chatbot

With the virtual environment activated:

```powershell
python manage.py chat
```

Example session:

```text
Type a message to begin. Enter "exit" or "quit" to leave.

user: Good morning! How are you doing?
bot: I am doing well, how about you?
user: You're welcome.
bot: Do you like hats?
user: quit
```

### Without activating the venv

You can call the venv Python directly:

```powershell
.\.venv\Scripts\python.exe manage.py chat
```

### Controls

| Input | Action |
|-------|--------|
| Any message | Bot replies with `bot: ...` |
| `exit` or `quit` | End the session |
| `Ctrl+C` | End the session |

## Troubleshooting

| Error | Solution |
|-------|----------|
| `Couldn't import Django` | Activate `.venv` first, or use `.\.venv\Scripts\python.exe manage.py chat` |
| `Can't find model 'en_core_web_sm'` | Run `pip install -r requirements.txt` |
| `Unable to import "yaml"` | Run `pip install -r requirements.txt` |
| Weak or odd replies | Run `python manage.py trainbot` before chatting |

## Repository

GitHub: https://github.com/sdhamania/Assignment-3
