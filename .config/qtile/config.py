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
from libqtile.command.client import InteractiveCommandClient

#modifiers
mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"
capslock = "lock"
slash = "mod5"

#apps
terminal = "kitty"
browser = "google-chrome"
filemanager = "dolphin"

#commands
cmd_app_launcher = "rofi --combi-modi window,drun,run -show combi -show-icons -kb-cancel Alt+F1,Escape,Alt+v -combi-display-format '{text}' -window-format '> {t}'"

#user defined functions
def movetonextgroup(qtile, lazy):
    current_group_name = qtile.current_screen.group.name
    next_group_name = int(current_group_name) + 1
    if next_group_name == 6:
        next_group_name = 1
    qtile.current_window.togroup(str(next_group_name), switch_group=True)
def movetoprevgroup(qtile, lazy):
    current_group_name = qtile.current_screen.group.name
    prev_group_name = int(current_group_name) - 1
    if prev_group_name == 0:
        prev_group_name = 5
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
    if group_name == qtile.current_screen.group.name:
        qtile.current_screen.set_group(qtile.current_screen.previous_group)
    else:
        for i in range(len(qtile.groups)):
            if group_name == qtile.groups[i].name:
                qtile.current_screen.set_group(qtile.groups[i])
                break
def tolastgroup(qtile, group_name):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

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
    Key([mod], "q",                 lazy.window.kill(), desc="Close Window (Window Management)"),
    Key([mod], "n",                 lazy.window.toggle_minimize(), desc="Toggle minimize (Window Management)"),
    Key([mod, shift], "n", 	    minimize_all(), desc="Toggle minimize on all windows (Window Management)"),
    Key([mod], "m",                 lazy.window.toggle_maximize(), desc="Toggle maximize (Window Management)"),
    Key([], "F11",                  lazy.window.toggle_fullscreen(), desc="Toggle fullscreen (Window Management)",),

    Key([control, mod, alt, shift], "Home", None, desc="Window Switching"),
    Key([mod], "h",                 lazy.layout.left(), desc="Move focus to left (Window Switching)"),
    Key([mod], "l",                 lazy.layout.right(), desc="Move focus to right (Window Switching)"),
    Key([mod], "j",                 lazy.group.next_window(), desc="Move focus to next window (Window Switching)"),
    Key([mod], "k",                 lazy.group.prev_window(), desc="Move focus to prev window (Window Switching)"),

    Key([control, mod, alt, shift], "Home", None, desc="Window Movement"),
    Key([mod, shift], "h",          lazy.layout.shuffle_left(), desc="Move window left (Window Movement)"),
    Key([mod, shift], "l",          lazy.layout.shuffle_right(), desc="Move window right (Window Movement)"),
    Key([mod, shift], "j",          lazy.layout.shuffle_down(), desc="Move window down (Window Movement)"),
    Key([mod, shift], "k",          lazy.layout.shuffle_up(), desc="Move window up (Window Movement)"),
    Key([mod, shift], "period",     lazy.function(movetonextgroup, lazy), desc="Move window to next group (Window Movement)"),
    Key([mod, shift], "comma",      lazy.function(movetoprevgroup, lazy), desc="Move window to prev group (Window Movement)"),

    Key([control, mod, alt, shift], "Home", None, desc="Window Resizing"),
    Key([control, mod, shift], "h", lazy.layout.grow_left(), desc="Grow window left (Window Resizing)"),
    Key([control, mod, shift], "l", lazy.layout.grow_right(), desc="Grow window right (Window Resizing)"),
    Key([control, mod, shift], "j", lazy.layout.grow_down(), desc="Grow window down (Window Resizing)"),
    Key([control, mod, shift], "k", lazy.layout.grow_up(), desc="Grow window up (Window Resizing)"),

    # Group management
    Key([control, mod, alt, shift], "Home", None, desc="Group Management"),
    Key([mod], "Tab",               lazy.next_layout(), desc="Toggle between layouts (Group Management)"),
    Key([mod, shift], "Return",     lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack (Group Management)",),
    Key([mod], "period",            lazy.screen.next_group(), desc="Go to next group (Group Management)"),
    Key([mod], "comma",             lazy.screen.prev_group(), desc="Go to prev group (Group Management)"),
    Key([mod], "slash",             lazy.screen.toggle_group(), desc="Switch to previous group (Group Management)"),

    # Window Manager actions
    Key([control, mod, alt, shift], "Home", None, desc="Window Manager Actions"),
    Key([mod, control], "r",        lazy.reload_config(), desc="Reload configuration (Window Manager Actions)"),
    #Key([mod], "r",                 lazy.spawncmd(), desc="Spawn a command using a prompt widget (Window Manager Actions)"),
    Key([control, mod, alt], "r",   lazy.restart(), desc="Restart Window Manager (Window Manager Actions)"),
    Key([mod, control], "q",        lazy.shutdown(), desc="Shutdown Window Manager (Window Manager Actions)"),
    #Key([mod, shift], "b",          lazy.hide_show_bar("all"), desc="Show/Hide Bars (Window Manager Actions)"),

    Key([control, mod, alt, shift], "Home", None, desc="Launch Apps"),
    Key([mod], "Return",            lazy.spawn(terminal), desc="Launch terminal (Launch Apps)"),
    Key([mod], "b",                 lazy.spawn(browser), desc="Open a new browser window (Launch Apps)"),
    Key([mod, alt], "b",            lazy.spawn("firefox --private-window"), desc="Open a new incognito browser window (Launch Apps)"),
    Key([mod, shift], "b",          lazy.spawn("google-chrome-stable"), desc="Open a new chrome window (Launch Apps)"),
    Key([mod], "f",                 lazy.spawn(filemanager), desc="Open file manager (Launch Apps)"),

    # Rofi launchers
    Key([control, mod, alt, shift], "Home", None, desc="Menus"),
    Key([alt], "F1",                lazy.spawn(cmd_app_launcher, shell=True), desc="Application Launcher (Menus)"),
    Key([alt], "v",                 lazy.spawn("rofi-gpaste"), desc="Clipboard Manager (Menus)"),
    Key([mod], "c",                 lazy.spawn("bash /home/s/scripts/confedit.sh nvim"), desc="Config files edit with nvim (Menus)"),
    Key([mod, shift], "c",          lazy.spawn("bash /home/s/scripts/confedit.sh code"), desc="Config files edit with code (Menus)"),
    Key([mod], "s",                 lazy.spawn("bash /home/s/scripts/scriptedit.sh nvim"), desc="Scripts edit with nvim (Menus)"),
    Key([mod, shift], "s",          lazy.spawn("bash /home/s/scripts/scriptedit.sh code"), desc="Scripts edit with code (Menus)"),
    Key([mod], "w",                 lazy.spawn("bash /home/s/scripts/rofi-wifi-menu.sh"), desc="WIFI Menu (Menus)"),
    Key([mod, shift], "w",          lazy.spawn("bash /home/s/scripts/wifi-switch.sh"), desc="Switch wifi to hotspot (Menus)"),
    Key([mod, control, alt], "b",   lazy.spawn("bash /home/s/scripts/rofi-bluetooth.sh"), desc="Bluetooth Menu (Menus)"),
    Key([mod], "0",                 lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1,Escape -show-icons"), desc="Power menu (Menus)"),

    # Brightness control
    Key([control, mod, alt, shift], "Home", None, desc="Brightness Control"),
    Key([], "XF86MonBrightnessUp",  lazy.spawn( "xbacklight -inc 5"), desc="Increase Brightness by 5% (Brightness Control)"),
    Key([], "XF86MonBrightnessDown",lazy.spawn( "xbacklight -dec 5"), desc="Decrease Brightness by 5% (Brightness Control)"),
    Key([mod, alt, control], "l",   lazy.spawn( "xbacklight -inc 5"), desc="Increase Brightness by 5% (Brightness Control)"),
    Key([mod, alt, control], "h",   lazy.spawn( "xbacklight -dec 5"), desc="Decrease Brightness by 5% (Brightness Control)"),
    Key([mod, alt, control], "g",   lazy.spawn( "xbacklight -set 1"), desc="Set Brightness to 1% (Brightness Control)"),
    Key([mod, alt, control], "semicolon",   lazy.spawn( "xbacklight -set 100"), desc="Set Brightness to 100% (Brightness Control)"),

    # Audio control
    Key([control, mod, alt, shift], "Home", None, desc="Audio Control"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase Volume by 5% (Audio Control)"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease Volume by 5% (Audio Control)"),
    Key([mod, alt, control], "k",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%"), desc="Increase Volume by 5% (Audio Control)"),
    Key([mod, alt, control], "j",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%"), desc="Decrease Volume by 5% (Audio Control)"),
    Key([], "XF86AudioMute",        lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle volume mute (Audio Control)"),
    Key([mod, alt, control], "m",   lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle"), desc="Toggle volume mute (Audio Control)"),
    Key([mod, shift], "m",   	    lazy.spawn("amixer set Capture toggle"), desc="Toggle mic mute (Audio Control)"),
    Key([alt], "space",             lazy.spawn("playerctl play-pause"), desc="Media play/pause/resume (Audio Control)"),


    # Screenshot tool - flameshot
    Key([control, mod, alt, shift], "Home", None, desc="Screenshot"),
    Key([mod], "Print",             lazy.spawn("flameshot full"), desc="Save fullscreen screenshot"),
    Key([mod, shift], "Print",      lazy.spawn("flameshot full --clipboard"), desc="Copy fullscreen screenshot"),
    Key([], "Print",                lazy.spawn("flameshot gui"), desc="Open screenshotter"),
    Key([control, mod], "s",        lazy.spawn("flameshot gui"), desc="Open screenshotter"),

    # Bluetooth tws connect/disconnect
    Key([control, mod, alt, shift], "Home", None, desc="Bluetooth settings"),
    Key([mod, control], "b",        lazy.spawn("bash /home/s/scripts/tws_switch.sh"), desc="Connect/Disconnect Bluetooth headphones"),
    #Key([mod, control, shift], "b", lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="Earphones profile switch"),
    #Key([mod, shift], "p",          lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="tws profile switch"),

    # ProtonVPN swith
    Key([control, mod, alt, shift], "Home", None, desc="VPN settings"),
    Key([mod, shift], "v",          lazy.spawn(
        "bash /home/s/scripts/protonvpn.sh"), desc="Toggle VPN"),

    # Misc
    Key([control, mod, alt, shift], "Home", None, desc="Misc"),
    Key([mod], "p",                 lazy.spawn("bash /home/s/scripts/picom_switch.sh"), desc="Toggle aesthetics"),
    Key([mod], "o",                 lazy.spawn("sudo isw -b on"), desc="CPU Fan Max Speed"),
    Key([mod, shift], "o",          lazy.spawn("sudo isw -b off"), desc="CPU Fan Normal Speed"),
    Key([mod], "Escape",            lazy.spawn("betterlockscreen -l"), desc="Lock screen"),
    Key([mod], "v",                 lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True), desc="Show/Hide Notification Center"),
    Key([], "F10",                  lazy.spawn("tdrop -ma -s dropdown kitty", shell=True), desc="Dropdown terminal"),
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

        # replace mod1 with Alt
        mods = mods.replace("Mod1", "Alt")
        mods = mods.replace("Alt + F1", "Super")

        # replace x86 key codes
        mods = mods.replace("Xf86monbrightness", "Fn + Arrow ")
        mods = mods.replace("Xf86audioraisevolume", "Fn + Arrow right")
        mods = mods.replace("Xf86audiolowervolume", "Fn + Arrow left")
        mods = mods.replace("Xf86audiomute", "Fn + End")

        # expand length to 30 if not category line
        if "Home" not in mods:
            mods = "\t"+mods
            for i in range(30-len(mods)):
                mods += " "

        mods = mods.replace("Control + Super + Alt + Shift + Home", "")

        key_help += "{} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend([Key([mod, shift], "slash", lazy.spawn("sh -c 'echo \"" + show_keys() +
            "\" | rofi -dmenu -i -mesg \"Keyboard Shortcuts\" -theme spotlight-dark-mono'"), desc="Print keyboard bindings"),])

groups = [
    Group("1", label="WWW", layout="stack"),
    Group("2", label="DEV", matches=[Match(wm_class="jetbrains-idea"), Match(wm_class="obsidian")], layout="stack"),
    Group("3", label="TXT", matches=[Match(wm_class="azuredatastudio"), Match(wm_class="Jaspersoft Studio")], layout="stack"),
    Group("4", label="ETC", matches=[Match(wm_class="blueman-applet"), Match(wm_class="protonvpn"), Match(wm_class="transmission-gtk"), Match(wm_class="TeamViewer")], layout="stack"),
    Group("5", label="RES", layout="stack"),
]

for i in groups:
    keys.extend([
        Key([mod], i.name,          lazy.function( toscreen, i.name), desc="Move to group i"),
        Key([mod, "shift"], i.name, lazy.window.togroup( i.name, switch_group=True), desc="Move focused window to group i"),
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
                width=1,
                x=0,
                y=0,
                on_focus_lost_hide=True
            ),
            DropDown(
                'todo',
                'kuro',
                height=0.9,
                width=0.8,
                x=0.1,
                y=-0.03,
                on_focus_lost_hide=True,
                opacity=0.85,
                warp_pointer=False,
                match=Match(wm_class="kuro"),
            ),
            DropDown(
                'calc',
                'gnome-calculator',
                height=0.2,
                width=0.4,
                x=0.6,
                y=0.0,
                on_focus_lost_hide=False,
                opacity=0.85,
                warp_pointer=False,
                match=Match(wm_class="gnome-calculator"),
            ),
            DropDown(
                'clipboard',
                'gpaste-ui',
                height=0.8,
                width=0.8,
                x=0.1,
                y=0.0,
                on_focus_lost_hide=True,
                opacity=0.85,
                warp_pointer=False,
                match=Match(wm_class="gpaste-ui"),
            ),
            DropDown(
                'teams',
                'teams',
                height=0.9,
                width=0.8,
                x=0.1,
                y=-0.03,
                on_focus_lost_hide=True,
                opacity=0.85,
                warp_pointer=False,
                match=Match(wm_class="microsoft teams - preview"),
            ),
        ],
    )
)

