import hashlib
import os
import time 
import sys 
import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO, format='%(message)s')

directory = os.getenv('FILE_DIRECTORY', './')  
file_name = os.getenv('FILE_NAME', 'output.txt')  

file_path = os.path.join(directory, file_name)




while True: 
  current_datetime = datetime.now()
  datetime_str = str(current_datetime.strftime('%Y-%m-%d %H:%M.%S') )

  hash_object = hashlib.sha256(datetime_str.encode())
  hash_hex = hash_object.hexdigest()

  logging.info(f"Write {datetime_str} : {hash_hex} to {file_path}")
  if not os.path.exists(directory):
    logging.info(f"Directory '{directory}' does not exist. exit")
    sys.exit(1) 
  
  
  try:
     with open(file_path, 'a', buffering=1) as file:
      file.write(datetime_str + ' : ' + hash_hex + '\n')  # Write the text with a newline
      logging.debug(f"Text successfully written to {file_path}")
  except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


  time.sleep(5)