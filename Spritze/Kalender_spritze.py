import arrow
from datetime import timedelta, datetime
from icalendar import Calendar, Event, Alarm
import pytz


c = Calendar()

time = time = datetime(2021, 8, 31, hour=10, minute=0,
                       tzinfo=pytz.timezone("Europe/Berlin"))
for i in range(10):

    e = Event()
    e.add('summary', "Spritze")
    e.add('location', "Dr.Bartnitzky")

    e.add('dtstart', time)

    first_alarm = Alarm()
    second_alarm = Alarm()
    first_alarm.add('trigger', timedelta(days=-2))
    second_alarm.add('trigger', timedelta(hours=-1))

    e.add_component(first_alarm)
    e.add_component(second_alarm)
    c.add_component(e)
    time += timedelta(days=25)
    if time.weekday() == 5:
        time += timedelta(days=-1)
    elif time.weekday() == 6:
        time += timedelta(days=+1)


with open("Spritze.ics", "wb") as f:
    f.write(c.to_ical())