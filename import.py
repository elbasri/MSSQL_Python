import pyodbc
import conf
import os

conn_str = conf.conn_str

try:
    #with pyodbc.connect(conn_str, autocommit=True) as conn:
    #    print("تم الاتصال بالمخدم بنجاح")
    #    conn.execute("CREATE DATABASE AsfarMaghrib;")
    #    print("القاعدة 'AsfarMaghrib' أنشئت بنجاح")

    with pyodbc.connect(conn_str + ";DATABASE=AsfarMaghrib", autocommit=True) as conn:
        
        script_path = os.path.join(os.path.dirname(__file__), '..', 'SchemaInitiale.sql')

        with open(script_path, 'r') as file:
            create_tables_script = file.read()

        conn.execute(create_tables_script)
        print("تم إنشاء الجداول بنجاح في 'AsfarMaghrib'")

except Exception as e:
    print("خطأ: ", e)
