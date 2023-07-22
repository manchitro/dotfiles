fish_add_path /home/s/scripts

if status is-interactive
    # Commands to run in interactive sessions can go here
end
alias dots='/usr/bin/git --git-dir=/home/s/.dots/ --work-tree=/home/s'

# tabtab source for jhipster package
# uninstall by removing these lines or running `tabtab uninstall jhipster`
[ -f /home/s/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish ]; and . /home/s/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish


#fish-command-timer variables
set fish_command_timer_time_format '%I:%M:%S%p | %b %d'
set fish_command_timer_min_cmd_duration 3000

set -q XDG_CONFIG_HOME || set -U XDG_CONFIG_HOME $HOME/.config

# Start X at login
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
    exec startx
  end
end

#Abbrevs
abbr -a rd 'ranger ~/Downloads/'
abbr -a rn 'ranger ~/Notes/'
abbr -a fd 'fd -a -d 20'
abbr -a da '/usr/bin/git --git-dir=/home/s/.dots/ --work-tree=/home/s add .config/{autostart,fish,flameshot,fontconfig,gtk-3.0,gtk-4.0,kde.org,kdedefaults,kitty,neofetch,nvim,ranger,xsettingsd,bluedevilglobalrc,gtkrc,gtkrc-2.0,kwinrc,mimeapps.list,plasma-org.kde.plasma.desktop-appletsrc,plasmarc,powermanagementprofilesrc,touchpadxlibinputrc,user-dirs.dirs} .bashrc .ideavimrc .keynavrc .profile .Xmodmap .vimrc .vim/ scripts/ .local/share/applications .icons/ .fonts/ dotroot/'
abbr -a nvidia-smi 'watch -n 1 nvidia-smi'
abbr -a r 'ranger'
abbr -a rh 'ranger ~/'
abbr -a rr 'ranger /'
abbr -a eap 'bash scripts/eap.sh'
abbr -a enable 'sudo systemctl enable'
abbr -a disable 'sudo systemctl disable'
abbr -a start 'sudo systemctl start'
abbr -a stop 'sudo systemctl stop'
abbr -a v 'nvim'
abbr -a rs 'ranger /media/s/Sub/'
abbr -a rms 'ranger /home/s/Downloads/ms/'
abbr -a i 'sudo apt install'
abbr -a isntall 'sudo apt install'
abbr -a install 'sudo apt install'
abbr -a remove 'sudo apt remove'
abbr -a mime 'xdg-mime'
abbr -a pd 'protonvpn-cli d'
abbr -a pc 'protonvpn-cli c'
abbr -a ralttab 'killall alttab && alttab -fg "#CDD6F4" -bg "#1E1E2E" -frame "#89b4fa" -inact "#313244" -font xft:HackNerdFontComplete-Regular -t 500x50 -vertical -d 2 -mk Super_L -kk grave & alttab -fg "#CDD6F4" -bg "#1E1E2E" -frame "#89b4fa" -inact "#313244" -font xft:HackNerdFontComplete-Regular -t 500x50 -vertical -d 0 -bw 10 -bc "#1E1E2E" & disown'
abbr -a ru 'ranger ~/orion/proxy-us/source/proxy-voting/'
abbr -a ri 'ranger ~/orion/proxy-international/source/proxy-voting/'
abbr -a ys 'yarn start'
abbr -a yb 'yarn build'
abbr -a rcbis 'ranger /home/s/Downloads/ms/CVPR/repo/MARL-CBIS/resources/downloaded/cbis/jpeg/'
abbr -a rmarl 'ranger /home/s/Downloads/ms/CVPR/repo/MARL-CBIS/'
abbr -a marl '/home/s/Downloads/ms/CVPR/repo/MARL-CBIS/'
abbr -a gm 'git commit -m "'
abbr -a gd 'git diff'
abbr -a fan 'sudo python3 /home/s/repo/MSI-Dragon-Center-for-Linux/set_fan.py'
abbr -a rl 'ranger ~/.local'
abbr -a ga 'git add .'
abbr -a tv 'sudo teamviewer --daemon start'
abbr -a tvs 'sudo teamviewer --daemon stop'
#Abbrevs end

## >>> conda initialize >>>
## !! Contents within this block are managed by 'conda init' !!
#if test -f /home/s/Downloads/ms/CVPR/miniconda3/bin/conda
#    eval /home/s/Downloads/ms/CVPR/miniconda3/bin/conda "shell.fish" "hook" $argv | source
#end
#mkdir -p $CONDA_PREFIX/etc/conda/activate.d
#echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
#echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/targets/x86_64-linux/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
#
## <<< conda initialize <<<

set -g EDITOR nvim
set -g VISUAL nvim
set GTK_THEME (gtk-query-settings | grep gtk-theme-name | awk '{print $2}' | tr -d "\"")
