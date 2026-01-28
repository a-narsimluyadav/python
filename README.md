# Hello World (Port 8000) - Sample Python Project

This repo contains a tiny Flask web app (`app.py`) that runs on port **8000**.

## How to run (Windows PowerShell)

1) Open PowerShell
2) Go to your project folder:

```powershell
cd "C:\python project"
```

3) (Recommended) Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4) Install requirements:

```powershell
pip install -r .\requirements.txt
```

5) Run the server (listens on `http://127.0.0.1:8000`):

```powershell
python .\app.py
```

6) Test in your browser:
- Open `http://127.0.0.1:8000/` and you should see: `Hello, World!`


