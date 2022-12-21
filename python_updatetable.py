from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials=PlainTextAuthProvider(username='superapple',password='fact@123')
conn=Cluster(['127.0.0.1'],port=9042,auth_provider=user_credentials)

try:
    cur=conn.connect(keyspace='suman')
    id='a75ad251-8174-11ed-a4dc-3c5282537df3'
    changed_id=uuid.UUID(id)
    sql="UPDATE peach SET name=%s Where id=%s"
    cur.execute(sql,("FLASK APPLICATION",changed_id))
    print("SUCESS : DATA UPDATED")
    print("Target ID TYPE")
    print(type(id))
    print("Changed ID TYPE")
    print(type(changed_id))
except:
    print("ERROR : Something went wrong :-(")
finally:
    cur.shutdown()



