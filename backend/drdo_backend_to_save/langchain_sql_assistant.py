from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import mysql.connector
import re

# Initialize the LLM
llm = Ollama(model="gemma:2b")

# ✅ Use actual table schema
table_info = """
CREATE TABLE fighterjets (
    jet_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    model VARCHAR(100),
    manufacturer VARCHAR(100),
    range_km INT,
    max_speed_kmph INT,
    status VARCHAR(50)
);
"""

# ✅ Updated prompt template
prompt = PromptTemplate(
    input_variables=["question", "table_info"],
    template="""
You are an AI assistant. Convert the user's natural language question into a syntactically correct MySQL query.

Here is the database schema:
{table_info}

Question: {question}
SQL Query:
"""
)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

# Take user input
user_question = input("Ask your question: ")

# Run the chain
response = chain.run({
    "question": user_question,
    "table_info": table_info
})

# Display raw response
print("\n🔍 Generated SQL Query (Raw):\n", response)

# Clean the SQL query
match = re.search(r"```sql\s*(.*?)\s*```", response, re.DOTALL)
if match:
    cleaned_sql = match.group(1).strip()
else:
    match = re.search(r"(SELECT\s+.*?;)", response, re.IGNORECASE | re.DOTALL)
    cleaned_sql = match.group(1).strip() if match else response.strip()

print("\n🧾 Cleaned SQL Query:\n", cleaned_sql)

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Divyanshusharmamysql@8',
    database='FighterJetDB'
)

cursor = connection.cursor()
try:
    cursor.execute(cleaned_sql)
    results = cursor.fetchall()

    print("\n📊 Results:")
    for row in results:
        print(row)
except Exception as e:
    print("❌ Error executing SQL:", e)

cursor.close()
connection.close()
