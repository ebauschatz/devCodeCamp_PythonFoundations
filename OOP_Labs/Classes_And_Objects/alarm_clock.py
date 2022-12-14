"""Class file for alarm clocks

An alarm clock can be used to display the current time or optionally sound an alarm 
at a specific time.
"""

class AlarmClock:
    """Representation of an alarm clock

    Instance Variables:
        current_time:
            string in 24-hour time representing the current time displayed on the clock
        alarm_enabled:
            bool representing if the alarm will sound or not at the alarm_time
        alarm_time:
            string in 24- hour time representing the time the alarm is set for

    Public Methods:
        set_current_time:
            Sets a new value for current_time and displays the time to the console
        set_is_alarm_enabled:
            Sets a new value for the alarm being turned on or not
        set_alarm_time:
            Sets a new value for the alarm_time and displays the time to the console
    """
    def __init__(self):
        """Initializes a customer
        
        Instance Variables:
            current_time:
                string in 24-hour time representing the current time displayed on the clock
            alarm_enabled:
                bool representing if the alarm will sound or not at the alarm_time
            alarm_time:
                string in 24- hour time representing the time the alarm is set for
        """
        self.current_time = '00:00'
        self.alarm_enabled = True
        self.alarm_time = '10:00'

    def set_current_time(self):
        """Sets a new value for current_time baesd on user input and displays the time to the console
        
        Effects:
            The current_time string is updated to the new value
        """
        new_time = input('Please enter a current time in 24-hour format: ')
        self.current_time = new_time
        print(f'The current time is: {self.current_time}')

    def set_is_alarm_enabled(self):
        """Sets a new value for the alarm being turned on or not based on user input
        
        Effects:
            The alarm_enabled bool is updated to the new value
        """
        new_enabled_status = input('Please enter True to turn the alarm on or False to turn it off: ')
        self.alarm_enabled = new_enabled_status

    def set_alarm_time(self):
        """Sets a new value for the alarm_time based on user input and displays the time to the console
        
        Effects:
            The alarm_time string is updated to the new value
        """
        new_alarm_time = input('Please enter an alarm time in 24-hour format: ')
        self.alarm_time = new_alarm_time
        print(f'The alarm time is set for: {self.alarm_time}')