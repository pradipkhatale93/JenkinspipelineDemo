from datetime import *
from pytz import *
from telegram import *

birthdays = 'Birthday_data'

file1 = open(birthdays, 'r')
today = datetime.now(timezone('Asia/kolkata'))
print("Date:")
print(today)
today_string = today.strftime("%m%d")
print(today_string)

API_Key = "5479759464:AAE8nUok2_-2be062AOr4KDDsiRTGe5yYDU"
CHAT_ID = "1229546292"
bot = Bot(API_Key)

#updater = Updater(API_Key, use_context=True)
#updater.start_polling()


flag = 0
for i in file1:
    if today_string in i:
        message = "\n Today's Birthday Notification: \n !!_Happy BirthDay_!! \n "
        i = i.split(' ')
        flag = 1
        message += i[1] + '\n'
        print(message)
        bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

if flag == 0:
    message = " \n Today's Birthday Notification: \n No Birthday today"
    print(message)
    bot.send_message(
    chat_id=CHAT_ID,
    text=message
        )
#updater.stop