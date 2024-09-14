import mysql.connector

def read_sales_order(sqlstr):
    sqlstr = str(sqlstr).replace("```","").replace("sql","")
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="",
        database="example"
    )
    
    cursor  = mydb.cursor()
    cursor.execute(sqlstr)
    result = cursor.fetchall()
    mydb.commit()
    mydb.close()
    return result