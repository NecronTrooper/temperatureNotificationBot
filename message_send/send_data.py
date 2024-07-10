import serial
import time
import urequests as requests

# Initialize the serial port
ser = serial.Serial('COM8', 9600)  # Adjust port as needed

# Telegram bot setup
TELEGRAM_TOKEN = 'your_tg_bot_api'
CHAT_ID = 'your_id'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response

while True:
    if ser.in_waiting:
        temperature_data = int(ser.readline().decode('utf-8').strip())
        print(f"Received temperature: {temperature_data}°C")
        if temperature_data > 25: #send notification when temperature is high
            send_telegram_message(f"Temperature Alert: {temperature_data}°C")
            time.sleep(300)
