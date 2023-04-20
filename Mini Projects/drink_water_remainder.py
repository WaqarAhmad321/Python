from plyer import notification
import time
while True:
    time.sleep(5)
    notification.notify(
        app_name="Remainder",
        title="Drink Water Remainder",
        message="Time for a glass of water.",
        app_icon="D:\Setups\drink-water.ico",
        timeout=10,

    )
