def categorize_access_events(events_list):
    zones = {}
    for user, zone, status in events_list:
        zones.setdefault(zone, []).append((user, status))
    return zones


def get_blocked_users(events_list):
    return {user for user, zone, status in events_list if status == 'DENIED'}


def get_last_access_logs(events_list, n=3):
    return events_list[-n:]


if __name__ == '__main__':
    test_events = [
        ('Ivanov', 'ServerRoom', 'ALLOWED'),
        ('Petrov', 'Lab-1', 'DENIED'),
        ('Sidorov', 'ServerRoom', 'DENIED'),
        ('Ivanov', 'Lab-1', 'ALLOWED'),
    ]
    
    print("[Автотест] События по зонам:", categorize_access_events(test_events))
    print("[Автотест] Заблокированные :", get_blocked_users(test_events))
    print("[Автотест] Последние 3     :", get_last_access_logs(test_events, 3))

