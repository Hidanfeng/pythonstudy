import logsetdict
from logging import config,getLogger

config.dictConfig(logsetdict.LOGGING_DIC)
logger1 = getLogger('xu')
logger1.info('这是一条日志')