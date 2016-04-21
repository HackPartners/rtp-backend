import os
from playhouse.db_url import connect
import sys

db_user = os.getenv("RTP_DBUSER", "hackpartner")
db_pass = os.getenv("RTP_DBPASS", "password")
db_name = os.getenv("RTP_DBNAME", "rtp_db")
db_host = os.getenv("RTP_DBHOST", "localhost")
db_port = os.getenv("RTP_DBPORT", "5432")

db_url = ("postgresql" + "://" + db_user + ":" + db_pass + "@" + db_host + ":" + db_port + "/" + db_name)

db = connect(db_url)
