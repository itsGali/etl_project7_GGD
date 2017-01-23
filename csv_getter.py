
#import csv
#import psycopg2
#import psycopg2.extras

#with open('etl_csv.csv', 'w+') as f:
    #writer = csv.writer(f, delimiter=',')
    #conn_2 = psycopg2.connect("dbname='etldb' user='' password=''")
    #cur_1 = conn_2.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur_2 = conn_2.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur_3 = conn_2.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur_2.execute('SELECT * from product_opinion INNER JOIN pros_cons ON product_opinion.product_review_id = pros_cons.product_review_id;')
    #cur_1.execute('SELECT * from product_info;')

    #for row1 in cur_1:
        #print(row1)
        #writer.writerow(row1)
    #for row2 in cur_2:
        #print(row2)
        #writer.writerow(row2)

#f.close()	
#print("Wykonano export do CSV z bazy ETL")
import csv
import json
import traceback
import psycopg2
import psycopg2.extras

with open("etl_csv.csv", "w") as f:
    writer = csv.writer(f, delimiter=',')
    conn_2 = psycopg2.connect("host='mgalant.ddns.net' port='5300' dbname='etldb' user='' password=''")
    cur_2 = conn_2.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur_2.execute('SELECT * from product_info INNER JOIN (SELECT * from product_opinion INNER JOIN pros_cons ON product_opinion.product_review_id = pros_cons.product_review_id) as a ON product_info.product_id = a.product_id;')
    for row2 in cur_2:
        #print(row2[4])
        writer.writerows([[row2]])
    conn_2.close()
    
    #query = """SELECT * from product_info INNER JOIN (SELECT * from product_opinion INNER JOIN pros_cons ON product_opinion.product_review_id = pros_cons.product_review_id) as a ON product_info.product_id = a.product_id"""
    #"""
    #conn = psycopg2.connect("host='mgalant.ddns.net' port='5300' dbname='etldb' user='' password=''")
    #cur = conn.cursor()

    #outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
    #with open('test.csv', 'w') as f:
        #cur.copy_expert(outputquery, f)
    #conn.close()
    #"""
print("Wykonano export do CSV z bazy ETL")
f.close()
