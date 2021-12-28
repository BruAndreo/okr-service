import time
from datetime import datetime, timedelta, timezone

class Timers:

    @staticmethod
    def add_minutes_actual_time(minutes: int) -> int:
        dt = datetime.now(tz=timezone.utc) + timedelta(minutes=minutes)
        return time.mktime(dt.timetuple())