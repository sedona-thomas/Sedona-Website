#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#""""""""""""""""""""" Zsh Configuration """"""""""""""""""""""""""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#""""""""""""""""""""""""""""" Anaconda """""""""""""""""""""""""""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
conda_location="/usr/local/anaconda3"
__conda_setup="$('/usr/local/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$conda_location/etc/profile.d/conda.sh" ]; then
        . "$conda_location/etc/profile.d/conda.sh"
    else
        export PATH="$conda_location/bin:$PATH"
    fi
fi
unset conda_location
unset __conda_setup
# <<< conda initialize <<<


#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""""""""""""""""""""""""""""" Main """"""""""""""""""""""""""""""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# variables
current_user="sedonathomas"
current_os="darwin"

# gets aliases
if [ -f ~/.zsh_aliases ]; then
    . ~/.zsh_aliases
fi

# sets default text editor
export EDITOR=vim
export VISUAL=vim

# sets colors
export TERM=xterm-256color tput colors

# list with colors
export CLICOLOR=1

# fixed PATH variable
export PATH="/usr/local/sbin:$PATH"

# if not running interactively (PS1 is NULL), quit
[ -z "$PS1" ] && return

# unique history without space
HISTCONTROL=ignoredups:ignorespace

# set vi editing mode
set -o vi





#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#""""""""""""""""""""""""""""" Prompt Settings """"""""""""""""""""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Default prompt
# PS1="%n@%m %1~ %# "

# change prompt colors
# syntax: http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html#Visual-effects
# colors: https://jonasjacek.github.io/colors/
# PROMPT='%F{blue}%n%f@%F{cyan}%m%f %1~ %# '

# username@hostname pwd_path current_folder time %
PROMPT=''
PROMPT+='%F{12}%6>>%n%<<'         # username, %6>> << = truncates 6 chars
PROMPT+='%f@'                     # @
PROMPT+='%F{12}%1>>%m%<< '        # hosname, %1>> << = truncates 1 char
PROMPT+='%F{4}%d '                # current working directory path
PROMPT+='%f%B%1~%b '              # working directory with 1 item
PROMPT+='%F{19}%t '               # time
PROMPT+='%f'
PROMPT+='%# '                     # \n%

# command line spell checker
setopt correct
export SPROMPT="Correct $fg[red]%R$reset_color to $fg[green]%r$reset_color? [Yes, No, Abort, Edit] "
#autoload U colors && colors

# colored GCC warnings and errors
export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""""""""""""""""""""""""" Homebrew Add-Ons """"""""""""""""""""""""
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# enables thefuck
#eval $(thefuck --alias)
# enables syntax highlighting
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

unset current_user
unset current_os
