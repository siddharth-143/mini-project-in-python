"""
    Python program to implement battery notification
"""

# pip install psutil
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent >= 30:
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=str(percent) + "% Battery remaining",
        duration=5,
        urgency=Notification,
    ).send()