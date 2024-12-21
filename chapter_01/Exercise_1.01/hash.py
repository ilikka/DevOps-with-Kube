import hashlib
import time 
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')


pseudo_random = datetime.now().strftime('%Y-%m-%d-%s-%H:%M')
hash_object = hashlib.sha256(pseudo_random.encode())
hash_hex = hash_object.hexdigest()

while True: 
  current_datetime = datetime.now()

  datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M.%S') )

  logging.info(f"{datetime_str} : {hash_hex}" )
  time.sleep(5)