keys.extend([
    # Key([], "F10", lazy.group['scratchpad'].dropdown_toggle("term"), desc="Dropdown terminal"),
    Key([], "F1", lazy.group['scratchpad'].dropdown_toggle("todo"), desc="todo list"),
    Key([], "F5", lazy.group['scratchpad'].dropdown_toggle("calc"), desc="Calculator"),
    Key([mod], "r", lazy.group['scratchpad'].dropdown_toggle("ranger"), desc="ranger"),
    Key([mod], "t", lazy.group['scratchpad'].dropdown_toggle("teams"), desc="teams"),
])

# Layouts
layouts = [
    # layout.Max                      (margin=20, border_width=2),
    layout.Stack(border_focus="dddddd", border_width=0,
                 margin=15, num_stacks=1),
    layout.Columns(border_focus="dddddd", border_width=1, margin=15,
                   insert_position=1, border_on_single=False, num_columns=2),
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
        Match(wm_class="qjackctl"),
        Match(wm_class="dconf-editor"),
        Match(wm_class="TeamViewer"),
        Match(title=""),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=0,
)

# Catppuccin Mocha
COLOR_01 = "#45475A"          # HOST
COLOR_02 = "#F38BA8"          # SYNTAX_STRING
COLOR_03 = "#A6E3A1"          # COMMAND
COLOR_04 = "#F9E2AF"          # COMMAND_COLOR2
# COLOR_05 = "#89B4FA"          # PATH
COLOR_05 = "#dddddd"          # PATH
COLOR_06 = "#F5C2E7"          # SYNTAX_VAR
COLOR_07 = "#94E2D5"          # PROMP
COLOR_08 = "#BAC2DE"          #

