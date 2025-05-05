import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "memory.db"

class Memory:
    """Indefinite persistent memory (no expiry)."""

    def __init__(self, db_path: Path = DB_PATH):
        self.conn = sqlite3.connect(db_path)
        self._ensure_schema()

    # ---------- private helpers ----------
    def _ensure_schema(self):
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS memory(
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT    NOT NULL,
                entry     TEXT    NOT NULL
            )
            """
        )
        self.conn.commit()

    # ---------- public API ----------
    def add(self, text: str):
        ts = datetime.utcnow().isoformat()
        self.conn.execute(
            "INSERT INTO memory(timestamp, entry) VALUES (?,?)", (ts, text)
        )
        self.conn.commit()

    def recall(self) -> list[str]:
        cur = self.conn.execute("SELECT entry FROM memory ORDER BY id")
        return [row[0] for row in cur.fetchall()]

    def get_recent(self, limit=1000):
        cur = self.conn.execute("SELECT entry FROM memory ORDER BY id DESC LIMIT ?", (limit,))
        return [row[0] for row in reversed(cur.fetchall())]

# singleton for import convenience
memory = Memory()
