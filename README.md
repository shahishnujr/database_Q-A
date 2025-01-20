# Employee Database Q&A with Streamlit and LangChain

This project is a **Streamlit-based web application** that enables users to query an employee database using natural language. Powered by **LangChain** and **OpenAI**, the application dynamically converts user input into SQL queries and executes them on a MySQL database.

## Features

- **Natural Language Processing**: Accepts user questions in plain English and converts them into SQL queries.
- **Dynamic Schema Parsing**: Automatically retrieves and displays the database schema.
- **Interactive UI**: Displays generated SQL queries and query results in a user-friendly manner.
- **Error Handling**: Notifies users of issues like invalid queries or database errors.

## Prerequisites

To run this project, ensure you have:

1. **Python 3.8 or above** installed.
2. **MySQL database** with the schema provided in the code (`sales_inventory`).
3. API key for OpenAI, stored in a module named `apikey.py` with the variable `openai_key`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3.Configure your MySQL database credentials in main.py:

    db_user = "<your_mysql_username>"
    db_pass = "<your_mysql_password>"
    db_host = "<your_mysql_host>"
4. Set your OpenAI API key in the apikey.py file:
    ```bash
    openai_key = "your_openai_api_key"
##Usage
Run the application:

    streamlit run main.py
Open the application in your browser at http://localhost:.
Enter your natural language question in the text input field, and view the generated SQL query and query results.
