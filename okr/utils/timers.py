from datetime import datetime, timedelta, timezone

class Timers:

    @staticmethod
    def add_minutes_actual_time(minutes: int):
        return datetime.now(tz=timezone.utc) + timedelta(minutes=minutes)