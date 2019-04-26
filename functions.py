import json

def upper_lower_check(topic, message, section, srv):
    """perform a range check on a value in the json formatted
    message. controls live in the configuration file. for example,
    a control section set up as:

        [temperature/somewhere]
        topic = sensor/somewhere
        targets = slack:environment
        format = Somewhere trouble with temperature {temperature}C
        check = temperature
        lower = 18
        upper = 24
        filter = upper_lower_check()

    when a message is received as:

        {"temperature": "19.0", "humidity": "73.0"}

    will not send a message to slack but a message as:

        {"temperature": "25.0", "humidity": "73.0"}

    will send "Somewhere trouble with temperature 25.0" to the
    configured slack channel.
    """
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
