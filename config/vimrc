"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Main Settings                                                         "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


" When started as "evim", evim.vim will already have done these settings.
if v:progname =~? "evim"
  finish
endif

" Get the defaults that most users want.
source $VIMRUNTIME/defaults.vim

if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file (restore to previous version)
  if has('persistent_undo')
    set undofile	" keep an undo file (undo changes after closing)
  endif
endif

if &t_Co > 2 || has("gui_running")
  " Switch on highlighting the last used search pattern.
  set hlsearch
endif

" Only do this part when compiled with support for autocommands.
if has("autocmd")

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
  autocmd FileType text setlocal textwidth=78

  augroup END

else

  set autoindent		" always set autoindenting on

endif " has("autocmd")

" Add optional packages.
"
" The matchit plugin makes the % command work better, but it is not backwards
" compatible.
" The ! means the package won't be loaded right away but when plugins are
" loaded during initialization.
if has('syntax') && has('eval')
  packadd! matchit
endif



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Start of manually added settings from Jae's Vim settings              "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


" Line numbers
set number

" Buffer switching using Cmd-arrows in Mac and Alt-arrows in Linux
:nnoremap <D-Right> :bnext<CR>
:nnoremap <M-Right> :bnext<CR>
:nnoremap <D-Left> :bprevious<CR>
:nnoremap <M-Left> :bprevious<CR>
" and don't let MacVim remap them
if has("gui_macvim")
   let macvim_skip_cmd_opt_movement = 1
endif


" When coding, auto-indent by 4 spaces, just like in K&R
" Note that this does NOT change tab into 4 spaces
" You can do that with "set tabstop=4", which is a BAD idea
set shiftwidth=4

" Always replace tab with 8 spaces, except for makefiles
set expandtab
autocmd FileType make setlocal noexpandtab


" My settings when editing *.txt files
"   - automatically indent lines according to previous lines
"   - replace tab with 8 spaces
"   - when I hit tab key, move 2 spaces instead of 8
"   - wrap text if I go longer than 76 columns
"   - check spelling
autocmd FileType text setlocal autoindent expandtab softtabstop=2 textwidth=76 spell spelllang=en_us


" Don't do spell-checking on Vim help files
autocmd FileType help setlocal nospell

" Prepend ~/.backup to backupdir so that Vim will look for that directory before littering the current dir with backups.
" You need to do "mkdir ~/.backup" for this to work.
set backupdir^=~/.backup


" Also use ~/.backup for swap files. The trailing // tells Vim to incorporate full path into swap file names.
set dir^=~/.backup//


" Ignore case when searching
" - override this setting by tacking on \c or \C to your search term to make
"   your search always case-insensitive or case-sensitive, respectively.
set ignorecase



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Start of my own manually added settings                               "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


set undofile
set undodir=/~/.undo_backup//

" Enable highlighting of misspelled terms
" set spell


"""""""""""""""""""""""""
" Statusline formatting "
"""""""""""""""""""""""""

" Keeps statusline on screen
set laststatus=2

" Current Mode
let g:currentmode={'n' : 'Normal', 'v' : 'Visual', 'V' : 'V·Line', '' : 'V·Block', 'i' : 'Insert', 'R' : 'R', 'Rv' : 'V·Replace', 'c' : 'Command'}

set statusline=
set statusline+=%y                             " type of file in buffer
set statusline+=\ %F                           " full file path
set statusline+=\ \[%{&fileformat}\]           " file format
set statusline+=\ \[%M\]                       " change marker
set statusline+=\ \[%{g:currentmode[mode()]}\] "current mode
set statusline+=%=                             " align right
set statusline+=\ Line:%l/%L                   " line / total lines
set statusline+=\ %3p%%                        " percent of lines
set statusline+=\ Col:%c                       " current column
set statusline+=\ Buf:%n                       " buffer number


"""""""""""""""""""""
" Syntax Appearance "
"""""""""""""""""""""

" Syntax highlighting
set term=xterm-256color
syntax on

" Set syntax highlighting color scheme
" List color schemes: "ls -l /usr/share/vim/vim*/colors/"
colorscheme Sedona_vim_colors

set tabstop=4

"hi CursorLine guibg=#808080 ctermbg=244 term=underline
"au InsertEnter * set cursorline
"au InsertLeave * set nocursorline
"hi statusline guifg=#808080 ctermfg=244 guibg=#ffffff ctermbg=15

" Highlight current line and column
set cursorline
set cursorcolumn
" Show the cursor position
set ruler
" Show the current mode
set showmode
" Show the filename in the window titlebar
set title
" Show the (partial) command as it’s being typed
set showcmd
" Set spell checking
set spell spelllang=en
set spellfile=~/.vim/spell/en.utf-8.add
" Enables command suggestion menu
set wildmenu
"set wildmode=list:longest,full
" Turns on error bells
set errorbells
" Confirm when closing an unsaved file
set confirm
" Highlights search
set hlsearch
" Automatically write when switching buffers
set autowrite
" Displays current file as title
set titlestring=%t
set title

