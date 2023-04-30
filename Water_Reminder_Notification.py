import time
from plyer import notification

if __name__ ==  "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = '''Water helps your body:
Keep a normal temperature. Lubricate and cushion joints. Protect your spinal cord and other sensitive tissues. Get rid of wastes through urination, perspiration, and bowel movements.''',
            # app_icon = "C:\\Users\\syeda\\OneDrive\\Desktop\\Notification\\im.png",
            timeout = 4
        )
        time.sleep(30)

        