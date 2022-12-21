from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
conn=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)

cur=conn.connect(keyspace='suman')

def display_all():
    sql="SELECT * FROM peach"
    data=cur.execute(sql)
    for row in data:
        print(row.id, row.name, row.mobile)
print("DISPLAY ALL !")
display_all()

def display_by_id(id):
    id=uuid.UUID(id)
    sql="SELECT * FROM peach WHERE id={0}".format(id)
    data=cur.execute(sql)
    for row in data:
        print(row[0],row[1],row[2])
print("DISPLAY BY ID !")
display_by_id('90ed8cae-8174-11ed-b615-3c5282537df3')

cur.shutdown()

