"
" vimrc
" vim configuration file
"


"
" Vundle Package Manager
"
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'gmarik/Vundle.vim'
Plugin 'tmhedberg/SimpylFold'
Plugin 'vim-scripts/indentpython.vim'
"Plugin 'scrooloose/syntastic'
Plugin 'nvie/vim-flake8'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-airline/vim-airline'
Plugin 'tpope/vim-fugitive'

call vundle#end()            " required
filetype plugin indent on    " required

"
" Navigation
"
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>


"
" Spaces & Tabs
"
set tabstop=4                   " number of visual spaces per tab
set shiftwidth=4
set softtabstop=4               " number of spaces in tab when editing
set expandtab                   " tabs are visual spaces


"
" UI Config
"
set bg=dark                     " dark backgrounmd, light foreground
set t_md=                       " disable bold fontface
"set number                      " show line numbers
set ruler                       " show line and column numbers
"set showcmd                     " show command in bottom bar
set cursorline                  " highlight current line
set wildmenu                    " visual autocomplete for command menu
set showmatch                   " highlight matching [{()}]
set backspace=indent,eol,start  " allow bksp in diff. cursor positions
filetype indent on              " load filetype-specific indent files
syntax enable                   " enable syntax color/processing
colorscheme slate               " Nice yellow and red colors on black screen

" statusline
set laststatus=2                " always display status bar
set statusline=\ %f%m%r%h%w\ %=%({%{&ff}\|%{(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\")}%k\|%Y}%)\ %([%v:%l/%L][%p%%]\ %)


"
" Search
"
set incsearch                   " search as chars are entered
set hlsearch                    " highlight matches
nnoremap <C-/> :/\s\+$


"
" Code Folding
"
set foldmethod=indent
set foldlevel=99


"
" Misc Utilities
"

" Paste toggle kemap
nnoremap <F2> :set invpaste paste?<CR>
set pastetoggle=<F2>
set showmode

" Set visual column delimiter
if exists('+colorcolumn')
    " Use the newer slick looking vertiacal line
    set colorcolumn=79
else
    " Use the ugly text highlight
    au BufWinEnter * let w:m2=matchadd('ErrorMsg', '\%>79v.\+', -1)
endif

" Remove all trailing whitespace
fun! TrimWhitespace()
    let l:save = winsaveview()
    %s/\s\+$//e
    call winrestview(l:save)
endfun
command! TrimWhitespace call TrimWhitespace()

" Python PEP-8
au BufNewFile,BufRead *.py
    \ set tabstop=4
    \ softtabstop=4
    \ shiftwidth=4
    \ textwidth=79
    \ expandtab
    \ autoindent
    \ fileformat=unix


set noshowmode              " don't disply current mode (insert/visual)


"
" References
"
" Vundle & Python: https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/
" Remove trailing whitespace: https://vi.stackexchange.com/a/456
