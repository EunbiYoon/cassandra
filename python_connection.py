from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
cur=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)
session=cur.connect(keyspace='suman')

try:
    session
    print("SUCCESS : CASSANDRA DB CONNECTED")
except:
    print("ERROR : EITHER USERNAME / PASSWORD / KEYSPACE WRONG !!!" )
finally: #close connection
    cur.shutdown()