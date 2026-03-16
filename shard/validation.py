def validate_intel(data):
    items_intel = ['timestamp', 'signal_id', 'entity_id', 'reported_lat', 'reported_lon', 'signal_type', 'priority_level']
    for item in items_intel:
        if item not in data or data[item] is None:
            return False
    return True


def validate_damage(data):
    items_damage = ['timestamp', 'attack_id', 'entity_id', 'weapon_type']
    for item in items_damage:
        if item not in data or data[item] is None:
            return False
    return True


def validate_attack(data):
    items_attack = ['timestamp', 'signal_id', 'entity_id', 'priority_level']
    for item in items_attack:
        if item not in data or data[item] is None:
            return False
    return True
