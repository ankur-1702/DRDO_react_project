import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Divyanshusharmamysql@8",
        database="FighterJetDB"
    )
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("✅ Connected successfully!")
    print("📂 Tables in FighterJetDB:")
    for table in tables:
        print("-", table[0])

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("❌ Connection failed:", err)

