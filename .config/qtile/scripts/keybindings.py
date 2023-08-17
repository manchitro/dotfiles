
from cmath import inf
import os
import subprocess
import datetime

from decimal import Rounded
from socket import INADDR_ALLHOSTS_GROUP
from turtle import bgcolor
from webbrowser import BackgroundBrowser
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from widgets import btindicator
from qtile_extras import widget

mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"
capslock = "lock"

terminal = "kitty"
browser = "google-chrome-stable"
filemanager = "nautilus"

def movetonextgroup(qtile, lazy):
	current_group_name = qtile.current_screen.group.name
	next_group_name = int(current_group_name) + 1
	if next_group_name == 5:
		next_group_name = 1
	qtile.current_window.togroup(str(next_group_name), switch_group=True)

def movetoprevgroup(qtile, lazy):
	current_group_name = qtile.current_screen.group.name
	prev_group_name = int(current_group_name) - 1
	if prev_group_name == 0:
		prev_group_name = 4
	logger.warn(prev_group_name)
	qtile.current_window.togroup(str(prev_group_name), switch_group=True)

def gotonextgroup(qtile):
	current_group_name = qtile.current_screen.group.name
	next_group_name = int(current_group_name) + 1
	qtile.current_screen.set_group(qtile.groups[next_group_name-1])

def gotoprevgroup(qtile):
	current_group_name = qtile.current_screen.group.name
	prev_group_name = int(current_group_name) - 1
	qtile.current_screen.set_group(qtile.groups[prev_group_name-1])

def toscreen(qtile, group_name):
    if group_name  == qtile.current_screen.group.name:
        qtile.current_screen.set_group(qtile.current_screen.previous_group)
    else:
        for i in range(len(qtile.groups)):
            if group_name == qtile.groups[i].name:
                qtile.current_screen.set_group(qtile.groups[i])
                break
@lazy.function
def minimize_all(qtile):
    areAllMinimized = True
    for win in qtile.current_group.windows:
        if getattr(win, "minimized") is False:
            win.toggle_minimize()
            areAllMinimized = False
    if areAllMinimized is True:
        for win in qtile.current_group.windows:
                win.toggle_minimize()


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    Key([control, mod, alt, shift], "Home", None, desc="Window Management"),
    Key([mod], "q",                 lazy.window.kill(), desc="Close Window"),
    Key([mod], "n",                 lazy.window.toggle_minimize(), desc="Toggle minimize"),
	Key([mod, shift], "n", 			minimize_all(), desc="Toggle minimize on all windows"),
    Key([mod], "m",                 lazy.window.toggle_maximize(), desc="Toggle maximize"),
    Key([], "F11",                  lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),

    Key([control, mod, alt, shift], "Home", None, desc="Switch between windows"),
    Key([mod], "h",                 lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l",                 lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j",                 lazy.group.next_window(), desc="Move focus to next window"),
    Key([mod], "k",                 lazy.group.prev_window(), desc="Move focus to prev window"),

    Key([control, mod, alt, shift], "Home", None, desc="Move windows"),
    Key([mod, shift], "h",          lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, shift], "l",          lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, shift], "j",          lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k",          lazy.layout.shuffle_up(), desc="Move window up"),

    Key([control, mod, alt, shift], "Home", None, desc="Resize windows"),
    Key([control, mod, shift], "h",        lazy.layout.grow_left(), desc="Grow window left"),
    Key([control, mod, shift], "l",        lazy.layout.grow_right(), desc="Grow window right"),
    Key([control, mod, shift], "j",        lazy.layout.grow_down(), desc="Grow window down"),
    Key([control, mod, shift], "k",        lazy.layout.grow_up(), desc="Grow window up"),

	#Group management
    Key([control, mod, alt, shift], "Home", None, desc="Group Management"),
    Key([mod], "Tab",               lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, shift], "Return",     lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
