import time 
def countdown(time_and_seconds):
    while time_and_seconds:
        minutes, seconds = divmod(time_and_seconds, 60)
        time_format =  "{:02d}: {:02d}".format(minutes,seconds)
        print(time_format, end = "\r")
        time.sleep(1)
        time_and_seconds -= 1

print("Countdown finished.")

countdown(0) #Enter amount in seconds!!!

    