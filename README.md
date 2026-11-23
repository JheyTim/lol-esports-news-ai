
# League of Legends Esports News AI

An AI-powered League of Legends esports news platform.

## Project Goals

- Collect esports news.
- Extract article information.
- Analyze news using AI.
- Generate news content.
- Manage image and video assets.
- Require human approval before publishing.
- Manage copyright and permissions.
- Integrate Facebook publishing.

## Technology Stack

- Python 3.14
- FastAPI
- SQLite
- Streamlit
- Groq
- GPT-OSS 120B
- FFmpeg
- Meta Graph API

## Project Structure

```text
lol-esports-news-ai/
├── app/
│   ├── routers/
│   ├── database.py
│   ├── schemas.py
│   └── main.py
├── dashboard/
├── tests/
├── data/
├── requirements.txt
└── README.md
```

## Installation

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run FastAPI

```powershell
python -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## Run Streamlit

Open another terminal:

```powershell
python -m streamlit run dashboard/app.py
```

## Development Budget

Target: ₱0 during the initial development period.

Paid services require prior approval.
