import psycopg2
import random

conn = psycopg2.connect(
    database="spsql",
    user="postgres",
    password="De3broers",
    host="localhost",
    port="5432"
)


# sends query to the database
def query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    return records


# creates a list of the attributes a product should have
def querywherelist(attributes):
    attributes = list(attributes[0])
    lst = [' targetaudience = ', ' and subsubcategory = ', ' and brand = ', ' and type = ']
    count = 0
    for attribute in attributes:
        attribute = lst[count] + "'" + attribute + "'"
        attributes[count] = attribute
        count += 1
    return attributes


# gets the products for recommendations
def recommendation(product_id):
    wherelst = querywherelist(query("select targetaudience, subsubcategory, brand, "
                                    "type from products where id = '" + str(product_id) + "'"))
    recommendations = []
    while len(recommendations) < 5:
        prods = query("select id from products where " + ''.join(wherelst) + " and id != '" +
                      str(product_id) + "' limit " + str(5 - len(recommendations)))
        for item in prods:
            recommendations.append(item)
        wherelst.pop()
    return recommendations
