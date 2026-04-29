import json
import streamlit as st
import gspread
import config


@st.cache_resource
def _get_client():
    if not config.GOOGLE_SERVICE_ACCOUNT_JSON:
        raise ValueError("GOOGLE_SERVICE_ACCOUNT_JSON is not set in .env")
    creds_dict = json.loads(config.GOOGLE_SERVICE_ACCOUNT_JSON)
    return gspread.service_account_from_dict(creds_dict)


def _get_sheet(tab_name: str):
    if not config.GOOGLE_SHEETS_ID:
        raise ValueError("GOOGLE_SHEETS_ID is not set in .env")
    client = _get_client()
    return client.open_by_key(config.GOOGLE_SHEETS_ID).worksheet(tab_name)


def read_sheet(tab_name: str) -> list[dict]:
    sheet = _get_sheet(tab_name)
    return sheet.get_all_records()


def append_row(tab_name: str, row: dict):
    sheet = _get_sheet(tab_name)
    headers = sheet.row_values(1)
    values = [row.get(h, "") for h in headers]
    sheet.append_row(values)


def find_rows(tab_name: str, column: str, value: str) -> list[dict]:
    records = read_sheet(tab_name)
    return [r for r in records if str(r.get(column, "")) == str(value)]
