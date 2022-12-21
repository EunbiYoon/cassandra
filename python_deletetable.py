from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
conn=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)

cur=conn.connect(keyspace='suman')

id=uuid.UUID('2382885e-8174-11ed-b9fd-3c5282537df3')
sql="DELETE FROM peach WHERE id={0}".format(id)
cur.execute(sql)
print("FORMAT 1 SUCESS : DATA DELETED :-)")

cur.shutdown()