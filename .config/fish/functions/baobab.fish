function baobab --description alias\ baobab\ GTK_THEME=\(gtk-query-settings\ \|\ grep\ gtk-theme-name\ \|\ awk\ \'\{print\ \$2\}\'\ \|\ tr\ -d\ \"\\\"\"\)\ baobab
  GTK_THEME=(gtk-query-settings | grep gtk-theme-name | awk '{print $2}' | tr -d "\"") baobab $argv
        
end
