def add_time(start, duration, starting_day=None):

    start = start.strip()
    start_time, period = start.rsplit(' ', 1)
    start_hour_str, start_min_str = start_time.split(':')
    start_hour = int(start_hour_str)
    start_min = int(start_min_str)
    period = period.upper()

    dur_hour_str, dur_min_str = duration.split(':')
    dur_hour = int(dur_hour_str)
    dur_min = int(dur_min_str)

    # Convert start time to 24-hour format
    if period == 'PM' and start_hour != 12:
        start_hour_24 = start_hour + 12
    elif period == 'AM' and start_hour == 12:
        start_hour_24 = 0
    else:
        start_hour_24 = start_hour

    # Total minutes from start and duration
    start_total_min = start_hour_24 * 60 + start_min
    dur_total_min = dur_hour * 60 + dur_min
    total_min = start_total_min + dur_total_min

    # Calculate days and remaining time
    min_per_day = 24 * 60
    days_passed = total_min // min_per_day
    remaining_min = total_min % min_per_day

    # Convert remaining minutes back to 12-hour time
    new_hour_24 = remaining_min // 60
    new_min = remaining_min % 60
    new_period = 'AM' if new_hour_24 < 12 else 'PM'
    new_hour_12 = new_hour_24 % 12
    if new_hour_12 == 0:
        new_hour_12 = 12

    # Time string
    time_part = f"{new_hour_12}:{new_min:02d} {new_period}"

    # Optional day calculation
    day_part = ""
    if starting_day:
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        start_idx = days.index(starting_day.strip().lower())
        new_idx = (start_idx + days_passed) % 7
        day_part = f", {days[new_idx].capitalize()}"

    # Add info about how many days later
    if days_passed == 1:
        day_part += " (next day)"
    elif days_passed > 1:
        day_part += f" ({days_passed} days later)"

    # Combine and return
    new_time = time_part + day_part
    return new_time


# Example test
print(add_time('11:23 AM', '10:43', 'thursday'))
