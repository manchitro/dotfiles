fish_add_path ~/scripts -g
fish_add_path ~/.local/bin/ -g

set -U fish_user_paths /usr/local/cuda/include $fish_user_paths
set -Ux LD_LIBRARY_PATH /home/s/Downloads/Compressed/TensorRT-8.6.1.6/lib

if status is-interactive
and not set -q TMUX
    exec tmux
end
alias dots='/usr/bin/git --git-dir=/home/s/.dots/ --work-tree=/home/s'

# tabtab source for jhipster package
# uninstall by removing these lines or running `tabtab uninstall jhipster`
[ -f ~/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish ]; and . ~/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish


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
abbr -a da '/usr/bin/git --git-dir=/home/s/.dots/ --work-tree=/home/s add .config/{autostart,fish,flameshot,fontconfig,gtk-3.0,gtk-4.0,kde.org,kdedefaults,kitty,neofetch,nvim,ranger,xsettingsd,bluedevilglobalrc,gtkrc,gtkrc-2.0,kwinrc,mimeapps.list,plasma-org.kde.plasma.desktop-appletsrc,plasmarc,powermanagementprofilesrc,touchpadxlibinputrc,user-dirs.dirs,dconf,dolphinrc,filetypesrc,flameshotrc,gwenviewrc,katerc,kde*,kglobalshortcutsrc,khotkeysrc,okularpartrc,okularrc,plasmanotifyrc,plasmashellrc,systemsettingsrc,kwinrulesrc,tmux, qtile, deadd} .bashrc .ideavimrc .keynavrc .profile .Xmodmap .vimrc .vim/ scripts/ .local/share/{applications,rofi,plasma} .icons/ .fonts/ dotroot/ .tmux/' 
abbr -a nvidia-smi 'watch -n 1 nvidia-smi'
abbr -a r 'ranger'
abbr -a rh 'ranger ~/'
abbr -a rr 'ranger /'
abbr -a eap 'bash ~/scripts/eap.sh'
abbr -a enable 'sudo systemctl enable'
abbr -a disable 'sudo systemctl disable'
abbr -a start 'sudo systemctl start'
abbr -a stop 'sudo systemctl stop'
abbr -a v 'nvim'
abbr -a rs 'ranger /media/s/Sub/'
abbr -a rms 'ranger ~/Downloads/MS-materials/'
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
abbr -a yi 'yarn install'
abbr -a rcbis 'ranger ~/Downloads/ms/CVPR/repo/MARL-CBIS/resources/downloaded/cbis/jpeg/'
abbr -a rmarl 'ranger ~/Downloads/ms/CVPR/repo/MARL-CBIS/'
abbr -a marl '~/Downloads/ms/CVPR/repo/MARL-CBIS/'
abbr -a gm 'git commit -m "'
abbr -a gd 'git diff'
abbr -a fan 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py'
abbr -a f0 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 100'
abbr -a f1 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 110'
abbr -a f2 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 120'
abbr -a f3 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 130'
abbr -a f4 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 140'
abbr -a f5 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 150'
abbr -a f9 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 90'
abbr -a f8 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 80'
abbr -a f7 'sudo python3 ~/repo/MSI-Dragon-Center-for-Linux/set_fan.py 70'
abbr -a rl 'ranger ~/.local'
abbr -a ga 'git add .'
abbr -a tv 'sudo teamviewer --daemon start'
abbr -a tvs 'sudo teamviewer --daemon stop'
abbr -a update 'sudo apt update'
abbr -a logout 'qdbus org.kde.Shutdown /Shutdown logout'
abbr -a reboot 'qdbus org.kde.Shutdown /Shutdown logoutAndReboot'
abbr -a shutdown 'qdbus org.kde.Shutdown /Shutdown logoutAndShutdown'
abbr -a cool 'sudo isw -b on'
abbr -a hot 'sudo isw -b off'
#Abbrevs end

## >>> conda initialize >>>
## !! Contents within this block are managed by 'conda init' !!
#if test -f ~/Downloads/ms/CVPR/miniconda3/bin/conda
#    eval ~/Downloads/ms/CVPR/miniconda3/bin/conda "shell.fish" "hook" $argv | source
#end
#mkdir -p $CONDA_PREFIX/etc/conda/activate.d
#echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
#echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/targets/x86_64-linux/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
#
## <<< conda initialize <<<

set -g EDITOR nvim
set -g VISUAL nvim
set GTK_THEME (gtk-query-settings | grep gtk-theme-name | awk '{print $2}' | tr -d "\"")
