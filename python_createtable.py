from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
conn=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)

sql="CREATE TABLE IF NOT EXISTS peach(id UUID PRIMARY KEY, name TEXT, mobile TEXT)"
cur=conn.connect(keyspace='suman')
cur.execute(sql)
print("table created!")
cur.shutdown()