PEACH = "#fe640b"

COLOR_09 = "#585B70"          #
COLOR_10 = "#F38BA8"          # COMMAND_ERROR
COLOR_11 = "#A6E3A1"          # EXEC
COLOR_12 = "#F9E2AF"          #
COLOR_13 = "#89B4FA"          # FOLDER
COLOR_14 = "#F5C2E7"          #
COLOR_15 = "#94E2D5"          #
COLOR_16 = "#A6ADC8"          #
SURFACE_0 = "#313244"
SURFACE_1 = "#45475a"

BACKGROUND_COLOR = "#1E1E2E"  # Background Color
FOREGROUND_COLOR = "#CDD6F4"  # Text

# Default widget attributes
widget_defaults = dict(font="Hack Bold", fontsize=14, padding=3)
extension_defaults = widget_defaults.copy()
my_sep = widget.Sep(foreground=COLOR_05, size_percent=50,
                    padding=15, linewidth=2)

screens = [
    Screen(
        wallpaper='/home/s/wallpapers/Sundarbans_web_cropped.jpg',
        wallpaper_mode='stretch',
        top=bar.Bar([
            widget.TaskList(  # taskbar
                    highlight_method="block",
                    max_title_width=250,
                    title_width_method="uniform",
                    icon_size=18,
                    padding_x=5,
                    padding_y=3,
                    rounded=True,
                    mouse_callbacks={
                        "Button3": lazy.spawn("xdotool key super+Tab"),
                        "Button2": lazy.window.kill(),
                    },
                    unfocused_border=SURFACE_1+"00",
                    foreground=SURFACE_0,
                    spacing=5,
                    window_name_location=False,
                    borderwidth=0,
                    border="#a6adc8",
                    ),
            #widget.Spacer(),
            widget.Image(  # clipboard image
                filename="/home/s/.config/qtile/icons/copy-content.png",
                margin=8,
                mouse_callbacks={
                    "Button1": lazy.spawn("rofi-gpaste")
                },
            ),
            widget.Clipboard(  # clipboard content
                timeout=0,
                mouse_callbacks={
                    "Button1": lazy.spawn("rofi-gpaste")
                },
                blacklist=['bitwarden'],
                blacklist_text='*******',
                max_chars=30,
                max_width=None,
            ),
            my_sep,
            widget.Systray(),
            widget.Spacer(length=10)
        ],
            30,
            background=SURFACE_1+"77",
            border_width=[0, 0, 1, 0],
            border_color=COLOR_05+"ee",
            # margin=[5,10,5,10]
        ),
        bottom=bar.Bar(
            [
                widget.Image(  # distro logo
                    filename="/home/s/.config/qtile/icons/arch.png",
                    margin=6,
                    mouse_callbacks={
                        "Button1": lazy.spawn("rofi -show drun -show-icons"),
                    },
                ),
                widget.Clock(  # clock and date
                    format="%I:%M:%S %p - %a, %d %b",
                    mouse_callbacks={
                        "Button1": lazy.spawn("/home/s/repo/eww/target/release/eww open --toggle calendarWindow"),
                    },
                ),
                my_sep,
                widget.Net(  # net down
                    format="{down} ▼▲ {up}",
                    prefix="k",
                ),
                my_sep,
                widget.GroupBox(  # groups
                    highlight_method="line",
                    font="DejaVu Sans ",
                    fontsize=12,
                    inactive=COLOR_16,
                    padding=8,
                    margin=4,
                    rounded=False,
                    hide_unused=False,
                    highlight_color=COLOR_01+"66",
                    this_current_screen_border=COLOR_05,
                    mouse_callbacks={
                        "Button3": lazy.spawn(browser),
                    },
                ),
                my_sep,
                widget.Prompt(),
                widget.WindowName(
                    font='Hack Bold',
                ),
                # widget.TaskList(                                                #taskbar
                #    highlight_method="block",
                #    max_title_width=200,
                #    title_width_method="uniform",
                #    icon_size=15,
                #    padding=7,
                #    rounded=False,
                #    mouse_callbacks={
                #        "Button3": lazy.spawn("xdotool key super+Tab"),
                #        "Button2": lazy.window.kill(),
                #        },
                #    border=SURFACE_1,
                #    foreground=FOREGROUND_COLOR,
                #    spacing=0,
                #    ),
                # my_sep,
                widget.Image(  # CPU image
                    filename="/home/s/.config/qtile/icons/processor.png",
                    margin=7
                ),
                widget.CPU(  # CPU load
                    format="{load_percent}%",
                    update_interval=5,
                ),
                my_sep,
                widget.Image(  # GPU image
                    filename="/home/s/.config/qtile/icons/graphic-card.png",
                    margin=5,
                ),
                widget.GenPollText(
                    func=lambda: subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits']).decode().strip(),
                    update_interval=5,
                    fmt='{}%',
                ),
                my_sep,
                widget.Image(  # RAM image
                    filename="/home/s/.config/qtile/icons/memory.png",
                    margin=5,
                ),
                widget.Memory(  # RAM usage
                    measure_mem="G",
                    format="{MemPercent}%",
                    update_interval=5,
                ),
                my_sep,
                widget.Image(  # CPU temp image
                    filename="/home/s/.config/qtile/icons/thermometer.png",
                    margin=8,
                ),
                widget.ThermalSensor(),
                my_sep,
                widget.Image(  # Volume image
                    filename="/home/s/.config/qtile/icons/sound.png",
                    margin=9,
                    mouse_callbacks={
                        # left click     - toggle mute
                        "Button1": lazy.spawn("amixer set Master toggle"),
                        # right click    - open pulseaudio control center volume tab
                        "Button3": lazy.spawn("pavucontrol -t 3"),
                        # scroll up      - volume up 1%
                        "Button4": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +1%"),
                        # scroll down    - volume down 1%
                        "Button5": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -1%"),
                        # middle click   - connect/disconnect TWS
                        "Button2": lazy.spawn("bash /home/s/scripts/tws_switch.sh"),
                    },
                ),
                widget.Volume(  # Volume level
                    get_volume_command="amixer -D pulse get Master".split(),
                    volume_down_command="pactl -- set-sink-volume @DEFAULT_SINK@ -1%",
                    volume_up_command="pactl -- set-sink-volume @DEFAULT_SINK@ +1%",
                    mouse_callbacks={
                        # left click     - toggle mute
                        "Button1": lazy.spawn("amixer set Master toggle"),
                        # right click    - open pulseaudio control center volume tab
                        "Button3": lazy.spawn("pavucontrol -t 3"),
                        # middle click   - connect/disconnect TWS
                        "Button2": lazy.spawn("bash /home/s/scripts/tws_switch.sh"),
                    },
                    fontsize=13,
                ),
                my_sep,
                widget.Image(  # Mic image
                    filename="/home/s/.config/qtile/icons/mic.png",
                    margin=9,
                    mouse_callbacks={
                        # left click     - toggle mic mute
                        "Button1": lazy.spawn("amixer set Capture toggle"),
                        # right click    - open pulseaudio control center input tab
                        "Button3": lazy.spawn("pavucontrol -t 4"),
                        # scroll up      - mic volume up 1%
                        "Button4": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SOURCE@ +1%"),
                        # scroll down    - mic volume down 1%
                        "Button5": lazy.spawn("pactl -- set-sink-volume @DEFAULT_SOURCE@ -1%"),
                    },
                ),
                widget.Volume(  # Mic level
                    get_volume_command="amixer get Capture".split(),
                    volume_down_command="pactl -- set-source-volume @DEFAULT_SOURCE@ -1%",
                    volume_up_command="pactl -- set-source-volume @DEFAULT_SOURCE@ +1%",
                    mouse_callbacks={
                        # left click     - toggle mic mute
                        "Button1": lazy.spawn("amixer set Capture toggle"),
                        # right click    - open pulseaudio control center input tab
                        "Button3": lazy.spawn("pavucontrol -t 4"),
                    },
                    fontsize=13,
                ),
                my_sep,
                widget.Image(  # Brightness image
                    filename="/home/s/.config/qtile/icons/bulb.png",
                    margin=8,
                    mouse_callbacks={
                        # scroll up      - brightness up 10%
                        "Button4": lazy.spawn("xbacklight -inc 10"),
                        # scroll down    - brightness down 10%
                        "Button5": lazy.spawn("xbacklight -dec 10"),
                    },
                ),
                widget.Backlight(  # Brighness level
                    backlight_name="intel_backlight",
                    step=5,
                    mouse_callbacks={
                        # scroll up      - brightness up 10%
                        "Button4": lazy.spawn("xbacklight -inc 10"),
                        # scroll down    - brightness down 10%
                        "Button5": lazy.spawn("xbacklight -dec 10"),
                    },
                    fontsize=13,
                ),
                my_sep,
                widget.Image(  # Battery image
                    filename="/home/s/.config/qtile/icons/battery.png",
                    margin=8,
                ),
                #                 widget.BatteryIcon(),
                widget.Battery(  # Battery level
                    charge_char="+",
                    discharge_char="",
                    format="{char}{percent:2.0%}",
                    update_interval=1,
                    low_foreground="#ffb0ab",
                    notify_below=11,
                    notification_timeout=0,
                    fontsize=13,
                ),
                my_sep,
                widget.Image(  # Notification center
                    filename="/home/s/.config/qtile/icons/bell.png",
                    margin_y=9,
                    mouse_callbacks={
                        "Button1": lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True),
                    },
                ),
                widget.Spacer(  # right padding
                    length=8,
                    mouse_callbacks={
                        "Button1": lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)", shell=True),
                    },
                ),
                #widget.Sep(
                #    linewidth=4,
                #    size_percent=100,
                #    foreground=COLOR_05,
                #    padding=0,
                #    mouse_callbacks={
                #        "Button1": lazy.spawn("xdotool key super+shift+n"),
                #    },
                #),
            ],
            33,
            background=SURFACE_1+"77",
            border_width=[1, 0, 0, 0],
            border_color=COLOR_05+"ee",
            # margin=[5,10,5,10]
        ),
    )
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",          lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3",          lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Drag([mod, shift], "Button1",   lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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
            if group.name != '5':
                # there can be multiple instances of a group
                targetgroup = client.qtile.groups_map[group.name]
                targetgroup.cmd_toscreen(toggle=False)
                break


@hook.subscribe.client_name_updated
def focus_group(client):
    for group in groups:
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            if group.name and (client.get_wm_class()[0] == 'code' or client.get_wm_class()[0] == 'google-chrome'):
                # there can be multiple instances of a group
                targetgroup = client.qtile.groups_map[group.name]
                targetgroup.cmd_toscreen(toggle=False)
                break


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
