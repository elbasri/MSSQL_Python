import pyodbc
import conf

def main():
    try:
        with pyodbc.connect(conf.conn_str) as conn:
            print("تم الاتصال بالمخدم بنجاح.")
            cursor = conn.cursor()

            while True:
                # مطالبة المستخدم بالإدخال لإنشاء الإجراء المُخزن
                print("\nأدخل عبارات الاستعلام (سكيول) للإجراء المُخزن الخاص بك. اكتب "دوز" للإنهاء، أو اكتب "إنهاء" للإنهاء:")
                user_input_lines = []
                while True:
                    line = input()
                    if line.lower() == 'دوز':
                        break
                    elif line.lower() == 'إنهاء':
                        return
                    user_input_lines.append(line)

                create_procedure_sql = '\n'.join(user_input_lines)

                if create_procedure_sql.strip():
                    print("إنشاء الإجراء المُخزن...")
                    cursor.execute(create_procedure_sql)
                    conn.commit()
                    print("تم إنشاء الإجراء المُخزن بنجاح.")

    except pyodbc.خطأ as e:
        print("خطأ استعلامات: ", e)
    except Exception as e:
        print("خطأ: ", e)

if __name__ == "__main__":
    main()
