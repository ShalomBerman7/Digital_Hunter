

def validate_message(data):
    items = ['timestamp', 'signal_id', 'entity_id', 'reported_lat', 'reported_lon', 'signal_type', 'priority_level']
    for item in items:
        if item not in data or data[item] is None:
            return False
    return True