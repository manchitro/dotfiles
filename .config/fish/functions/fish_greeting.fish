function fish_greeting
    echo (set_color yellow; date +%T; set_color normal)
    fortune | lolcat
end

