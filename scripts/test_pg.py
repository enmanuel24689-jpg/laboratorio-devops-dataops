import psycopg

try:
    conn = psycopg.connect(
        "host=127.0.0.1 port=5432 dbname=laboratorio user=admin password=admin123"
    )

    print("CONEXION EXITOSA")

    cur = conn.cursor()
    cur.execute("SELECT version();")

    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print("Conexion fallida:")
    print(e)