
def parse_data(data):
    try:
        parts = data.split(',')
        telemetry = {
            "Altitude": parts[0],
            "Temperature": parts[1],
            "Battery": parts[2]
        }
        return telemetry
    except:
        return None
