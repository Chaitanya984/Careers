
import pymysql
import os
from dotenv import load_dotenv
dotenv_path = '.env'
load_dotenv(dotenv_path)

data = os.environ.get("db")
ht = os.environ.get("host")
pt = os.environ.get("port")
pwd = os.environ.get("password")
ur = os.environ.get("user")
cset = os.environ.get("charset")

timeout = 10
connection = pymysql.connect(
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db=data,
  host=ht,
  password=pwd,
  port=21911,
  user=ur,
  charset=cset,
  write_timeout=timeout,
  read_timeout=timeout,

)

# try:
#   cursor = connection.cursor()
#   # cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
#   cursor.execute(("SELECT * FROM jobs"))
#   all = cursor.fetchall()
#   first = all[0]
#   print(type(first))
      
# finally:
#   connection.close()


def load_jobs_from_db():
      # cursor = self.connection.cursor()          

      # # cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
      # # cursor.execute(("SELECT * FROM jobs"))
      # self.connection.ping() 
      # with self.connection.cursor() as cursor:         
        # cursor.execute("SELECT * FROM jobs")
    # try:
    #     with connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute("SELECT * FROM jobs")
    #             jobs = cursor.fetchall()
    #             print(jobs)
    # finally:
    #     connection.close()
    # return jobs
      cursor = connection.cursor()
      # cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
      cursor.execute(("SELECT * FROM jobs"))
      all = cursor.fetchall()
      first = all[0]
      print(type(first))
      return all


jobs = load_jobs_from_db()