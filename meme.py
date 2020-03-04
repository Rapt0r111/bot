def send_message(chat_id, text):
url = "https://api.telegram.org/bot{token}/{method}".format(token="1141601649:AAEO9WVLjW_2XDz2eCoPvIF1-BQFss3-jRg",method="sendMessage")
data = {
"chat_id": chat_id,
"text": text
}
r = requests.post(url, data=data)
print(r.json())

def reply_keyboard_markup(keyboard, resize, one_time):
url = "https://api.telegram.org/bot{token}/{method}".format(
token="TOKEN",
method="ReplyKeyboardMarkup"
)

data = {
"keyboard": keyboard,
"resize_keyboard": resize,
"one_time_keyboard": one_time
}

def main(event, context):
start_menu = reply_keyboard_markup(["Расписание", "Меню"], True, True)
start_text = "bla bla bla"
if msg == "/start":
send_message(id, start_text, start_menu)