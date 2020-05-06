import psycopg2

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


# makes a dict of all the profiles as key the have baud the same products. with as value the amount of same items baud
def createprofiddict(viewedproducts, user_id):
    prof_ids = {}
    for product in viewedproducts:
        for id in query("select profid from profiles_previously_viewed where prodid = '" + str(product[0]) +
                        "' and profid != '" + str(user_id) + "'"):
            if id[0] in prof_ids:
                prof_ids[id[0]] = prof_ids[id[0]] + 1
            else:
                prof_ids[id[0]] = 1
    return prof_ids


# gets the products for recommendations
def recommendation(user_id):
    userproducts = query("select prodid from profiles_previously_viewed where profid = '" + str(user_id) + "'")
    ids = createprofiddict(userproducts, user_id)
    recommendationnr = 0
    recommendations = []
    while recommendationnr < 5:
        count = 0
        for id, value in ids.items():
            if value > count:
                count = value
                prof = id
        recproducts = query("select prodid from profiles_previously_viewed where profid = '" + str(prof) + "' limit " +
                            str(5 - recommendationnr))
        del ids[prof]
        recommendationnr += len(recproducts)
        for item in recproducts:
            recommendations.append(item)
    return recommendations