# 	Key([control, alt], "l",        lazy.screen.next_group(), desc="go to next group"),
# 	Key([control, alt], "h",        lazy.screen.prev_group(), desc="go to next group"),
	#Key([control, alt, shift], "j", lazy.function(movetonextgroup, lazy), desc="move window to next group"),
	#Key([control, alt, shift], "l", lazy.function(movetonextgroup, lazy), desc="move window to next group"),
	#Key([control, alt, shift], "k", lazy.function(movetoprevgroup, lazy), desc="move window to previous group"),
	#Key([control, alt, shift], "h", lazy.function(movetoprevgroup, lazy), desc="move window to previous group"),

    #Qtile actions
    Key([control, mod, alt, shift], "Home", None, desc="Qtile Management"),
    Key([mod, control], "r",        lazy.reload_config(), desc="Reload config"),
    Key([mod], "r",                 lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod, control], "q",        lazy.shutdown(), desc="Shutdown Qtile"),
    Key([control, mod, alt], "r",   lazy.restart(), desc="Restart Qtile"),

    Key([control, mod, alt, shift], "Home", None, desc="Launch Apps"),
    Key([mod], "Return",            lazy.spawn(terminal), desc="Launch terminal"),              #Terminal
    Key([mod], "b",                 lazy.spawn(browser), desc="Open a new browser window"),     #Broswer
    Key([mod, shift], "b",          lazy.spawn("buku-rofi --nostdin"), desc="List bookmarks"),  #Browser bookmarks
    Key([mod], "f",                 lazy.spawn(filemanager), desc="Open file manager"),         #File Manager

    #Rofi launchers
    Key([control, mod, alt, shift], "Home", None, desc="Menus"),
    Key([alt], "F1",                lazy.spawn("rofi --combi-modi window,drun,run -show combi -show-icons -kb-cancel Alt+F1,Escape,Alt+v -combi-display-format '{text}' -window-format '> {t}'"), desc="Application Launcher"),
    Key([alt], "v",                 lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons"), desc="Clipboard Manager"),
    Key([mod], "c",                 lazy.spawn("bash /home/s/scripts/confedit.sh vim"), desc="Config files edit with vim"),
    Key([mod, shift], "c",          lazy.spawn("bash /home/s/scripts/confedit.sh code"), desc="Config files edit with code"),
    Key([mod], "s",                 lazy.spawn("bash /home/s/scripts/scriptedit.sh vim"), desc="Scripts edit with vim"),
    Key([mod, shift], "s",          lazy.spawn("bash /home/s/scripts/scriptedit.sh code"), desc="Scripts edit with code"),
    Key([mod], "w",                 lazy.spawn("bash /home/s/scripts/rofi-wifi-menu.sh"), desc="WIFI Menu"),
    Key([mod, shift], "w",          lazy.spawn("bash /home/s/scripts/wifi-switch.sh"), desc="Switch wifi to hotspot"),
    Key([mod, control, alt], "b",   lazy.spawn("bash /home/s/scripts/rofi-bluetooth.sh"), desc="Bluetooth Menu"),
    Key([mod], "0",                 lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1,Escape -show-icons"), desc="Open power menu"),

    #Brightness control
    Key([control, mod, alt, shift], "Home", None, desc="Brighness Control"),
    Key([], "XF86MonBrightnessUp",  lazy.spawn("xbacklight -inc 5"), desc="Increase Brightness by 5%"),
    Key([], "XF86MonBrightnessDown",lazy.spawn("xbacklight -dec 5"), desc="Decrease Brightness by 5%"),
    Key([mod, alt, control], "l",   lazy.spawn("xbacklight -inc 5"), desc="Increase Brightness by 5%"),
    Key([mod, alt, control], "h",   lazy.spawn("xbacklight -dec 5"), desc="Decrease Brightness by 5%"),
    Key([mod, alt, control], "g",   lazy.spawn("xbacklight -set 1"), desc="Set Brightness to 1%"),
    Key([mod, alt, control], "semicolon",   lazy.spawn("xbacklight -set 100"), desc="Set Brightness to 100%"),

    #Audio control
    Key([control, mod, alt, shift], "Home", None, desc="Audio Control"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase Volume by 5%"), 
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease Volume by 5%"),
    Key([mod, alt, control], "k",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase Volume by 5%"),
    Key([mod, alt, control], "j",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease Volume by 5%"),
    Key([], "XF86AudioMute",        lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle volume mute"),
    Key([mod, alt, control], "m",   lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle volume mute"),
    Key([mod, shift], "m",   		lazy.spawn("amixer set Capture toggle"), desc="Toggle mic mute"),
    Key([mod], "space",             lazy.spawn("playerctl play-pause"), desc="Media pause/resume"),
    Key([alt], "space",             lazy.spawn("playerctl play-pause"), desc="Media pause/resume"),


    #Screenshot tool - flameshot
    Key([control, mod, alt, shift], "Home", None, desc="Screenshot"),
    Key([mod], "Print",             lazy.spawn("flameshot full"), desc="Save fullscreen screenshot"),
    Key([mod, shift], "Print",      lazy.spawn("flameshot full --clipboard"), desc="Copy fullscreen screenshot"),
    Key([], "Print",                lazy.spawn("flameshot gui"), desc="Open screenshotter"),
    Key([control,mod], "s",         lazy.spawn("flameshot gui"), desc="Open screenshotter"),

    #Bluetooth tws connect/disconnect
    Key([control, mod, alt, shift], "Home", None, desc="Bluetooth settings"),
    Key([mod, control], "b",        lazy.spawn("bash /home/s/scripts/tws_switch.sh"), desc="Connect/Disconnect earphones"),
    Key([mod, control, shift], "b",        lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="Earphones profile switch"),
    Key([mod, shift], "p",          lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="tws profile switch"),

    #ProtonVPN swith
    Key([control, mod, alt, shift], "Home", None, desc="VPN settings"),
    Key([mod, shift], "v",          lazy.spawn("bash /home/s/scripts/protonvpn.sh"), desc="Toggle VPN"),

	#Misc
    Key([control, mod, alt, shift], "Home", None, desc="Misc"),
    Key([mod], "p",                 lazy.spawn("bash /home/s/scripts/picom_switch.sh"), desc="Toggle aesthetics"),
	Key([mod], "o",                 lazy.spawn("sudo isw -b on"), desc="CPU Fan Max Speed"),
	Key([mod, shift], "o",          lazy.spawn("sudo isw -b off"), desc="CPU Fan Normal Speed"),
	Key([mod], "Escape",            lazy.spawn("betterlockscreen -l"), desc="Lock screen"),
    Key([mod], "v",                 lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True), desc="Show/Hide Notification Center"),
    Key([capslock], "h",        lazy.spawn("xdotool key --clearmodifiers --delay 1 Left" ), desc="Mimic left arrow"),
    Key([capslock], "j",        lazy.spawn("xdotool key --clearmodifiers --delay 1 Down" ), desc="Mimic down arrow"),
    Key([capslock], "k",        lazy.spawn("xdotool key --clearmodifiers --delay 1 Up"   ), desc="Mimic up arrow"),
    Key([capslock], "l",        lazy.spawn("xdotool key --clearmodifiers --delay 1 Right"), desc="Mimic right arrow"),
]

def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        mods += k.key.capitalize()

        #replace mod1 with Alt
        mods = mods.replace("Mod1", "Alt")
        mods = mods.replace("Alt + F1", "Super")

        #replace x86 key codes
        mods=mods.replace("Xf86monbrightness","Fn + Arrow ")
        mods=mods.replace("Xf86audioraisevolume","Fn + Arrow right")
        mods=mods.replace("Xf86audiolowervolume","Fn + Arrow left")
        mods=mods.replace("Xf86audiomute","Fn + End")

        #expand length to 30 if not category line
        if "Home" not in mods:
            mods = "\t"+mods
            for i in range(30-len(mods)):
                mods += " "

        mods=mods.replace("Control + Super + Alt + Shift + Home","")

        key_help += "{} {}".format(mods, k.desc + "\n")

    return key_help

keys.extend([Key([mod], "slash", lazy.spawn("sh -c 'echo \"" + show_keys() + "\" | rofi -dmenu -i -mesg \"Keyboard Shortcuts\" -theme spotlight-dark-mono'"), desc="Print keyboard bindings"),])

groups = [
	Group("1", label="WWW",         matches=[Match(wm_class="google-chrome-stable"), Match(wm_class="teams")], layout="columns"),
	Group("2", label="DEV",         matches=[Match(wm_class="jetbrains-idea")], layout="stack"),
	Group("3", label="TXT",         matches=[Match(wm_class="azuredatastudio")], layout="stack"),
	Group("4", label="ETC",         matches=[Match(wm_class="blueman-applet"), Match(wm_class="protonvpn"), Match(wm_class="transmission-gtk"),]),
]

for i in groups:
    keys.extend([
        Key([mod], i.name,          lazy.function(toscreen, i.name), desc="Move to group i"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Move focused window to group i"),
    ])

groups.append(
	ScratchPad(
        "scratchpad",   
        [
            DropDown(
                "term",
                terminal,
                opacity=0.9,
                height=1,
                width=0.99,
                x=0.0055,
                y=-0.005,
                on_focus_lost_hide=True
            ),
            DropDown(
                'todo',
                'kuro',
                height = 0.8,
                width = 0.8,
                x = 0.1,
                y = 0.0,
                on_focus_lost_hide = False,
                opacity = 0.85,
                warp_pointer = False,
                match = Match(wm_class="kuro"),
            ),
            DropDown(
                'calc',
                'gnome-calculator',
                height = 0.2,
                width = 0.2,
                x = 0.8,
                y = 0.0,
                on_focus_lost_hide = False,
                opacity = 0.85,
                warp_pointer = False,
                match = Match(wm_class="gnome-calculator"),
            ),
        ],
    )
)

keys.extend([
	Key([], "grave", lazy.group['scratchpad'].dropdown_toggle("term"), desc="Dropdown terminal"),
	Key([], "F1", lazy.group['scratchpad'].dropdown_toggle("todo"), desc="todo list"),
	Key([], "F5", lazy.group['scratchpad'].dropdown_toggle("calc"), desc="Calculator"),
	Key([mod], "r", lazy.group['scratchpad'].dropdown_toggle("ranger"), desc="ranger"),
])

#Layouts
layouts = [
    #layout.Max                      (margin=20, border_width=2),
    layout.Stack                    (border_focus="#89B4FA", border_width=0, margin=[10, 10, 15, 10], num_stacks=1),
    layout.Columns                  (border_focus="#89B4FA", border_width=2, margin=[10, 10, 15, 10], insert_position=1, border_on_single=False, num_columns=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(panel_width=100, place_right=True, bg_color="00000000", vspace=5, inactive_bg="00000020", active_bg="ffffff20", font="Hack Nerd Font Bold", sections=["Tabs"]),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="gnome-calculator"),  # calculator
        Match(wm_class="indicator-stickynotes"),  # notes
        Match(wm_class="guake"),  # guake main window
        Match(wm_class="eww"),  # eww widgets
        Match(wm_class="eww"),  # eww widgets
        Match(wm_class="qjackctl"),  # eww widgets
        #Match(wm_class="zoom"),  # eww widgets
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
	border_width=0,
)

#Catppuccin Mocha
COLOR_01="#45475A"          # HOST
COLOR_02="#F38BA8"          # SYNTAX_STRING
COLOR_03="#A6E3A1"          # COMMAND
COLOR_04="#F9E2AF"          # COMMAND_COLOR2
COLOR_05="#89B4FA"          # PATH
COLOR_06="#F5C2E7"          # SYNTAX_VAR
COLOR_07="#94E2D5"          # PROMP
COLOR_08="#BAC2DE"          #

COLOR_09="#585B70"          #
COLOR_10="#F38BA8"          # COMMAND_ERROR
COLOR_11="#A6E3A1"          # EXEC
COLOR_12="#F9E2AF"          #
COLOR_13="#89B4FA"          # FOLDER
COLOR_14="#F5C2E7"          #
COLOR_15="#94E2D5"          #
COLOR_16="#A6ADC8"          #
SURFACE_0="#313244"
SURFACE_1="#45475a"

BACKGROUND_COLOR="#1E1E2E"  # Background Color
FOREGROUND_COLOR="#CDD6F4"  # Text

# Default widget attributes
widget_defaults = dict(font="Hack Nerd Font Bold", fontsize=12, padding=3)
extension_defaults = widget_defaults.copy()
my_sep = widget.Sep(foreground="89B4FA", size_percent=50, padding=15, linewidth=2)

screens = [
    Screen(
        bottom=bar.Bar(
            [
				widget.Spacer(                                                  #right padding
                    length=10, 
                    mouse_callbacks={
                        "Button1": lazy.group['scratchpad'].dropdown_toggle("term"),                        },
                    ),
                widget.Image(                                                   #distro logo
                    filename="/home/s/.config/qtile/icons/arch.png", 
                    margin=5, 
                    mouse_callbacks={
                        "Button1": lazy.spawn("rofi -show drun -show-icons"),
                        },
                    ),
                widget.Clock(                                                   #clock and date
                    format="%I:%M:%S %p - %a, %d %b", 
                    mouse_callbacks={
                        "Button1": lazy.spawn("eww open --toggle calendarWindow"),
                        },
                    ),
                my_sep,
                widget.Net(                                                     #net down
                    format="{down} ▼▲ {up}", 
                    prefix="k",
                    ),
                my_sep,
                widget.GroupBox(                                                #groups
                    highlight_method="line", 
                    font="SpaceMono Bold",
                    fontsize=11,
                    inactive=COLOR_16,
                    padding=8,
                    margin=4, 
                    rounded=False,
                    hide_unused=False,
                    visible_groups=[],
                    highlight_color=COLOR_01+"66",
                    this_current_screen_border=COLOR_05,
                    mouse_callbacks={
                        "Button3": lazy.spawn(browser),
                        },
                    ),
                my_sep,
                widget.Prompt(),
				widget.TaskList(                                                #taskbar
                    highlight_method="block",
                    max_title_width=200,
                    title_width_method="uniform",
                    icon_size=15,
                    padding=7,
                    rounded=False,
                    mouse_callbacks={
                        "Button3": lazy.spawn("xdotool key super+Tab"),
                        },
                    border=SURFACE_1,
                    foreground=FOREGROUND_COLOR,
                    spacing=0,
                    ),
                btindicator.BtIndicator(                                        #TWS indicatior
                        hci="/dev_FC_E8_06_16_0C_AA",
                        mouse_callbacks={
                            "Button3": lazy.spawn("bash /home/s/scripts/tws_switch.sh"), 
                            "Button1": lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh")
                            },
                        ),
                my_sep,
                widget.Systray(),
                #my_sep,
                #widget.Image(                                                   #CPU image
                #        filename="/home/s/.config/qtile/icons/cpu.png",
                #        margin=7
                #        ),
                #widget.CPU(                                                     #CPU load
                #        format="{load_percent}%",
                #        ),
                #my_sep,
                #widget.Image(                                                   #GPU image
                #        filename="/home/s/.config/qtile/icons/gpu.png",
                #        margin=5,
                #        ),
                #widget.NvidiaSensors(),
                #my_sep,
                #widget.Image(                                                   #RAM image
                #        filename="/home/s/.config/qtile/icons/ram.png",
                #        margin=5,
                #        ),
                #widget.Memory(                                                  #RAM usage
                #        measure_mem="G",
                #        format="{MemPercent}%",
                #        ),
                my_sep,
                widget.Image(                                                   #clipboard image
                        filename="/home/s/.config/qtile/icons/copy-content.png",
                        margin=10,
                        mouse_callbacks={
                            "Button1":lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons")
                            },
                        ),
                widget.Clipboard(                                               #clipboard content
                        timeout=0,
                        mouse_callbacks={
                            "Button1":lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons")
                            },
                        ),
                my_sep,
                widget.Image(                                                   #CPU temp image
                        filename="/home/s/.config/qtile/icons/temp.png",
                        margin=8,
                        ),
                widget.ThermalSensor(                                           #CPU temp
                        fontsize=13,
                        ),
                my_sep,
                widget.Image(                                                   #Volume image
                        filename="/home/s/.config/qtile/icons/sound.png",
                        margin=9,
                        mouse_callbacks={
                            "Button1": lazy.spawn("amixer set Master toggle"),                      #left click     - toggle mute
                            "Button3": lazy.spawn("pavucontrol -t 3"),                              #right click    - open pulseaudio control center volume tab
                            "Button4": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +1%"),   #scroll up      - volume up 1%
                            "Button5": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -1%"),   #scroll down    - volume down 1%
                            "Button2": lazy.spawn("bash /home/s/scripts/tws_switch.sh"),            #middle click   - connect/disconnect TWS
                            },
                        ),
                widget.Volume(                                                  #Volume level                                                                      
                        get_volume_command="amixer -D pulse get Master".split(),                    
                        volume_down_command="pactl -- set-sink-volume @DEFAULT_SINK@ -1%",
                        volume_up_command="pactl -- set-sink-volume @DEFAULT_SINK@ +1%",
                        mouse_callbacks={
                            "Button1": lazy.spawn("amixer set Master toggle"),                      #left click     - toggle mute
                            "Button3": lazy.spawn("pavucontrol -t 3"),                              #right click    - open pulseaudio control center volume tab
                            "Button2": lazy.spawn("bash /home/s/scripts/tws_switch.sh"),            #middle click   - connect/disconnect TWS
                            }, 
                        fontsize=13,
                        ),
                my_sep,
                widget.Image(                                                   #Mic image
                        filename="/home/s/.config/qtile/icons/mic.png",
                        margin=9,
                        mouse_callbacks={
                            "Button1": lazy.spawn("amixer set Capture toggle"),                     #left click     - toggle mic mute
                            "Button3": lazy.spawn("pavucontrol -t 4"),                              #right click    - open pulseaudio control center input tab
                            "Button4": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SOURCE@ +1%"), #scroll up      - mic volume up 1%
                            "Button5": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SOURCE@ -1%"), #scroll down    - mic volume down 1%
                            },
                        ),
                widget.Volume(                                                  #Mic level
                        get_volume_command="amixer get Capture".split(),
                        volume_down_command="pactl -- set-source-volume @DEFAULT_SOURCE@ -1%",
                        volume_up_command="pactl -- set-source-volume @DEFAULT_SOURCE@ +1%",
                        mouse_callbacks={
                            "Button1": lazy.spawn("amixer set Capture toggle"),                     #left click     - toggle mic mute
                            "Button3": lazy.spawn("pavucontrol -t 4"),                              #right click    - open pulseaudio control center input tab
                            }, 
                        fontsize=13,
                        ),
                my_sep,
                widget.Image(                                                   #Brightness image
                        filename="/home/s/.config/qtile/icons/bulb.png",
                        margin=8,
                        mouse_callbacks={
                            "Button4": lazy.spawn("xbacklight -inc 10"),                            #scroll up      - brightness up 10%
                            "Button5": lazy.spawn("xbacklight -dec 10"),                            #scroll down    - brightness down 10%
                            },
                        ),
                widget.Backlight(                                               #Brighness level
                        backlight_name="intel_backlight",
                        step=5,
                        mouse_callbacks={
                            "Button1": lazy.spawn("xbacklight -set 1"),                             #left click     - brightness set 1%
                            },
                        fontsize=13,
                        ),
                my_sep,
                widget.Image(                                                   #Battery image
                        filename="/home/s/.config/qtile/icons/battery.png",
                        margin=8,
                        ),
                widget.Battery(                                                 #Battery level
                        charge_char="+",
                        discharge_char="",
                        format="{char}{percent:2.0%}",
                        update_interval=5,
                        low_foreground="#ffb0ab",
                        notify_below=11,
                        notification_timeout=0,
                        fontsize=13,
                        ),
                my_sep,
                widget.Image(                                                   #Notification center
                        filename="/home/s/.config/qtile/icons/bell.png",
                        margin=9,
                        mouse_callbacks={
                            "Button1": lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True),
                            },
                        ),
				widget.Spacer(                                                  #right padding
                        length=5,
                        mouse_callbacks={
                            "Button1": lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True),
                            },
                        ),
                widget.Sep(
                        linewidth=4,
                        size_percent=100,
                        foreground="#89b4fa",
                        padding=0,
                        mouse_callbacks={
                            "Button1": lazy.spawn("xdotool key super+shift+n"),
                            },
                        ),
            ],
            33,
            background=BACKGROUND_COLOR+"00",
            border_width=[1,0,0,0],
            border_color="#89b4fa"+"ee",
            #margin=[5,10,5,10]
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",          lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3",          lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Drag([mod, shift], "Button1",   lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2",         lazy.window.bring_to_front()),
]

# hooks
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

@hook.subscribe.client_focus
def on_focus(client):
    lazy.window.bring_to_front()

@hook.subscribe.client_new
def focus_group(client):
	for group in groups: 
		match = next((m for m in group.matches if m.compare(client)), None)
		if match:
			if group.name != '4':
				targetgroup = client.qtile.groups_map[group.name]  # there can be multiple instances of a group
				targetgroup.cmd_toscreen(toggle=False)
				break

@hook.subscribe.client_name_updated
def focus_group(client):
	for group in groups: 
		match = next((m for m in group.matches if m.compare(client)), None)
		if match:
			if group.name != '4' and (client.get_wm_class()[0] == 'code' or client.get_wm_class()[0] == 'google-chrome'):
				targetgroup = client.qtile.groups_map[group.name]  # there can be multiple instances of a group
				targetgroup.cmd_toscreen(toggle=False)
				break

@hook.subscribe.focus_change
def float_to_front(qtile):
    """
    Bring all floating windows of the group to front
    """
    for window in qtile.currentGroup.windows:
        if window.floating:
            window.cmd_bring_to_front()


# default options
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

