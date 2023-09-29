
import psycopg2
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
print(prods)
# print(sales)


def remaining_stock():
    stock = [] 
    cur = conn.cursor()
    
    cur.execute(f'SELECT * FROM rem_stock')
    rem_stocks = cur.fetchall()

    for rem_stock in rem_stocks:
        product = {}  # Create a new dictionary for each product
        product['name'] = rem_stock[1]
        product['rem_stock'] = rem_stock[2]
        stock.append(product)

    return stock

s = remaining_stock()
# the output is a list of dictionaries
print(s)

conn.close()
