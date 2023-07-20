function fish_prompt
    echo -n (set_color brcyan)$USER' '(set_color brmagenta)'in '(set_color brgreen)(prompt_pwd)' '
    echo (set_color brmagenta)'on'(set_color bryellow)(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/')
    echo -n (set_color white)'⥂ '
end
