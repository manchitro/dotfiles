function fish_user_key_bindings
    fish_vi_key_bindings
    bind -M insert kj "if commandline -P; commandline -f cancel; else; set fish_bind_mode default; commandline -f backward-char force-repaint; end"
    bind -M visual -m default kj

    bind -M default gg beginning-of-buffer
    bind -M default G end-of-buffer

    bind -M visual gg beginning-of-buffer
    bind -M visual G end-of-buffer

    bind -M default V beginning-of-line begin-selection end-of-line
    bind -M visual V beginning-of-line begin-selection end-of-line
end


