import pyodbc
import conf

def delete_trigger(conn, trigger_name):
    cursor = conn.cursor()
    
    cursor.execute(f"IF OBJECT_ID(N'{trigger_name}', 'TR') IS NOT NULL DROP TRIGGER {trigger_name};")
    conn.commit()
    print(f"Trigger '{trigger_name}' deleted successfully.")

try:
    with pyodbc.connect(conf.conn_str) as conn:
        print("تم الاتصال بالمخدم بنجاح")

        trigger_name = "trg_AuditUpdateEmploye"

        delete_trigger(conn, trigger_name)

        print("تم حذف المشغل بنجاح.")

except Exception as e:
    print("خطأ: ", e)
