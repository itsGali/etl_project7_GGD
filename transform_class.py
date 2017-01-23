#/usr/bin/python2.7
import json
import traceback
import psycopg2
from ast import literal_eval

# cur.execute("""CREATE TABLE product_info(product_id integer PRIMARY KEY, producer varchar, model varchar, category varchar, extra_info varchar, review varchar, reviews_count varchar);""")
# cur.execute("""CREATE TABLE product_opinion(product_review_id integer PRIMARY KEY, product_id integer, product_reviewer varchar, product_reviewers_score varchar, product_review_summary varchar, product_review_time varchar(albo datetime), product_review_body varchar, product_review_helpful integer, product_review_unhelpful integer);""")
# cur_3.execute("""CREATE TABLE pros_cons(product_review_id integer PRIMARY KEY, pros varchar, cons varchar);""")
# cur.execute("""SELECT * FROM product_info;""")
#conn_2 = psycopg2.connect("dbname='testetl' user='' password=''")
with open('product_info.json', 'r') as pi:
    jl = json.loads(pi.read(),encoding='utf-8')
    jl_str = json.dumps(jl)
    product_info = literal_eval(jl_str)
    sql_product_info = "INSERT INTO product_info (" + ", ".join(product_info.keys()) + ") VALUES (" + ", ".join(["%("+k+")s" for k in product_info]) + ");"
    try:
        conn_1 = psycopg2.connect("dbname='etldb' user='' password=''")
        cur_1 = conn_1.cursor()
        try:
            cur_1.execute("select exists(select product_id from product_info where product_id=%s)", (product_info['product_id'],))
            if (cur_1.fetchone()[0])== True:
                sys.exit(0)
            cur_1.execute(sql_product_info, product_info)
            conn_1.commit()
        except psycopg2.Error as d:
            print(str(d))
    except psycopg2.Error as e:
        #print("I am unable to connect to the database")
        print("juz istnieje")
        #print(e.pgcode)
        #print(e.pgerror)
        #print(traceback.format_exc())

with open('product_opinion.json', 'r') as po:
    jlo = json.loads(po.read(),encoding='utf-8')
    jlop_str = json.dumps(jlo)
    product_opinion = literal_eval(jlop_str)
    sql_product_opinion = ""
    product_opinion_sql = {}
    try:
        conn_2 = psycopg2.connect("dbname='etldb' user='' password=''")
        cur_2 = conn_2.cursor()
        for l in product_opinion[product_info['product_id']]:
            product_opinion_sql ={'product_review_id' : l, 'product_id': (product_info['product_id']), 'product_reviewer': product_opinion[product_info['product_id']][l][0], 'product_reviewers_score': product_opinion[product_info['product_id']][l][1], 'product_review_summary': product_opinion[product_info['product_id']][l][2], 'product_review_time': product_opinion[product_info['product_id']][l][3], 'product_review_body': product_opinion[product_info['product_id']][l][4], 'product_review_helpful': product_opinion[product_info['product_id']][l][5], 'product_review_unhelpful': product_opinion[product_info['product_id']][l][6]}
            # print(product_opinion_sql)
            sql_product_opinion = "INSERT INTO product_opinion(" + ", ".join(product_opinion_sql.keys()) + ") VALUES (" + ", ".join(["%("+k+")s" for k in product_opinion_sql]) + ");"
            try:
                cur_2.execute(sql_product_opinion, product_opinion_sql)
                conn_2.commit()
            except psycopg2.Error as e:
                print(str(e))
    except psycopg2.Error as e:
        #print("I am unable to connect to the database")
        print("juz istnieje ten rekord w bazie")
        #print(e.pgcode)
        #print(e.pgerror)
        #print(traceback.format_exc())

with open('product_opinion_pros_cons.json', 'r') as popc:
    jlpopc = json.loads(popc.read(),encoding='utf-8')
    jlpopc_str = json.dumps(jlpopc)
    product_opinion_pros_cons = literal_eval(jlpopc_str)

    try:
        conn_3 = psycopg2.connect("dbname='etldb' user='' password=''")
        cur_3 = conn_3.cursor()

        for ky in product_opinion_pros_cons.keys():
            product_opinion_pros_cons_sql = {'product_review_id': ky, 'pros': product_opinion_pros_cons[ky]['zalety'], 'cons': product_opinion_pros_cons[ky]['wady']}
            sql_product_opinion_pros_cons = "INSERT INTO pros_cons (" + ", ".join(product_opinion_pros_cons_sql.keys()) + ") VALUES (" + ", ".join(["%(" + k + ")s" for k in product_opinion_pros_cons_sql]) + ");"
            try:
                cur_3.execute(sql_product_opinion_pros_cons, product_opinion_pros_cons_sql)
                conn_3.commit()
            except psycopg2.Error as d:
                print(str(d))
    except psycopg2.Error as e:
        #print("I am unable to connect to the database")
        print("juz istnieje ten rekord w bazie")
        #print(e.pgcode)
        #print(e.pgerror)
        print(traceback.format_exc())
print("Zaladowano do bazy")
