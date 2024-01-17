import pyodbc
import conf

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("تم الاتصال بالمخدم")
        
        cursor = conn.cursor()

        query = """
        SELECT table_name
        FROM information_schema.views
        """
        cursor.execute(query)

        views = cursor.fetchall()

        print("قائمة المشاهدات في قاعدة البيانات:")
        for view in views:
            print(view[0])

except Exception as e:
    print("خطأ: ", e)
