Vim�UnDo� b��?��L���p�Xw���٣��׾���Э   �   set termguicolors                         	    d��    _�                     d        ����                                                                                                                                                                                                                                                                                                                                                             d��M    �   d               �   e            �   d            5��    d                      �                     �    d                  I   �              �      5�_�                    e       ����                                                                                                                                                                                                                                                                                                                            k           e          V       d��r    �   d   e          0is_vim="ps -o state= -o comm= -t '#{pane_tty}' \   A    | grep -iqE '^[^TXZ ]+ +(\\S+\\/)?g?(view|n?vim?x?)(diff)?$'"   Gbind-key -n C-h  if-shell  "$is_vim"  "send-keys C-h"  "select-pane -L"   Ibind-key -n C-j   if-shell  "$is_vim"  "send-keys C-j"   "select-pane -D"   Gbind-key -n C-k  if-shell  "$is_vim"  "send-keys C-k"  "select-pane -U"   Ibind-key -n C-l   if-shell  "$is_vim"  "send-keys C-l"   "select-pane -R"   Ibind-key -n C-\   if-shell  "$is_vim"  "send-keys C-\\"  "select-pane -l"5��    d                      �      �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�?�    �         d      imap kj <Esc>5��                                              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             d�@    �         d      " imap kj <Esc>5��                                              5�_�      	              d        ����                                                                                                                                                                                                                                                                                                                                                             d�n    �   d   �           �   e   f        �   d   f        5��    d                      �                     �    d                      �              J      5�_�                	   f       ����                                                                                                                                                                                                                                                                                                                            �           �          V       d��    �   d   �          >" Enable line and character visual mode after pressing Shift+S�   e   f        �   e   f          (xnoremap S :<C-U>call SurroundWith()<CR>       function! SurroundWith()   3    " Get the user input for the surrounding string   F    let surround_string = input("Enter the string to surround with: ")       @    " Store the original register and clear it for pasting later       let reg_save = @"       let @" = ''       6    " Yank the selected text into the unnamed register       normal! gv"xy       )    " Build the final replacement command   *    let replacement = surround_string . @"   U    let replacement .= substitute(substitute(@" , '\n', '\\n', 'g'), '"', '\\"', 'g')   &    let replacement .= surround_string           " Perform the replacement   &    execute "normal! gv" . replacement       #    " Restore the original register       let @" = reg_save       )    " Clear the register used for yanking       let @x = ''   endfunction    5��    e                      �                    �    d           >           �      >               �    d                      �              c      5�_�   	      
          d        ����                                                                                                                                                                                                                                                                                                                            d           �           V        d�s     �   c   e   �       5�5�_�                    d        ����                                                                                                                                                                                                                                                                                                                                                 V���    d�v    �   c   �        5��    c                      �      e              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V���    d��     �          c      $set termguicolors$5��                                                �                                                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V���    d��     �          c      $set termguicolors$5��                                                �                                                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        d��     �          c      iet termguicolors5��                                                5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                 V       d��     �          �      set termguicolors   4�          �      4   set termguicolors�                 4   set termguicolors   45��                                               �                                                  5�_�             	             ����                                                                                                                                                                                                                                                                                                                                                 v       d��     �          �      0set termguicolors05��                                                �                                                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v        d��     �          �      $set termguicolors$5��                                                �                                                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 v       d��     �          �      "set termguicolors"5��                                                �                                                  5��