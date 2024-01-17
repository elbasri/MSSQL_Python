import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("تم الاتصال بالمخدم")
        
        cursor = conn.cursor()

        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
        """
        cursor.execute(query)

        tables = cursor.fetchall()

        print("قائمة الجداول في قاعدة البيانات:")
        for table in tables:
            print(table[0])

except Exception as e:
    print("خطأ: ", e)
