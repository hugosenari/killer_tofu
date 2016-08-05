import muffin

killer_tofu = muffin.Application('killer_tofu')

def result(content={}, msgs=[], status=200):
    return {
        "status": status,
        "msgs": msgs,
        "content": content
    }

def collection():
    return killer_tofu.ps.motor.killer_tofu
