import pyodbc
import conf

def create_views(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE VIEW chauffeur AS
    SELECT 
        E.IdEmploye, 
        E.Nom, 
        E.Prenom, 
        E.Nationalite, 
        E.CarteIdentite, 
        E.Phone, 
        E.Etat, 
        C.NomLigne_id
    FROM 
        webapp_employe AS E
    JOIN 
        webapp_conduit AS C ON E.IdEmploye = C.IdEmploye_id
    """)

    cursor.execute("""
    CREATE VIEW agentGuichet AS
    SELECT 
        E.IdEmploye, 
        E.Nom, 
        E.Prenom, 
        E.Nationalite, 
        E.CarteIdentite, 
        E.Phone, 
        E.Etat, 
        V.NumeroTicket_id
    FROM 
        webapp_employe AS E
    JOIN 
        webapp_vend AS V ON E.IdEmploye = V.IdEmploye_id
    """)

    conn.commit()

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("تم الاتصال بنجاح")

        create_views(conn)

        print("تم الإنشاء بنجاح.")

except Exception as e:
    print("خطأ: ", e)
