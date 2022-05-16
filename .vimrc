"kj to esc
:imap kj <Esc>

"tab to 4 spaces
set tabstop=4 softtabstop=0 expandtab shiftwidth=4 smarttab

"copy from and to clipboard
vnoremap <C-c> "*y :let @+=@*<CR>
map <C-S-v> "+p"

"set toggle spellcheck
map <F6> :setlocal spell! spelllang=en_us<CR>

"show line numbers
:set number

"Smartcase search
:set ignorecase
:set smartcase

:set hidden
:set mouse=a

"H to start of line end L to end of line
:map H ^
:map L $

"exit visual mode with kj
:xnoremap kj <Esc>
