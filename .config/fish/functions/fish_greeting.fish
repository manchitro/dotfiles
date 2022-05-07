function fish_greeting
    pfetch | lolcat
    echo (date +%a' '%b' '%d', '%Y) | lolcat
    fortune | lolcat
end

