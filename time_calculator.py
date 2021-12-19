def add_time(start, duration, starting_day="None"):
    hour, min1 = start.split(":")
    min, zone = min1.split(" ")
    duration_hour, duration_minutes = duration.split(":")

    # Add minutes first
    hours, minutes = add_minutes(int(min), int(duration_minutes))

    # Add hours then
    final_hour, zone, days = add_hours(int(hour), int(duration_hour) + hours, zone)

    # Change Days
    if starting_day != "None":
        ending_day = next_day(starting_day, days)
        if days == 0:
            answer = "Returns: " + str(final_hour) + ":" + str(minutes) + " " + str(
                zone) + " " + ending_day + "(next day)"
        else: answer = "Returns: " + str(final_hour) + ":" + str(minutes) + " " + str(zone) + " " + ending_day + " (" + str(days) + " days later)"
    else: answer = "Returns: " + str(final_hour) + ":" + str(minutes) + " " + str(zone)


    return print(answer)


def next_day(starting_day, days):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    end_day_pos = week.index(starting_day) + days
    if end_day_pos > 6:
        end_day_pos = end_day_pos % 7
    end_day = week[end_day_pos]
    return end_day


def add_hours(start, duration, zone, day=None):
    # Wechsel Zeitzone wenn Modulo 1 --> Modulo /
    count_zone = duration // 12 % 2
    count_days = duration // 24
    sum = start + (duration % 12)

    # Add hours
    if sum < 12:
        pass
    else:
        sum = sum - 12
        count_zone = count_zone + 1
        if sum == 0:
            sum = 12

    # Change time zone
    if count_zone == 1:
        if zone == "PM":
            zone = "AM"
            count_days = count_days + 1
        else:
            zone = "PM"
    return sum, zone, count_days


def add_minutes(start, duration):
    hours = (start + duration) // 60
    minutes = (start + duration) % 60
    single_minutes = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if minutes < 10:
        minutes = single_minutes[minutes]
    return hours, minutes
