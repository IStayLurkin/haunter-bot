import json
import logging
import os
import threading
# import sqlite3 # Uncomment if/when implementing SQLite support

class ChatMemory:
    """
    Handles persistent storage and retrieval of chat conversation history.
    Currently supports JSON format. Designed to be thread-safe for basic operations.
    """
    def __init__(self, config: dict):
        """
        Initializes the memory handler based on configuration.
        Args:
            config (dict): The loaded application configuration.
        """
        mem_config = config.get('memory', {})
        self.memory_type = mem_config.get('type', 'json').lower()
        self.memory_path = mem_config.get('path')
        self.history = []
        self._lock = threading.Lock() # Lock for thread safety

        if not self.memory_path:
            raise ValueError("Memory path ('memory.path') not specified in configuration.")

        # Ensure the directory for the memory file exists
        memory_dir = os.path.dirname(self.memory_path)
        if memory_dir and not os.path.exists(memory_dir):
            try:
                os.makedirs(memory_dir)
                logging.info(f"Created memory directory: {memory_dir}")
            except OSError as e:
                logging.error(f"Failed to create memory directory {memory_dir}: {e}")
                raise

        # Load initial history
        if self.memory_type == 'json':
            self._load_json()
        # elif self.memory_type == 'sqlite':
        #     self._init_db() # Ensure table exists
        #     self._load_db()
        else:
            raise ValueError(f"Unsupported memory type specified in config: '{self.memory_type}'")

        logging.info(f"ChatMemory initialized. Type: {self.memory_type.upper()}, Path: {self.memory_path}, Initial messages: {len(self.history)}")

    def _load_json(self):
        """Loads history from the JSON file."""
        with self._lock: # Acquire lock for file access
            try:
                if os.path.exists(self.memory_path) and os.path.getsize(self.memory_path) > 0:
                    with open(self.memory_path, 'r', encoding='utf-8') as f:
                        self.history = json.load(f)
                    logging.info(f"Loaded {len(self.history)} messages from JSON file: {self.memory_path}")
                else:
                    self.history = []
                    logging.info(f"JSON memory file not found or empty ({self.memory_path}), starting new history.")
            except (json.JSONDecodeError, IOError) as e:
                logging.error(f"Error loading JSON memory from {self.memory_path}: {e}. History reset.")
                self.history = [] # Reset history on load error
            except Exception as e:
                 logging.error(f"Unexpected error loading JSON memory: {e}", exc_info=True)
                 self.history = []

    def _save_json(self):
        """Saves the current history to the JSON file."""
        with self._lock: # Acquire lock for file access
            try:
                with open(self.memory_path, 'w', encoding='utf-8') as f:
                    json.dump(self.history, f, indent=2, ensure_ascii=False)
                logging.debug(f"Saved {len(self.history)} messages to JSON file: {self.memory_path}")
            except IOError as e:
                logging.error(f"Error saving JSON memory to {self.memory_path}: {e}")
            except Exception as e:
                 logging.error(f"Unexpected error saving JSON memory: {e}", exc_info=True)


    # --- Placeholder for SQLite Implementation ---
    # def _init_db(self):
    #     """Initializes the SQLite database and table if they don't exist."""
    #     with self._lock:
    #         try:
    #             conn = sqlite3.connect(self.memory_path, check_same_thread=False) # Allow access from multiple threads
    #             cursor = conn.cursor()
    #             cursor.execute('''
    #                 CREATE TABLE IF NOT EXISTS messages (
    #                     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     role TEXT NOT NULL,
    #                     content TEXT NOT NULL,
    #                     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    #                 )
    #             ''')
    #             conn.commit()
    #             conn.close()
    #             logging.debug("SQLite database initialized successfully.")
    #         except sqlite3.Error as e:
    #             logging.error(f"Error initializing SQLite database at {self.memory_path}: {e}")
    #             raise

    # def _load_db(self):
    #     """Loads history from the SQLite database."""
    #     with self._lock:
    #         try:
    #             conn = sqlite3.connect(self.memory_path, check_same_thread=False)
    #             cursor = conn.cursor()
    #             cursor.execute("SELECT role, content FROM messages ORDER BY timestamp ASC")
    #             self.history = [{'role': row[0], 'content': row[1]} for row in cursor.fetchall()]
    #             conn.close()
    #             logging.info(f"Loaded {len(self.history)} messages from SQLite: {self.memory_path}")
    #         except sqlite3.Error as e:
    #             logging.error(f"Error loading SQLite memory from {self.memory_path}: {e}. History reset.")
    #             self.history = []

    # def _save_db(self, role: str, content: str):
    #     """Saves a single message to the SQLite database."""
    #     # Note: This saves one message at a time. _save_json saves the whole list.
    #     with self._lock:
    #         try:
    #             conn = sqlite3.connect(self.memory_path, check_same_thread=False)
    #             cursor = conn.cursor()
    #             cursor.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))
    #             conn.commit()
    #             conn.close()
    #             logging.debug(f"Saved message (Role: {role}) to SQLite.")
    #         except sqlite3.Error as e:
    #             logging.error(f"Error saving message to SQLite: {e}")
    # -----------------------------------------

    def add_message(self, role: str, content: str):
        """
        Adds a message to the history and persists it.
        Args:
            role (str): The role of the message sender ('user', 'assistant', 'system', 'tool').
            content (str): The text content of the message.
        """
        if role not in ['user', 'assistant', 'system', 'tool']:
            logging.warning(f"Invalid role '{role}' provided for message. Check calling code.")
            # Decide how to handle: raise error, default role, or skip? Skipping for now.
            return

        message = {'role': role, 'content': content}

        with self._lock: # Lock during history modification and saving
            self.history.append(message)
            # Persist the change
            if self.memory_type == 'json':
                self._save_json()
            # elif self.memory_type == 'sqlite':
            #     self._save_db(role, content) # Save this specific message

        logging.debug(f"Added message to memory (Role: {role}, Length: {len(content)})")

    def get_history(self, limit: int = None) -> list:
        """
        Returns the conversation history.
        Args:
            limit (int, optional): If provided, returns only the last 'limit' messages. Defaults to None (all history).
        Returns:
            list: A list of message dictionaries. Returns a copy to prevent external modification.
        """
        with self._lock: # Ensure we read a consistent state
            if limit and limit > 0:
                # Return a copy of the relevant slice
                return list(self.history[-limit:])
            else:
                # Return a copy of the entire list
                return list(self.history)

    def clear_history(self):
        """Clears the chat history both in memory and in the persistent storage."""
        with self._lock: # Lock during clearing and saving
            self.history = []
            if self.memory_type == 'json':
                # Save the empty list to the file
                self._save_json()
            # elif self.memory_type == 'sqlite':
            #     try:
            #         conn = sqlite3.connect(self.memory_path, check_same_thread=False)
            #         cursor = conn.cursor()
            #         cursor.execute("DELETE FROM messages")
            #         conn.commit()
            #         conn.close()
            #         logging.info("Cleared SQLite memory table.")
            #     except sqlite3.Error as e:
            #         logging.error(f"Error clearing SQLite memory: {e}")

        logging.info("Chat memory cleared.")

