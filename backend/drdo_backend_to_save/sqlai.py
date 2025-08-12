import openai
import mysql.connector

# Set API key
openai.api_key = "OPENAI_API_KEY"

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divyanshusharmamysql@8",
    database="FighterJetDB"
)
cursor = conn.cursor()

# Get user input
question = input("Ask your question: ")

# New Chat API call
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful SQL assistant. Convert natural language to MySQL queries "
                "for the following schema:\n"
                "- FighterJets(jet_id, name, model, manufacturer, range_km, max_speed_kmph, status)\n"
                "- FlightLogs(flight_id, jet_id, takeoff_time, landing_time, date, fuel_consumed_liters)"
            )
        },
        {"role": "user", "content": question}
    ]
)

# Extract SQL query
sql_query = response.choices[0].message["content"].strip().strip(";")

print("\n🔍 Generated SQL Query:")
print(sql_query)

# Execute the query
try:
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    
    print("\n📊 Result:")
    for row in rows:
        print(row)
except Exception as e:
    print("❌ Error executing query:", e)

cursor.close()
conn.close()
