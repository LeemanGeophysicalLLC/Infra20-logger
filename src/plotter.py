# Copyright (c) 2020 Leeman Geophysical LLC.
# Distributed under the terms of the MIT License.

"""Plot and upload."""

# At the top of the hour (minutes 0-14)
# -> Plot the 15 minute file from 45-59 mintues
# -> Plot the last hour
# -> Plot the last day
# -> Plot the last week
#
# At any other time
# -> Plot the 15 minute file for the previous 15 minutes

from datetime import datetime, timedelta
import maptlotlib.pyplot as plt

def plot_fifteen_minutes(now):
    """
    Plots the last 15 minutes (previous index to now)
    """
    filetime = now - timedelta(minutes=15)
    filename = datetime.strftime(filetime, '%Y_%j_%H_%M.txt')
    

def plot_hour(now):
    pass

def plot_day(now):
    pass

def plot_week(now):
    pass

now = datetime.utcnow()

minutes = [0, 15, 30, 45]
minute_idx = now.minute // 15
now = now.replace(minutes[minute_idx])

# We're at the top of the hour
if mintues[minute_idx] == 0:
    plot_fifteen_minutes(now)
    plot_hour(now)
    plot_day(now)
    plot_week(now)
