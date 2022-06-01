# Copyright (c) 2010 Aldo Cortesi

# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions: #
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"

terminal = "kitty"

vol_cur  = "amixer -D pulse get Master"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "k", lazy.layout.grow_up(), desc="Grow window up"),
    #Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, shift],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Browser
    Key([mod], "b", lazy.spawn("google-chrome"), desc="Open a google-chrome"),

    #File Manager
    Key([mod], "f", lazy.spawn("nautilus"), desc="Open a file manager"),

    #Restart qtile
    Key([control, mod, alt], "r", lazy.restart(), desc="Restart Qtile"),

    #Rofi launchers
    Key([alt], "F1", lazy.spawn("rofi -show drun -kb-cancel Alt+F1,Escape,Alt+v"), desc="Rofi Application Launcher"),
    Key([alt], "v", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v, Esc"), desc="Rofi Clipboard Manager"),
    Key([alt], "Return", lazy.spawn("rofi -show window -kb-cancel Alt+Return,Escape,Alt+F1"), desc="Rofi Window Switcher"),
    Key([mod], "c", lazy.spawn("bash /home/s/scripts/confedit.sh"), desc="Rofi Window Switcher"),

    # toggle between windows just like in unity with 'alt+tab'
    Key([alt,shift], "Tab", lazy.layout.down()),
    Key([alt], "Tab", lazy.layout.up()),

    #Brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    Key([mod, alt, control], "l", lazy.spawn("xbacklight -inc 5")),
    Key([mod, alt, control], "h", lazy.spawn("xbacklight -dec 5")),

    #Audio control
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("pactl -- set-sink-volume 0 +5%") #amixer -c 0 -q set Master 2dB+
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("pactl -- set-sink-volume 0 -5%") #amixer -c 0 -q set Master 2dB-
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("pactl -- set-sink-mute 0 toggle") #amixer -c 0 -q set Master toggle
    ),
    Key(
        [mod], "space",
        lazy.spawn("playerctl play-pause") #amixer -c 0 -q set Master toggle
    ),
    Key(
        [mod, alt, control], "k",
        lazy.spawn("pactl -- set-sink-volume 0 +5%") #amixer -c 0 -q set Master 2dB+
    ),
    Key(
        [mod, alt, control], "j",
        lazy.spawn("pactl -- set-sink-volume 0 -5%") #amixer -c 0 -q set Master 2dB-
    ),
    Key(
        [mod, alt, control], "m",
        lazy.spawn("pactl -- set-sink-mute 0 toggle") #amixer -c 0 -q set Master toggle
    ),


    #Toggle Minimize window
    Key([mod], "n", lazy.window.toggle_minimize(), desc="Toggle minimization on focused window"),

    #Shutdown menu
    Key([mod], "0", lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1"), desc="Open a power menu"),

    #Screenshot tool - flameshot
    Key([], "Print", lazy.spawn("flameshot gui"), desc="open flameshot gui")
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, shift],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, shift], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(),
    layout.Columns(border_focus="#cccccc", border_width=1, margin=10),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#Define colors
colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]

def longNameParse(text):
    arr=text.split('|')
    for window in arr:
        if "Google Chrome" in window:
            arr[arr.index(window)]=window[-14:]
    text=' |'.join(arr)
    return text

widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(filename="/home/s/.config/qtile/icons/ubuntu.png", margin=7, mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},),
                widget.TextBox("|"),
                widget.Clock(format="%I:%M:%S %p - %a, %b %d", mouse_callbacks={"Button1": lazy.spawn("gnome-calendar")}),
                widget.TextBox("|"),
                widget.Net(format="{down}"),
                widget.Image(filename="/home/s/.config/qtile/icons/net.png", margin=7),
                widget.Net(format="{up}"),
                widget.TextBox("|"),
                widget.Prompt(),
                widget.WindowTabs(font="Montserrat", parse_text=longNameParse),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                widget.TextBox("|"),
                widget.Systray(),
                widget.TextBox("|"),
                widget.Image(filename="/home/s/.config/qtile/icons/cpu.png", margin=7),
                widget.CPU(format="{load_percent}%"),
                widget.TextBox("|"),
                widget.Image(filename="/home/s/.config/qtile/icons/temp.png", margin=6),
                widget.ThermalSensor(),
                widget.TextBox("|"),
                widget.Image(filename="/home/s/.config/qtile/icons/gpu.png", margin=5),
                widget.NvidiaSensors(),
                widget.TextBox("|"),
                widget.Image(filename="/home/s/.config/qtile/icons/ram.png", margin=5),
                widget.Memory(measure_mem="G", format="{MemUsed: .2f}{mm} /{MemTotal: .2f}{mm}"),
                widget.TextBox("| 📋"),
                widget.Clipboard(),
                widget.TextBox("|"),
                widget.Image(filename="/home/s/.config/qtile/icons/sound.png", margin=7, mouse_callbacks={"Button1": lazy.spawn("pavucontrol")}),
                widget.Volume(get_volume_command="amixer -D pulse get Master".split(), mouse_callbacks={"Button1": lazy.spawn("pavucontrol")}),
                widget.TextBox("| 🔆"),
                widget.Backlight(backlight_name="intel_backlight"),
                widget.TextBox("|"),
                widget.Battery(charge_char="⚡ ", discharge_char="🔋 ",format="{char}{percent:2.0%}"),
                widget.TextBox("|"),
                widget.Image(
                    filename="/home/s/.config/qtile/icons/power.png",
                    margin=7,
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1")},
                    ),
            ],
            30,
            background="#ffffff10"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie # and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

import os
import subprocess

from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


