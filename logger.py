import os
import logging 
from datetime import datetime

LOG_FORMAT='%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s'
LOG_DIR_NAME='logs'

def set_logger(name):
    logger= logging.getLogger(name)
    
    # LOGフォルダがない場合は作成
    if not os.path.exists(LOG_DIR_NAME):
        os.mkdir(LOG_DIR_NAME)
    
    # ログの設定
    now_time = datetime.now()
    formatter = logging.Formatter(LOG_FORMAT)
    fh = logging.FileHandler(filename=f'{LOG_DIR_NAME}/{now_time:log_%Y%m%d}.log',encoding="utf-8")
    fh.setFormatter(formatter)
    fh.setLevel=logging.INFO

    logger.addHandler(fh)

    return logger
