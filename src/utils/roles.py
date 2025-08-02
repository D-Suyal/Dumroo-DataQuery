import streamlit as st
from enum import IntEnum, StrEnum

class REGION(StrEnum):
    INDIA = "INDIA",
    USA = "USA"

class VALID_CLASSES(IntEnum):
    CLASS_4 = 4,
    CLASS_5 = 5


ROLE_DATA = {
    "grade_5_admin": {
        "avatar": "👩‍🏫",
        "region": None,
        "grade": "5"
    },
    "usa_grade_4_admin": {
        "avatar": "👨‍🏫",
        "region": "USA",
        "grade": "4"
    },
    "usa_head_admin": {
        "avatar": "🧑‍💼",
        "region": "USA",
        "grade": None
    },
    "india_head_admin": {
        "avatar": "🧑‍💼",
        "region": "INDIA",
        "grade": None
    },
    "super_admin": {
        "avatar": "👑",
        "region": None,
        "grade": None
    },
    "dumroo_assistant": {
        "avatar": "src/avatars/dumroo_assistant.png",
        "region": None,
        "grade": None
    }
}

def get_avatar(role: str):
    return ROLE_DATA.get(role, {}).get("avatar", "💬")

def filter_dataframe_by_role(df, role: str):
    info = ROLE_DATA.get(role, {})
    admin_grade = info.get('grade')
    admin_region = info.get('region')

    if role in ["super_admin"]:
        return df.copy()

    if admin_grade is None and admin_region:
        return df[df['country'].str.upper() == str(admin_region).upper()]

    if admin_grade and admin_region:
        return df[
            (df['country'].str.upper() == str(admin_region).upper()) &
            (df['grade'].astype(str) == str(admin_grade))
        ]

    if admin_grade and not admin_region:
        return df[df['grade'].astype(str) == str(admin_grade)]

    return df.head(0)
