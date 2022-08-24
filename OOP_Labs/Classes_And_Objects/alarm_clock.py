class AlarmClock:
    def __init__(self):
        self.current_time = '00:00'
        self.alarm_enabled = True
        self.alarm_time = '10:00'

    def set_current_time(self):
        new_time = input('Please enter a current time in 24-hour format: ')
        self.current_time = new_time
        print(f'The current time is: {self.current_time}')

    def set_is_alarm_enabled(self):
        new_enabled_status = input('Please enter True to turn the alarm on or False to turn it off: ')
        self.alarm_enabled = new_enabled_status

    def set_alarm_time(self):
        new_alarm_time = input('Please enter an alarm time in 24-hour format: ')
        self.alarm_time = new_alarm_time
        print(f'The alarm time is set for: {self.alarm_time}')