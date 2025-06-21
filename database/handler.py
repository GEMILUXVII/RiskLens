
import sqlite3

def init_db():
    """Initializes the database and creates the logs table if it doesn't exist."""
    conn = sqlite3.connect('simulation_log.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            location TEXT,
            risk_type TEXT,
            probability REAL,
            risk_level REAL
        )
    ''')
    conn.commit()
    conn.close()

def log_simulation(timestamp, location, risk_type, probability, risk_level):
    """Logs a simulation event to the database."""
    conn = sqlite3.connect('simulation_log.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (timestamp, location, risk_type, probability, risk_level) VALUES (?, ?, ?, ?, ?)",
        (timestamp, location, risk_type, probability, risk_level)
    )
    conn.commit()
    conn.close()
