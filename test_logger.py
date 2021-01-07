from logger import set_logger

logger = set_logger(__name__)

def test():
    logger.info("＊＊＊＊＊＊＊＊infoメッセージ＊＊＊＊＊＊＊＊＊＊")
    logger.warning("＊＊＊＊＊＊＊＊warningメッセージ＊＊＊＊＊＊＊＊＊＊")
    logger.error("＊＊＊＊＊＊＊＊errorメッセージ＊＊＊＊＊＊＊＊＊＊")
    
if __name__ == "__main__":
    test()
