from pystray import MenuItem as item
import pystray
from PIL import Image
import subprocess


def run_script1():
    # Replace 'path/to/script1.py' with the actual path to your script
    subprocess.run(["python", "path/to/script1.py"])


def run_script2():
    # Replace 'path/to/script2.py' with the actual path to your script
    subprocess.run(["python", "path/to/script2.py"])


image = Image.open("icons/kb-enabled.png").convert("RGB")
menu = (item("Run Script 1", run_script1), item("Run Script 2", run_script2))
icon = pystray.Icon("Test Icon 1", image, "Test Icon 1", menu)
icon.run()
