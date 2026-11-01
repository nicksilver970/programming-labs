import sys
from variant14_mod import (
    categorize_access_events,
    get_blocked_users,
    get_last_access_logs,
)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    events = [
        ('Ivanov', 'ServerRoom', 'ALLOWED'),
        ('Petrov', 'Lab-1', 'DENIED'),
        ('Sidorov', 'ServerRoom', 'DENIED'),
        ('Ivanov', 'Lab-1', 'ALLOWED'),
        ('Kuznetsov', 'ServerRoom', 'ALLOWED'),
        ('Petrov', 'ServerRoom', 'DENIED'),
    ]

    zones_dict = categorize_access_events(events)
    blocked = get_blocked_users(events)
    last_logs = get_last_access_logs(events, n)

    print("=== СКУД УМНОГО ЗДАНИЯ (BMS) ===")
    print(f"Всего событий в журнале: {len(events)}")

    print("\nСобытия, сгруппированные по зонам:")
    for zone, records in zones_dict.items():
        print(f"  {zone}:")
        for user, status in records:
            print(f"     - {user:<12} : {status}")

    print(f"\nНарушители доступа (set): {blocked}")
    print(f"Свежие проходы (срез [-{n}:]): {last_logs}")


if __name__ == '__main__':
    main()
