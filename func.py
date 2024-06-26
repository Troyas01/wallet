"""
Тут мы описываем неск. функций для работы с базой данных
"""

import sqlite3
from one import connection_bd


def add_transaction(date, description, amount):
    connection_bd("my_wallet.db",
                  """
                  INSERT INTO my_wallet (date, description, amount)
                  VALUES (?, ?, ?)
                  """, (date, description, amount)
                  )

def get_total_amount():
    conn = sqlite3.connect('my_wallet.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT SUM(amount) FROM my_wallet
    ''')

    total = cursor.fetchone()[0]
    conn.close()

    return total if total is not None else 0.0

def del_transaction(transaction_id):
    connection_bd("my_wallet.db",
                  """
                  DELETE FROM my_wallet WHERE id = ?
                  """, (transaction_id,))

def show_transaction():
    conn = sqlite3.connect("my_wallet.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM my_wallet
    """)

    my_wallet = cursor.fetchall()
    conn.close()

    return my_wallet
