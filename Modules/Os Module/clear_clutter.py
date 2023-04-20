import os
files = os.listdir("D:\\Code\\Python\\Modules\\Os Module\\cluttered")

i = 1
for file in files:
    if file.endswith(".pdf"):
        os.rename(f"D:\\Code\\Python\\Modules\\Os Module\\cluttered\\{file}",
                  f"D:\\Code\\Python\\Modules\\Os Module\\cluttered\\{i}.pdf")
        i = i + 1
