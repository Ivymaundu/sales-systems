import psycopg2
from flask import request,redirect
try:
    conn = psycopg2.connect(
        database="myduka_class", user='postgres', password='12345', host='127.0.0.1', port= '5432')
except:
    print('unable to connect to the database')

def get_data(my_data):
    cur = conn.cursor()
    t = "select * from "+my_data
    cur.execute(t)
    data = cur.fetchall()
    return data
prods=get_data('products')
sales=get_data('sales')

def add_product(values):
    cur = conn.cursor()
    insert_product="INSERT INTO products(name,buying_price,selling_price,stock_quantity) values(%s,%s,%s,%s)"
    cur.execute(insert_product,values)
    conn.commit()

def add_sale(values):
    cur=conn.cursor()
    insert_sale="INSERT INTO sales(pid,quantity,created_at) values(%s,%s,now())"
    cur.execute(insert_sale,values)
    conn.commit()



# def calc_profit():
#     cursor = conn.cursor()
#     m =" SELECT SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit,\
#     sales.created_at FROM sales JOIN products ON sales.pid = products.id  WHERE sales.created_at >=\
#     '2022-10-13 05:00:48'  AND sales.created_at <= '2023-10-05 20:33:31' GROUP BY sales.created_at\
#     ORDER BY sales.created_at ASC;"

#     cursor.execute(m)
#     data3=cursor.fetchall()
#     return data3
def calc_profit():
    cur=conn.cursor()
    find_profit="SELECT date(created_at) as days,sum((products.selling_price-products.buying_price)*sales.quantity) as profit from sales join products on products.id=sales.pid group by days order by days;"
    cur.execute(find_profit)
    profit_per_day=cur.fetchall()
    return profit_per_day



