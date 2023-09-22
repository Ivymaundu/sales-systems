import psycopg2
def get_data(my_data):
    conn = psycopg2.connect(
    database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
    t = "select * from "+my_data
    cursor.execute(t)
    data = cursor.fetchall()
    conn.close()
    return data

prods=get_data('products')
sales=get_data('sales')
print(prods)
print(sales)