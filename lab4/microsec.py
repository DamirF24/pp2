from datetime import datetime

# Get current datetime
current_datetime = datetime.now()

# Drop microseconds
current_datetime_no_microseconds = current_datetime.replace(microsecond=0)

# Print the result
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", current_datetime_no_microseconds)
