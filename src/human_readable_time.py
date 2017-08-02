"""Translates seconds to a string of time from a proper context."""
from math import floor


def format_duration(seconds):
    """Output a human readable time converted from seconds."""
    if seconds == 0:
        return 'now'
    time = []
    years = floor(seconds/60/60/24/365)
    if years >= 1:
        seconds = seconds - years * 60 * 60 * 24 * 365
        if years > 1:
            time.append(str(int(years)) + ' years')
        else:
            time.append(str(int(years)) + ' year')
    days = floor(seconds/60/60/24)
    if days >= 1:
        seconds = seconds - days * 60 * 60 * 24
        if days > 1:
            time.append(str(int(days)) + ' days')
        else:
            time.append(str(int(days)) + ' day')
    hours = floor(seconds/60/60)
    if hours >= 1:
        seconds = seconds - hours * 60 * 60
        if hours > 1:
            time.append(str(int(hours)) + ' hours')
        else:
            time.append(str(int(hours)) + ' hour')
    minutes = floor(seconds/60)
    if minutes >= 1:
        seconds = seconds - minutes * 60
        if minutes > 1:
            time.append(str(int(minutes)) + ' minutes')
        else:
            time.append(str(int(minutes)) + ' minute')
    if seconds >= 1:
        if seconds > 1:
            time.append(str(int(seconds)) + ' seconds')
        else:
            time.append(str(int(seconds)) + ' second')
    if len(time) > 2:
        time = ', |'.join(time)
        time = time.split('|')
        time[len(time)-2] = time[len(time)-2][:-2]
    if len(time) > 1:
        time.insert(len(time)-1, ' and ')
    return ''.join(time)
