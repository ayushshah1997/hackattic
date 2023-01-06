import base64
from base import Problem
import psycopg2
import gzip

p = Problem(name='backup_restore')
cmds = gzip.decompress(base64.b64decode(p.get_question()['dump']))
rows = str(cmds).split('\\n')[95:165]
ssn = []
for r in rows:
    if r.__contains__("alive"):
        ssn.append(r.split("\\t")[3])
# f = open("backup.txt", "wb")
# f.write(cmds)

# f.close()
#     # Connect to the database
#     conn = psycopg2.connect(host='localhost', port=5432, dbname='postgres', user='postgres', password='postgres')
#
#     # Create a cursor
#     cur = conn.cursor()
#
#     # Execute the SQL commands
#
#     cur.execute(sql)
#
#     # Commit the changes
#     conn.commit()
#
#     # Close the cursor and connection
#     cur.close()
#     conn.close()

p.send_answer({"alive_ssns": ssn})
