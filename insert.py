import psycopg2
try:
    conn = psycopg2.connect(
        database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
except:
    print('unable to connect to the database')

   

def insert_records_into_table(table_name,values):
    cursor=conn.cursor
    task = f"INSERT INTO {table_name}(name,buying_price,selling_price,stock_quantity) VALUES('%',%,%,%)"
    
    values=('spaghetti',150,250,50)
    cursor.execute(task,values)
    conn.commit()

new_record=insert_records_into_table('table_name','values')
print('records inserted succesfully')
conn.close

def insert_records_into_table(table_name,values):
    cursor=conn.cursor
    task = f"INSERT INTO {table_name}(pid,quantity,created_at) VALUES(%,%,%,%)"
    new_record=values
    cursor.execute(task,new_record)
    conn.commit()


print('records inserted succesfully')
conn.close

    
