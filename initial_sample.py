"""from langchain_openai.llms import OpenAI
import os
from apikey import openai_key
os.environ['OPENAI_API_KEY'] = openai_key
llm = OpenAI(temperature=0.6)
print(llm("write a poem in 3 lines"))"""

from langchain.utilities import SQLDatabase

from langchain_experimental.sql import SQLDatabaseChain

from langchain_openai.llms import OpenAI
import os   
from apikey import openai_key
import streamlit as st
os.environ['OPENAI_API_KEY'] = openai_key
llm = OpenAI(temperature=0.6)

#credentials of myql workbench
db_user = ""
db_pass = ""
db_host = ""
db_name = "sales_inventory"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}",sample_rows_in_table_info =3)
#print(db.table_info)

db_chain = SQLDatabaseChain.from_llm(llm,db,verbose = True)


st.title("Employee Database Q&A")
question = st.text_input("Question: ")
if question:
    answer = db_chain.run(question)
    st.header("Answer: ")
    st.write(answer)