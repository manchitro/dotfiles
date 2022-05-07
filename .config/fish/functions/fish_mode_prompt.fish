function fish_mode_prompt
  switch $fish_bind_mode
    case default
      set_color --bold red
      echo 'Norm'
    case insert
      set_color --bold green
      echo 'Ins'
    case replace_one
      set_color --bold green
      echo 'Rep'
    case visual
      set_color --bold brmagenta
      echo 'Vis'
    case '*'
      set_color --bold red
      echo '?'
  end
  echo ' | '
  set_color normal
end
