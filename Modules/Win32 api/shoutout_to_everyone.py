import win32com.client as wi

speaker = wi.Dispatch("SAPI.SpVoice")
words = ["Python", "Code", "Programming", "Win32com.client"]
# i = 0
# while True:
#     if i <= len(words) - 1:
#         speaker.Speak(f"Shoutout to {words[i]}")
#     else:
#         break
#     i = i + 1
for word in words:
    speaker.Speak(f"Shoutout to {word}")

# words = input("Enter the words you want to listen from the Computer:\n")
# speaker.Speak(words)
