"kj to esc
imap kj <Esc>

"tab to 4 spaces
set tabstop=4 softtabstop=0 expandtab shiftwidth=4 smarttab

"copy from and to clipboard
vnoremap <C-c> "*y :let @+=@*<CR>
map <C-S-v> "+p"

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

"plugins
call plug#begin('~/.vim/plugged')
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    Plug 'preservim/nerdtree'
    Plug 'mhinz/vim-startify'
call plug#end()

"keep cursor in middle
:set so=999
nnoremap <Leader>zz :let &scrolloff=999-&scrolloff<CR>

" these lines are needed for ToggleComment()
autocmd FileType c,cpp,java      let b:comment_leader = '//'
autocmd FileType arduino         let b:comment_leader = '//'
autocmd FileType sh,ruby,python  let b:comment_leader = '#'
autocmd FileType zsh             let b:comment_leader = '#'
autocmd FileType conf,fstab      let b:comment_leader = '#'
autocmd FileType matlab,tex      let b:comment_leader = '%'
autocmd FileType vim             let b:comment_leader = '"'

" l:pos   --> cursor position
" l:space --> how many spaces we will use b:comment_leader + ' '

function! ToggleComment()
    if exists('b:comment_leader')
        let l:pos = col('.')
        let l:space = ( &ft =~ '\v(c|cpp|java|arduino)' ? '3' : '2' )
        if getline('.') =~ '\v(\s*|\t*)' .b:comment_leader
            let l:space -= ( getline('.') =~ '\v.*\zs' . b:comment_leader . '(\s+|\t+)@!' ?  1 : 0 )
            execute 'silent s,\v^(\s*|\t*)\zs' .b:comment_leader.'[ ]?,,g'
            let l:pos -= l:space
        else
            exec 'normal! 0i' .b:comment_leader .' '
            let l:pos += l:space
        endif
        call cursor(line("."), l:pos)
    else
        echo 'no comment leader found for filetype'
    end
endfunction

nnoremap <C-_> :call ToggleComment()<CR>
inoremap <C-_> <C-o>:call ToggleComment()<CR>
xnoremap <C-_> :'<,'>call ToggleComment()<CR>

