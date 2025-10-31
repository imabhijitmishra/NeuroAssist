import time
from datetime import datetime

# Define the medication times
medication_schedule = {
    "08:00": "Donepezil",
    "14:00": "Memantine",
    "20:00": "Rivastigmine"
}

print("🧠 NeuroAssist Reminder Timer started...\n")

while True:
    now = datetime.now().strftime("%H:%M")
    if now in medication_schedule:
        medicine = medication_schedule[now]
        print(f"💊 Reminder: It's {now}! Time to take your medicine: {medicine}")
        time.sleep(60)
    else:
        time.sleep(30)
