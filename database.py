import sqlite3
import json

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_NAME)
        self.create_tables()
        self.load_game_data()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                level INTEGER DEFAULT 1,
                xp INTEGER DEFAULT 0,
                hp INTEGER DEFAULT 100,
                max_hp INTEGER DEFAULT 100,
                stamina INTEGER DEFAULT 100,
                hunger INTEGER DEFAULT 100,
                thirst INTEGER DEFAULT 100,
                gold INTEGER DEFAULT 0,
                gems INTEGER DEFAULT 0,
                inventory TEXT DEFAULT '{}',
                pet TEXT DEFAULT '{}',
                guild_id TEXT DEFAULT NULL
            )
        ''')
        # Tambahkan tabel lain untuk guild, quests, dungeons, dll.
        self.conn.commit()

    def load_game_data(self):
        with open('data/items.json') as f:
            self.items = json.load(f)
        with open('data/monsters.json') as f:
            self.monsters = json.load(f)
        with open('data/recipes.json') as f:
            self.recipes = json.load(f)
