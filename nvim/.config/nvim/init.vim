let mapleader=","

set runtimepath+=~/.local/share/dein/repos/github.com/Shougo/dein.vim

if dein#load_state('~/.local/share/dein')
    call dein#begin('~/.local/share/dein')

    call dein#add('~/.local/share/dein/repos/github.com/Shougo/dein.vim')
    call dein#load_toml("~/.config/nvim/plugins.toml", {})

    call dein#end()
    call dein#save_state()
endif

if dein#check_install()
    call dein#install()
endif

filetype plugin indent on
syntax enable

set background=dark

" tmux, not sure if this is still necessary
set t_8f=[38;2;%lu;%lu;%lum
set t_8b=[48;2;%lu;%lu;%lum

" transparency
if !has("gui_running")
    highlight Normal ctermbg=NONE guibg=NONE
    highlight NonText ctermbg=NONE guibg=NONE
endif

set termguicolors
set lazyredraw

set number
set relativenumber

set expandtab
set tabstop=2
set shiftwidth=2
set shiftround
set smartindent
set textwidth=80
set list

set hidden

set scrolloff=2
set sidescrolloff=5

set shell=/usr/bin/fish

set splitbelow
set splitright
set equalalways

set confirm
set undofile

set ignorecase
set smartcase

set wildignore=*.o,*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
set wildmode=longest,list
set wildignorecase

noremap j gj
noremap k gk

nnoremap Y y$

nnoremap Q <nop>

cnoremap <C-A> <Home>
cnoremap <C-E> <End>

vnoremap < <gv
vnoremap > >gv

nnoremap <silent> <Leader>c :nohlsearch<CR>

nnoremap <Leader>bd :bdelete<CR>
nnoremap <Leader>bn :bnext<CR>
nnoremap <Leader>bp :bprev<CR>

" window management
nnoremap <A--> <C-W>S
nnoremap <silent> <A-_> :botright split<CR>
nnoremap <A-bar> <C-W>v
nnoremap <silent> <A-\> :vertical botright split<CR>

nnoremap <A-h> <C-W>h
nnoremap <A-j> <C-W>j
nnoremap <A-k> <C-W>k
nnoremap <A-l> <C-W>l

" resume position
augroup LastPosition
    autocmd! BufReadPost *
                \ if line("'\"") > 0 && line("'\"") <= line("$") |
                \   exe "normal! g`\"" |
                \ endif
augroup END
