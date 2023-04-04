import logging
logging.basicConfig(
	level=logging.CRITICAL,
	format="{asctime} {levelname:<8} {message}",
	style="{",
	filename='%slog' % __file__[:-2],
	filemode='w'
)
	

logging.debug("This is a debug msg")
logging.info("This is a info msg")
logging.warning("This is a warning msg")
logging.error("This is a error msg")
logging.critical("This is a critical msg")

a = 2
b = 0
try:
	prod = a/b

except Exception as e:
	logging.critical("Exception occurred: ", exc_info=True)

