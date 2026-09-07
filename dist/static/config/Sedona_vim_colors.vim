" local syntax file - set colors on a per-machine basis:
" vim: tw=0 ts=4 sw=4
" Vim color file
" Maintainer: Sedona Thomas
" Last Change: 09/23/2020

set background=light
hi clear
if exists("syntax_on")
  syntax reset
endif

let colors_name = "Sedona_vim_colors"

" Color Names: https://jonasjacek.github.io/colors/


" Main:
" color: black/white
hi Normal         guifg=#000000 ctermfg=0   guibg=#ffffff ctermbg=15 gui=NONE cterm=NONE
" color: black/grey
hi NonText        guifg=#000000 ctermfg=0   guibg=#c6c6c6 ctermbg=251 gui=NONE cterm=NONE
" color: grey/white
hi comment        guifg=#9e9e9e ctermfg=247 guibg=#ffffff ctermbg=15 gui=NONE cterm=NONE
"color: black
hi LineNr         guifg=#000000 ctermfg=0 gui=NONE cterm=NONE


" Constant Values:
" color: blue
hi constant       guifg=#005fff ctermfg=27 gui=NONE cterm=NONE
" color: green
hi string         guifg=#00af00 ctermfg=34 gui=NONE cterm=NONE
" color: red
hi character      guifg=#ff0000 ctermfg=9 gui=NONE cterm=NONE
" color: maroon
hi number         guifg=#800000 ctermfg=1 gui=NONE cterm=NONE
" color: maroon
hi float          guifg=#800000 ctermfg=1 gui=NONE cterm=NONE
" color: purple
hi boolean        guifg=#800080 ctermfg=5 gui=NONE cterm=NONE


" Variable Names:
" color: black
hi identifier     guifg=#000000 ctermfg=0   gui=NONE cterm=NONE
hi function       guifg=#000000 ctermfg=0   gui=NONE cterm=NONE


" Statements:
" color: blue
hi statement      guifg=#0000ff ctermfg=12 gui=NONE cterm=NONE
" if, else, ...
hi conditional    guifg=#0000ff ctermfg=12 gui=NONE cterm=NONE
" for, while, do, ...
hi repeat         guifg=#0000ff ctermfg=12 gui=NONE cterm=NONE
" =, *, sizeof, ...
hi operator       guifg=#000000 ctermfg=0 gui=NONE cterm=NONE
hi keyword        guifg=#0000ff ctermfg=12 gui=NONE cterm=NONE
" try, catch, throw
" color: dark magenta
hi exception      guifg=#870087 ctermfg=90 gui=NONE cterm=NONE


" Preprocessor:
" color: fuchsia
hi preproc        guifg=#ff00ff ctermfg=13 gui=NONE cterm=NONE
" #include
hi include        guifg=#ff00ff ctermfg=13 gui=NONE cterm=NONE
" #define
hi define         guifg=#ff00ff ctermfg=13 gui=NONE cterm=NONE
hi macro          guifg=#ff00ff ctermfg=13 gui=NONE cterm=NONE
" #if, #else, etc
hi precondit      guifg=#ff00ff ctermfg=13 gui=NONE cterm=NONE


" Types:
" color: dark green
hi type           guifg=#005f00 ctermfg=22 gui=NONE cterm=NONE
hi StorageClass   guifg=#008700 ctermfg=28 gui=NONE cterm=NONE
hi Structure      guifg=#008700 ctermfg=28 gui=NONE cterm=NONE
hi Typedef        guifg=#005f00 ctermfg=22 gui=NONE cterm=NONE


" Special Symbols:
" color: black
hi special        guifg=#000000 ctermfg=0 gui=NONE cterm=NONE
hi specialchar    guifg=#000000 ctermfg=0 gui=NONE cterm=NONE
hi tag            guifg=#000000 ctermfg=0 gui=NONE cterm=NONE
hi specialcomment guifg=#000000 ctermfg=0 gui=NONE cterm=NONE
hi debug          guifg=#000000 ctermfg=0 gui=NONE cterm=NONE


" Messages:
" color: black/red
hi Error          guifg=#000000 ctermfg=0   guibg=#ff0000 ctermbg=9 gui=NONE cterm=NONE
hi ErrorMsg       guifg=#000000 ctermfg=0   guibg=#ff0000 ctermbg=9 gui=NONE cterm=NONE
hi WarningMsg     guifg=#000000 ctermfg=0   guibg=#ff0000 ctermbg=9 gui=NONE cterm=NONE


" Notes:
" color: black/orange
hi Todo           guifg=#000000 ctermfg=0   guibg=#d78700 ctermbg=172 gui=NONE cterm=NONE


" Underlined Text:
" color: highlighter yellow
hi underlined     guibg=#c0c0c0 ctermbg=7 gui=NONE cterm=NONE

" Cursor:
" color: sea green/lime
hi Cursor         guibg=#5fd787 ctermbg=78  guifg=#00ff00 ctermfg=10 gui=NONE cterm=NONE
" highlights current line
" color: grey
hi CursorLine     guibg=#808080 ctermbg=244 term=underline gui=underline cterm=underline


" StatusLine:
" color: black/white
hi StatusLine     guibg=#000000 ctermbg=0   guifg=#ffffff ctermfg=15 gui=NONE cterm=NONE
" color: light blue/navy blue
hi StatusLineNC	  guifg=#00afff ctermfg=39  guibg=#00005f ctermbg=17 gui=NONE cterm=NONE


" Search:
" color: highlighter yellow/pastel blue
hi Search         guibg=#ffff00 ctermbg=11 guifg=#000000 ctermfg=0 gui=bold cterm=bold
hi IncSearch      guibg=#5f87af ctermbg=67 gui=NONE cterm=NONE


" Formatting:
" color: dark grey
hi title          guifg=#444444 ctermfg=238
" color: cyan/sky blue
hi ShowMarksHL    guifg=#00ffff ctermfg=51  guibg=#00afff ctermbg=39 gui=bold cterm=bold
" color: gold
hi label          guifg=#ffd700 ctermfg=220


" Unsure:
" color: dark green
hi DiffChange     guibg=#005f00 ctermbg=22
" color: olive
hi DiffText       guibg=#808000 ctermbg=3
" color: bright purple
hi DiffAdd        guibg=#875fff ctermbg=99
" color: coral pink
hi DiffDelete     guibg=#ff8787 ctermbg=210
" color: gray/white
hi Folded         guibg=#4e4e4e ctermbg=239
hi FoldColumn     guibg=#4e4e4e ctermbg=239 guifg=#ffffff ctermfg=15

