from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
conn=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)

cur=conn.connect(keyspace='suman')
sql="INSERT INTO peach(id,name,mobile) VALUES(%s,%s,%s)"
cur.execute(sql, [uuid.uuid1(),'AWS POSSIBLE','343434'])
print("SUCESS !!!")
cur.shutdown()

