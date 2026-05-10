import sqlite3
import click
from flask import g, current_app

DB_PATH = "db/reservations.db"
DB_SCHEMA = "db/schema.sql"

def create_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def get_db():
    if "db" not in g:
        g.db = create_connection()
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    connection = create_connection()
    with open(DB_SCHEMA, "r") as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

@click.command("init-db")
def init_db_command():
    """Wipe and recreate tables from schema.sql."""
    init_db()
    click.echo("Initialized the database.")

def register(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
