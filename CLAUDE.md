# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A personal Streamlit dashboard ("Personal Intelligence Dashboard") that aggregates data from Google Sheets, GitHub, weather APIs, and Google Calendar into a single web UI. Authentication is handled via credentials stored in a Google Sheets worksheet.

## Running the App

```bash
pip install -r requirements.txt
streamlit run main.py
```

No build step, no linter config, no test suite exists in the repo.

## Required Environment Variables

Create a `.env` file (gitignored) with:

```
GOOGLE_SHEETS_ID=<spreadsheet id from the URL>
GOOGLE_SERVICE_ACCOUNT_JSON=<full JSON string of the service account key file>
GITHUB_TOKEN=<optional, avoids rate limiting>
GITHUB_USERNAME=ericklie95
WEATHER_LAT=-33.8688
WEATHER_LON=151.2093
```

`GOOGLE_SERVICE_ACCOUNT_JSON` must be the entire JSON key file contents as a single-line string, not a file path.

## Architecture

```
main.py          → calls app.run()
app.py           → Streamlit page config, sidebar, 3 tabs
auth.py          → login/register logic (SHA-256 hashed passwords)
config.py        → loads .env via python-dotenv, exports constants
components/      → one function per UI section, rendered inside tabs
services/        → thin wrappers around external APIs
```

**Data flow**: All persistent state (users, logged metrics) lives in a Google Sheets spreadsheet. `services/sheets.py` is the only DB layer — it reads/writes named worksheets by tab name. The `_get_client()` function is cached with `@st.cache_resource` so the gspread connection is shared across rerenders. Data fetched from GitHub and weather APIs is cached with `@st.cache_data(ttl=...)`.

**Authentication**: `st.session_state["authenticated"]` is the gate. `sidebar_display()` (called unconditionally in `app.run()`) owns all login/register UI and writes to session state. Everything else checks `st.session_state.get("authenticated")` before rendering.

**Google Sheets as database**: The spreadsheet has at minimum two worksheets:
- `users` — columns: `username`, `email`, `password_hash`, `created_at`
- `data_to_visualise` — columns: `date`, `github_commits`, `notes` (used by analytics tab)

## Incomplete / In-Progress Areas

- `display_todays_overview()` is imported and called in `app.py` but the import is commented out — the function exists in `components/overview.py`. Uncomment the import to activate Tab 1.
- Tabs 2 (Performance Analytics) and 3 (Quick Actions) are implemented in `components/analytics.py` and `components/quick_actions.py` but their calls in `app.py` are inside a docstring block (effectively disabled).
- `services/calendar.py` is a stub — `get_today_events()` always returns `[]`. Full implementation requires Google Calendar OAuth 2.0 setup.

## Adding a New Service Integration

1. Create `services/<name>.py` with functions decorated with `@st.cache_data(ttl=<seconds>)`.
2. Add any new env vars to `config.py` using `os.getenv()`.
3. Call the service from the appropriate component in `components/`.
4. Errors from services should be caught and shown with `st.warning(...)`, not raised, so one broken integration doesn't block the whole dashboard.
