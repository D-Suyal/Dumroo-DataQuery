# Dumroo.ai – Data Query App

A Streamlit-based application for role-based CSV data analysis powered by OpenAI's GPT-4o via LangChain. Upload your CSV file, select your admin role, and chat with the AI to query your data — all with fine-grained access control based on your role.

---

## Features

* **Role-based access:** Only see data relevant to your admin role.
* **Conversational querying:** Chat interface for asking questions about uploaded CSV data.
* **OpenAI GPT-4o integration:** Natural language processing for smart data analysis.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/D-Suyal/Dumroo-DataQuery.git
cd Dumroo-DataQuery
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3 -m venv dumroo
source dumroo/bin/activate  # On Windows: dumroo\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
# Also install dependencies not listed in requirements.txt:
pip install python-dotenv pandas
```

### 4. Set Up OpenAI API Key

Create a `.env` file in the project root and add:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Or, you can securely enter your API key when prompted on first run.

---

## Usage

```bash
streamlit run app.py
```

* Select your admin role from the dropdown.
* Upload a CSV file (Sample file given named "student_data.csv").
* Ask questions in the chat box!

---

## Project Structure

```
.
├── app.py                # Streamlit main app
├── src
|   ├──avatars/          # Avatar images for roles (e.g., dumroo_assistant.png)
|   |   └──dumroo_assistant.png
|   ├──utils/
|   │   ├── api.py
|   │   ├── chat.py
|   │   ├── llm.py
|   │   └── roles.py
|   └──app.py
├── .env                  # (add your OpenAI API Key here)
├── requirements.txt
└──student_data.csv
```

---

## Dependencies

**In `requirements.txt`:**

* langchain
* langchain-experimental
* langchain-openai
* streamlit
* tabulate

**Install additionally:**

* python-dotenv
* pandas

```bash
pip install python-dotenv pandas
```

---

## Notes

* Ensure avatar images exist in `src/avatars/` as referenced in `roles.py`.
* Your OpenAI key must have access to GPT-4o (or update `llm.py` for a different model).

---

## License

MIT