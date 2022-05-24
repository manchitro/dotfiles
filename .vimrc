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

"enable mouse
:set mouse=a

"syntax highlighting
:set syntax=on

"Smartcase search
:set ignorecase
:set smartcase

:set hidden
:set mouse=a

"H to start of line end L to end of line
:map H ^
:map L $

"plugins
call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
call plug#end()
