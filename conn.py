import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("تم الاتصال بمخدم قواعد البيانات")
        
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
        print("نسخة المخدم:", row[0])

except Exception as e:
    print("خطأ: ", e)
