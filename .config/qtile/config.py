from cmath import inf
import os
import subprocess

from decimal import Rounded
from socket import INADDR_ALLHOSTS_GROUP
from turtle import bgcolor
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger

from widgets import btindicator

mod = "mod4"
alt = "mod1"
control = "control"
shift = "shift"

terminal = "kitty"
browser = "google-chrome-stable"

def movetonextgroup(qtile, lazy):
	current_group_name = qtile.current_screen.group.name
	next_group_name = int(current_group_name) + 1
	if next_group_name == 5:
		next_group_name = 1
	logger.warn(next_group_name)
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

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    #Window Management
    Key([mod], "q",                 lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "n",                 lazy.window.toggle_minimize(), desc="Toggle minimization on focused window"),
    Key([], "F11",                  lazy.window.toggle_fullscreen(), desc="Toggle fullscreen",),
    Key([alt], "Tab",               lazy.group.next_window()),
    Key([alt,shift], "Tab",         lazy.group.prev_window()),

    # Switch between windows
    Key([mod], "h",                 lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l",                 lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j",                 lazy.group.next_window(), desc="Move focus to next window"),
    Key([mod], "k",                 lazy.group.prev_window(), desc="Move focus to prev window"),

    # Move windows between
    Key([mod, shift], "h",          lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, shift], "l",          lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, shift], "j",          lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shift], "k",          lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize windows
    Key([mod, control], "h",        lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, control], "l",        lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, control], "j",        lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, control], "k",        lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, shift], "Return",     lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return",            lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "t",                 lazy.spawn(terminal), desc="Launch terminal"),

    #Layout management
    Key([mod], "Tab",               lazy.next_layout(), desc="Toggle between layouts"),

    #Qtile actions
    Key([mod, control], "r",        lazy.reload_config(), desc="Reload the config"),
    Key([mod, control], "q",        lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r",                 lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([control, mod, alt], "r",   lazy.restart(), desc="Restart Qtile"),

    #Browser
    Key([mod], "b",                 lazy.spawn(browser), desc="Open a new browser window"),
    Key([mod, shift], "b",          lazy.spawn(browser + " --incognito"), desc="Open a new incognito browser window"),

    #File Manager
    Key([mod], "f",                 lazy.spawn("pcmanfm"), desc="Open a file manager"),

    #Rofi launchers
    Key([alt], "F1",                lazy.spawn("rofi -combi-modi window,drun,run -show combi -show-icons -kb-cancel Alt+F1,Escape,Alt+v -combi-display-format '{text}' -window-format '> {t}'"), desc="Rofi Application Launcher"),
    Key([alt], "v",                 lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons"), desc="Rofi Clipboard Manager"),
    Key([mod], "c",                 lazy.spawn("bash /home/s/scripts/confedit.sh"), desc="Rofi Window Switcher"),
    Key([mod], "w",                 lazy.spawn("bash /home/s/scripts/rofi-wifi-menu.sh"), desc="Rofi WIFI Menu"),
    Key([mod, control, alt], "b",   lazy.spawn("bash /home/s/scripts/rofi-bluetooth.sh"), desc="Rofi Bluetooth Menu"),

    #Brightness control
    Key([], "XF86MonBrightnessUp",  lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown",lazy.spawn("xbacklight -dec 5")),
    Key([mod, alt, control], "l",   lazy.spawn("xbacklight -inc 5")),
    Key([mod, alt, control], "h",   lazy.spawn("xbacklight -dec 5")),
    Key([mod,  alt, control], "g",  lazy.spawn("xbacklight -set 1")),

    #Audio control
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%")), 
    Key([mod, alt, control], "k",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([mod, alt, control], "j",   lazy.spawn("pactl -- set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute",        lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([mod, alt, control], "m",   lazy.spawn("pactl -- set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([mod], "space",             lazy.spawn("playerctl play-pause")),
    Key([alt], "space",             lazy.spawn("playerctl play-pause")),

    #Shutdown menu
    Key([mod], "0",                 lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1,Escape -show-icons"), desc="Open a power menu"),

    #Screenshot tool - flameshot
    Key([], "Print",                lazy.spawn("flameshot gui"), desc="open flameshot gui"),

    #Bluetooth tws connect/disconnect
    Key([mod, control], "b",        lazy.spawn("bash /home/s/scripts/tws_switch.sh"), desc="connect/disconnect tws"),

    #Bluetooth tws profile switch
    Key([alt, control], "b",        lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="TWS profile switch"),

    #Bluetooth tws profile switch
    Key([mod, shift], "p",          lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh"), desc="tws profile switch"),

    #ProtonVPN swith
    Key([mod, shift], "v",          lazy.spawn("bash /home/s/scripts/protonvpn.sh"), desc="tws profile switch"),

	#Group management
	Key([control, alt], "j",        lazy.screen.next_group(), desc="go to next group"),
	Key([control, alt], "l",        lazy.screen.next_group(), desc="go to next group"),
	Key([control, alt], "k",        lazy.screen.prev_group(), desc="go to next group"),
	Key([control, alt], "h",        lazy.screen.prev_group(), desc="go to next group"),
	Key([control, alt, shift], "j", lazy.function(movetonextgroup, lazy), desc="move window to next group"),
	Key([control, alt, shift], "l", lazy.function(movetonextgroup, lazy), desc="move window to next group"),
	Key([control, alt, shift], "k", lazy.function(movetoprevgroup, lazy), desc="move window to previous group"),
	Key([control, alt, shift], "h", lazy.function(movetoprevgroup, lazy), desc="move window to previous group"),

	#CoolerBoost
	Key([mod], "o",                 lazy.spawn("sudo isw -b on"), desc="Write EC/CoolerBoost"),

	#betterlockscreen
	Key([mod], "Escape",            lazy.spawn("betterlockscreen -l dim"), desc="lock screen"),

    #bitwarden
	Key([mod], "p",                 lazy.spawn("bitwarden-desktop"), desc="Bitwarden password manager"),
]

groups = [
	Group("1", label="WEB",         matches=[Match(wm_class="google-chrome-stable"), Match(wm_class="teams")], layout="stack"),
	Group("2", label="DEV",         matches=[Match(wm_class="jetbrains-idea")], layout="stack"),
	Group("3", label="TXT",         matches=[Match(wm_class="code")], layout="stack"),
	Group("4", label="ETC",         matches=[Match(wm_class="blueman-applet"), Match(wm_class="protonvpn"), Match(wm_class="transmission-gtk"),]),
]

for i in groups:
    keys.extend([
        Key([mod], i.name,          lazy.function(toscreen, i.name), desc="Move to group i"),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc="Move focused window to group i"),
    ])

#Layouts
layouts = [
    layout.Columns                  (border_focus="#ffffff", border_width=1, margin=15, insert_position=1),
    layout.Stack                    (num_stacks=1, border_width=0, margin=15),
    # layout.Max(),
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
        Match(title="Guake!"),  # guake main window
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
	border_width=0,
)

# Default widget attributes
widget_defaults = dict(font="Hack Nerd Font Bold", fontsize=12, padding=3)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
				widget.Spacer       (length=17, mouse_callbacks={"Button1": lazy.spawn("rofi -show drun -show-icons")}),
                widget.Image        (filename="/home/s/.config/qtile/icons/arch.png", margin=5, mouse_callbacks={"Button1": lazy.spawn("rofi -show drun -show-icons")}),
                widget.Clock        (format="%I:%M:%S %p - %a, %b %d", mouse_callbacks={"Button1": lazy.spawn("gnome-calendar")}),
                widget.TextBox      ("|"),
                widget.Net          (format="{down}"),
                widget.Image        (filename="/home/s/.config/qtile/icons/net.png", margin=9),
                widget.Net          (format="{up}"),
                widget.TextBox      ("|"),
                widget.CurrentLayout(),
                widget.TextBox      ("|"),
                widget.GroupBox     (highlight_method="block", font="SpaceMono", fontsize=12, inactive="aaaaaa", rounded=False, hide_unused=False, visible_groups=['1', '2', '3']),
                widget.TextBox      ("|"),
                widget.Prompt       (),
				widget.TaskList     (highlight_method="block", max_title_width=200, title_width_method="uniform", icon_size=12, padding=8, rounded=True, mouse_callbacks={"Button3": lazy.spawn("rofi -show window -kb-cancel Alt+Return,Escape,Alt+F1 -show-icons")}, border='ffffff30', spacing=0),
                widget.TextBox      ("|"),
                widget.Systray      (),
                #widget.TextBox     ("|"),
                #widget.Image       (filename="/home/s/.config/qtile/icons/cpu.png", margin=7),
                #widget.CPU         (format="{load_percent}%"),
                #widget.TextBox     ("|"),
                #widget.Image       (filename="/home/s/.config/qtile/icons/temp.png", margin=6),
                #widget.ThermalSensor(),
                #widget.TextBox     ("|"),
                #widget.Image       (filename="/home/s/.config/qtile/icons/gpu.png", margin=5),
                #widget.NvidiaSensors(),
                #widget.TextBox     ("|"),
                #widget.Image       (filename="/home/s/.config/qtile/icons/ram.png", margin=5),
                #widget.Memory      (measure_mem="G", format="{MemPercent}%"),
                btindicator.BtIndicator (hci="/dev_FC_E8_06_16_0C_AA", mouse_callbacks={"Button3": lazy.spawn("bash /home/s/scripts/tws_switch.sh"), "Button1": lazy.spawn("bash /home/s/scripts/tws_profile_switch.sh")}),
                widget.TextBox      ("|"),
                widget.Image        (filename="/home/s/.config/qtile/icons/copy-content.png", margin=9, mouse_callbacks={"Button1":lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons")}),
                widget.Clipboard    (timeout=0, mouse_callbacks={"Button1":lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}' -kb-cancel Alt+F1,Escape,Alt+v -show-icons")}),
                widget.TextBox      ("|"),
                widget.Image        (filename="/home/s/.config/qtile/icons/sound.png", margin=8, mouse_callbacks={"Button1": lazy.spawn("pavucontrol -t 3"), "Button3": lazy.spawn("pavucontrol -t 4"),},),
                widget.Volume       (get_volume_command="amixer -D pulse get Master".split(), volume_down_command="pactl -- set-sink-volume 0 -5%", volume_up_command="pactl -- set-sink-volume 0 +5%", mouse_callbacks={"Button1": lazy.spawn("pavucontrol -t 3"), "Button3": lazy.spawn("pavucontrol -t 4"),},),
                widget.TextBox      ("|"),
                widget.Image        (filename="/home/s/.config/qtile/icons/brightness.png", margin=8),
                widget.Backlight    (backlight_name="intel_backlight", step=5, mouse_callbacks={"Button1": lazy.spawn("xbacklight -set 1")},),
                widget.TextBox      ("|"),
                widget.Image        (filename="/home/s/.config/qtile/icons/battery.png", margin=7,),
                widget.Battery      (charge_char="+", discharge_char="", format="{char}{percent:2.0%}", update_interval=5, low_foreground="#ffb0ab", notify_below=5,),
                widget.TextBox      ("|"),
                widget.Image        (filename="/home/s/.config/qtile/icons/power.png", margin=8, mouse_callbacks={"Button1": lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1,Escape -show-icons")}),
				widget.Spacer       (length=17, mouse_callbacks={"Button1": lazy.spawn("rofi -show p:rofi-power-menu -kb-cancel Alt+F1,Escape -show-icons")})],
            30,
            background="#00000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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

# default options
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

