from alarm_clock import AlarmClock

def main():
    alarm_clock = AlarmClock()
    print(alarm_clock.current_time)
    alarm_clock.set_current_time()
    alarm_clock.set_is_alarm_enabled()

main()