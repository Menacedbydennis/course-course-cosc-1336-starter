from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds

epoch_seconds = 3800
hours = get_hour(epoch_seconds)
minutes = get_minutes(epoch_seconds)
seconds = get_seconds(epoch_seconds)

print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")  # Output should be 01:03:20
