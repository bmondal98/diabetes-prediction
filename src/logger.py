'''
    for logging
'''

import logging
import os
import sys
from datetime import datetime
from src.constants import projectConstant
#from src.constants import projectConstant



LOG_FOLDER = f"{projectConstant.PROJECT_NAME}_LOGS"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M')}.log"
#f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(LOG_FOLDER)

os.makedirs(logs_path, exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    # filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(LOG_FILE_PATH),
                              logging.StreamHandler()]

)
