set termguicolors

"kj to esc
imap kj <Esc>

"tab to 4 spaces
set tabstop=4 softtabstop=0 expandtab shiftwidth=4 smarttab

"copy from and to clipboard
vnoremap <C-c> "*y :let @+=@*<CR>
map <C-S-v> "+p

"set toggle spellcheck
map <F6> :setlocal spell! spelllang=en_us<CR>

"show line numbers
set number

"enable mouse
set mouse=a

"Smartcase search
set ignorecase
set smartcase

set hidden
set mouse=a

"H to start of line end L to end of line
map H ^
map L $

"keep cursor in middle
:set so=999
nnoremap <Leader>zz :let &scrolloff=999-&scrolloff<CR>

set autoread
"Use a line cursor within insert mode and a block cursor everywhere else.

" Reference 
" Ps = 0 -> blinking block
" Ps = 1 -> blinking block (default)
" Ps = 2 -> steady block 
" Ps = 3 -> blinking underline 
" Ps = 4 -> steady underline 
" Ps = 5 -> blinking bar (xterm)
" Ps = 6 -> steady bar (xterm)
let &t_SI = "\e[5 q"
let &t_EI = "\e[2 q"

set undofile " Maintain undo history between sessions
set undodir=~/.vim/undodir

"highlight search matches
set hlsearch

"autosave on change
" autocmd TextChanged,TextChangedI <buffer> silent write

"Ctrl+s to save
noremap <silent> <C-S>          :update<CR>
vnoremap <silent> <C-S>         <C-C>:update<CR>
inoremap <silent> <C-S>         <C-O>:update<CR>

"Wrap
set wrap
map <C-w> :set wrap!<CR>

"don't skip _ in word movement
set iskeyword-=_

" reload vimrc
map <F5> :source ~/.vimrc<CR>

" vimwiki prereq
set nocompatible
filetype plugin on
syntax on

"disable beeping
set noerrorbells visualbell t_vb=
autocmd GUIEnter * set visualbell t_vb=

"wrap 
set wrap linebreak

" Search for selected text, forwards or backwards.
vnoremap <silent> * :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy/<C-R>=&ic?'\c':'\C'<CR><C-R><C-R>=substitute(
  \escape(@", '/\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gVzv:call setreg('"', old_reg, old_regtype)<CR>
vnoremap <silent> # :<C-U>
  \let old_reg=getreg('"')<Bar>let old_regtype=getregtype('"')<CR>
  \gvy?<C-R>=&ic?'\c':'\C'<CR><C-R><C-R>=substitute(
  \escape(@", '?\.*$^~['), '\_s\+', '\\_s\\+', 'g')<CR><CR>
  \gVzv:call setreg('"', old_reg, old_regtype)<CR>

autocmd BufNewFile,BufRead * setlocal formatoptions=

