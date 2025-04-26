
import sqlite3

def iniciar_banco():
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            categoria TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_transacao(tipo, valor, categoria, data):
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute('INSERT INTO transacoes (tipo, valor, categoria, data) VALUES (?, ?, ?, ?)',
              (tipo, valor, categoria, data))
    conn.commit()
    conn.close()

def obter_transacoes():
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transacoes')
    linhas = c.fetchall()
    conn.close()
    return linhas

def obter_transacoes_por_mes():
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute('''
        SELECT strftime('%Y-%m', data) as mes, tipo, sum(valor) as total
        FROM transacoes
        GROUP BY mes, tipo
    ''')
    linhas = c.fetchall()
    conn.close()
    return linhas

def obter_despesas_por_categoria():
    conn = sqlite3.connect('despesas.db')
    c = conn.cursor()
    c.execute('''
        SELECT categoria, sum(valor) as total
        FROM transacoes
        WHERE tipo = 'débito'
        GROUP BY categoria
    ''')
    linhas = c.fetchall()
    conn.close()
    return linhas
