function fish_user_key_bindings
    fish_vi_key_bindings
    bind -M insert kj "if commandline -P; commandline -f cancel; else; set fish_bind_mode default; commandline -f backward-char force-repaint; end"
    bind -M visual -m default kj

    bind -M default gg beginning-of-buffer
    bind -M default G end-of-buffer

    bind -M visual gg beginning-of-buffer
    bind -M visual G end-of-buffer

    bind -M default H beginning-of-line
    bind -M default L end-of-line

    bind -M visual H beginning-of-line
    bind -M visual L end-of-line

    bind -M default V beginning-of-line begin-selection end-of-line
    bind -M visual V beginning-of-line begin-selection end-of-line

    bind -M visual \cu togglecase-selection
    bind -M visual v kill-selection

    bind yy fish_clipboard_copy
end


