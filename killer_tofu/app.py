import muffin
import logging

killer_tofu = muffin.Application('killer_tofu')

logger = logging.getLogger('killer_tofu')
logger.info('Killer Toffu Started')

def result(content={}, msgs=[], status=200):
    return {
        "status": status,
        "msgs": msgs,
        "content": content
    }

def collection():
    return killer_tofu.ps.motor.killer_tofu
