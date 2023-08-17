import sys
from libqtile.command.client import InteractiveCommandClient
if len(sys.argv) == 2:
    c = InteractiveCommandClient()
    c.simulate_keypress([], sys.argv[1])
    print("Pressed " + sys.argv[1])
else:
    print("Keyname needed")
