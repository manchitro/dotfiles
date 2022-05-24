if status is-interactive
    # Commands to run in interactive sessions can go here
end
alias dots='/usr/bin/git --git-dir=/home/s/dotfiles/ --work-tree=/home/s'

# tabtab source for jhipster package
# uninstall by removing these lines or running `tabtab uninstall jhipster`
[ -f /home/s/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish ]; and . /home/s/orion/proxy-us/source/proxy-voting/Client/node_modules/tabtab/.completions/jhipster.fish


#fish-command-timer variables
set fish_command_timer_time_format '%I:%M:%S%p | %b %d'
