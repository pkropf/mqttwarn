import json

def upper_lower_check(topic, message, section, srv):
    #srv.logging.debug(f"topic: {topic}")
    #srv.logging.debug(f"message: {message}")
    #srv.logging.debug(f"section: {section}")
    #srv.logging.debug(f"mwcore: {srv.mwcore.keys()}")

    check = srv.mwcore["cf"].get(section, 'check')
    #srv.logging.debug(f"check: {check}")
    upper = srv.mwcore["cf"].getint(section, 'upper')
    #srv.logging.debug(f"upper: {upper}")
    lower = srv.mwcore["cf"].getint(section, 'lower')
    #srv.logging.debug(f"lower: {lower}")

    value = int(float((json.loads(message)[check])))
    if value < lower:
        return False
    if value > upper:
        return False

    return True
