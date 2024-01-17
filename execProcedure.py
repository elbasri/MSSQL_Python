import sys
import pyodbc
import conf

def execute_procedure(cursor, procedure_name, *parameters):
    sql_command = f"EXEC {procedure_name}"
    if parameters:
        params = ', '.join(f"'{param}'" for param in parameters)
        sql_command += f" {params}"

    cursor.execute(sql_command)

    more_results = True
    while more_results:
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        more_results = cursor.nextset()

def main():
    try:
        with pyodbc.connect(conf.conn_str) as conn:
            print("تم الاتصال بالمخدم بنجاح")
            cursor = conn.cursor()

            while True:
                procedure_name = input("أدخل اسم الإجراء المُخزن (أو اكتب "خروج" للخروج): ")
                if procedure_name.lower() == 'خروج':
                    break

                parameters = input("أدخل المعلمات مفصولة بمسافات (إن وجدت): ").split()

                execute_procedure(cursor, procedure_name, *parameters)

    except pyodbc.خطأ as e:
        print("خطأ استعلام: ", e)
    except Exception as e:
        print("خطأ: ", e)

if __name__ == "__main__":
    main()
