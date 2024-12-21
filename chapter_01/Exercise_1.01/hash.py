import hashlib
import time 
from datetime import datetime


while True: 
  current_datetime = datetime.now()

  datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M') )

  hash_object = hashlib.sha256(datetime_str.encode())
  hash_hex = hash_object.hexdigest()

  print(datetime_str, ":", hash_hex)
  time.sleep(5)