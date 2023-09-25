import psycopg2
try:
    conn = psycopg2.connect(
        database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
except:
    print('unable to connect to the database')

# def get_data(my_data):
#     cur = conn.cursor()
#     t = "select * from "+my_data
#     cur.execute(t)
#     data = cur.fetchall()
#     return data
# prods=get_data('products')
# sales=get_data('sales')
# print(prods)
# print(sales)


def insert_records():
    cur = conn.cursor()

        # Execute the INSERT statement
    cur.execute("INSERT INTO products (name, buying_price,selling_price,stock_quantity) VALUES (%s, %s,%s,%s)", ("yoghurt", 20,50,10))
    conn.commit()
    cur.close()
    conn.close()

    print("Data inserted successfully!")  
   

total=insert_records()
print(total)
conn.close()

#     cur=conn.cursor 
#     new_record= f"INSERT INTO products {table_name} VALUES (%,%,%,%)"
#     record_data=values
#     cur.execute(new_record,record_data)
#     data=all()
#     return data

# new_record=insert_records('products',"'downy',10,50,30")
# print(new_record)

