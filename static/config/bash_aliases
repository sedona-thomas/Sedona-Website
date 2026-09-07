#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#"""""""""""""""""""""""" Bash Aliases """""""""""""""""""""""""""""
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#""""""""""""""""""""""""""""
#"""""""""" Main """"""""""""
#""""""""""""""""""""""""""""

# variables
website="http://www.columbia.edu/~snt2127"
UNI="snt2127"
current_user="sedonathomas"
current_os="darwin"
my_shell="bash"

# ssh
alias cunix="ssh $UNI@cunix.columbia.edu"
alias clic="ssh $UNI@clic.cs.columbia.edu"
alias clac="ssh $UNI@clac.cs.columbia.edu"

# main system
alias reset="reset && clear"
if [[ $my_shell == "zsh" ]]; then
    alias restart="source ~/.zshrc"
elif [[ $my_shell == "bash" ]]; then
    alias restart="source ~/.bashrc"
fi
alias diff="colordiff"
alias special_diff='diff -y --suppress-common-lines --width=250'
alias like="apropos"
alias rm='rm -iv'
alias cp='cp -iv'
alias mv='mv -iv'
alias special_tree='tree -RapugD --si --du'

# files
if [[ $OSTYPE == *"darwin"* ]]; then
    alias restart_finder='killall Finder /System/Library/CoreServices/Finder.app'
    alias show_files='defaults write com.apple.finder AppleShowAllFiles YES; restart_finder'
    alias hide_files='defaults write com.apple.finder AppleShowAllFiles NO; restart_finder'
fi

# config files
alias fix_zsh="vim ~/.zshrc ~/.zsh_aliases"
alias fix_zshrc="vim ~/.zshrc"
alias fix_zsh_aliases="vim ~/.zsh_aliases"
alias fix_bash="vim ~/.bashrc ~/.bash_aliases"
alias fix_bashrc="vim ~/.bashrc"
alias fix_bash_aliases="vim ~/.bash_aliases"
alias fix_aliases="vim ~/.zsh_aliases ~/.bash_aliases"
alias fix_vimrc="vim ~/.vimrc"


#"""""""""""""""""""""""""""""
#"""""""""" Generic """"""""""
#"""""""""""""""""""""""""""""

# navigation shortcuts
alias up="cd .."
alias p1="cd part1"
alias p2="cd part2"
alias p3="cd part3"
alias p4="cd part4"
alias p5="cd part5"
alias q1="cd q1"
alias q2="cd q2"
alias q3="cd q3"
alias q4="cd q4"
alias q5="cd q5"

# ls aliases
if [[ $OSTYPE == *"linux"* ]]; then
	alias ls='ls              --color=auto'
    alias ls='ls     -1       --color=auto' #one output per line
    alias ll="ls     -alF     --color=auto"
    alias lh='ls     -lah     --color=auto'
    alias la="ls     -A       --color=auto"
    alias laf="ls    -aF      --color=auto"
    alias l="ls      -CF      --color=auto"
    alias ls_all="ls -1ahlACF --color=auto"
elif [[ $OSTYPE == *"darwin"* ]]; then
	alias ls='ls     -G'
    alias ls='ls     -1G' #one output per line
    alias ll="ls     -alFG"
    alias lh='ls     -lahG'
    alias la="ls     -AG"
    alias laf="ls    -aFG"
    alias l="ls      -CFG"
    alias ls_all="ls -1ahlACFG"
fi


# main
if [[ $OSTYPE == *"linux"* ]]; then
    alias dmesg='dmesg   --color'
    alias pacman='pacman --color=auto'
fi
alias grep="grep   --color=auto"
alias egrep="egrep --color=auto"
alias fgrep="fgrep --color=auto"
alias gccg='gcc -g -Wall'
alias g++g='g++ -g -Wall'
alias valgrindlc='valgrind --leak-check=yes'

# vim  
alias RM="vim            ./README.txt"
alias MF="vim            ./Makefile"
alias open_all="vim      ./*"
alias open_all_sh="vim   ./*.sh"
alias open_all_c="vim    ./*.c"
alias open_all_h="vim    ./*.h"
alias open_all_py="vim   ./*.py"
alias open_all_java="vim ./*.java"
alias open_all_txt="vim  ./*.txt"
alias open_all_ch="vim   ./*.c *.h"

# git
alias git_diff="git diff --color"           # difference between working file and staging area
alias git_diff_s="git_diff"                 # difference between working file and staging area
alias git_diff_c="git_diff --cached"        # difference between staging area and last commit
alias git_log="git log --color"             # log of repository changes
alias git_log_s="git_log --stat --summary"  # log with short summary of changes
alias git_log_l="git_log -p"                # log with long summary of changes
alias git_log_clone="git_log origin.."      # clone log of repository changes
alias git_log_s_clone="git_log_s origin.."  # clone log with short summary of changes
alias git_log_l_clone="git_log -p origin.." # clone log with long summary of changes

#"""""""""""""""""""""""""""""
#""""""""" Personal """"""""""
#"""""""""""""""""""""""""""""

# copy file templates
alias cpC="wget    $website/templates/template.c"
alias cpH="wget    $website/templates/template.c"
alias cpMF="wget   $website/templates/MakefileTemplate"
alias cpSH="wget   $website/templates/template.sh"
alias cpHTML="wget $website/templates/template.HTML"
alias cpCSS="wget  $website/templates/template.CSS"
alias cpJAVA="wget $website/templates/template.java"
alias cpPY="wget   $website/templates/template.py"
alias cpS="wget    $website/templates/template.s"

#""""""""""""""""""""""""""""""
#""""" Personal Computer """"""
#""""""""""""""""""""""""""""""

if [[ $USER == $current_user ]] && [[ $OSTYPE == *$current_os* ]]; then

    # navigation
    alias dl="cd    ~/Downloads/"
    alias term="cd  ~/Terminal/"
    alias ss="cd    ~/Terminal/Shell\ Scripts/"
    alias home="cd  ~"
    alias wf="cd    ~/Workflows/"
    alias sc_sh="cd ~/Workflows/Screenshots/"
    alias temp="cd  ~/temp/"
    alias tmp="cd   ~/temp/"
    alias ED="cd    /Volumes/"
    alias external_drive="cd /Volumes/"

    if [ -d ~/OneDrive ]; then
        
        # OneDrive variables
        cs=" ~/OneDrive/Documents/Computer\ Science"
        
        # OneDrive
        alias od="cd        ~/OneDrive"
        alias od_doc="cd    ~/OneDrive/Documents/"
        alias edu="cd       ~/OneDrive/Documents/Education"
        alias col="cd        ~/OneDrive/Documents/Education/College"
        alias CS="cd        $cs"
        alias CP="cd        $cs/Codepath"
        alias od_ss="cd     $cs/Shell\ Scripts"
        alias CLAC="cd      $cs/Terminal/CLAC"
        alias templates="cd $cs/templates"

        # ssh
        alias ssh_auto_login="$cs/Shell\ Scripts/ssh/ssh_auto_login.sh"

        # update all
        alias ud_all="ud_all_files; ud_all_software; ud_all_cunix; ud_all_templates"
        alias ud_all_files="ud_ss; ud_rc; ud_wf"
        alias ud_all_software="ud_brew; ud_conda"
        alias ud_all_cunix="ud_cunix_rc; ud_cunix_templates; ud_cunix_ss; ud_cunix_resume"
        alias ud_all_rc="ud_rc; ud_cunix_rc"
        alias ud_all_ss="ud_ss; ud_cunix_ss"
        alias ud_all_templates="ud_cunix_templates; clac '~/shell_scripts/update_templates.sh'"
        
        # files
        alias ud_ss="$cs/Shell\ Scripts/update/update_shell_scripts.sh"
        alias ud_rc="$cs/Shell\ Scripts/update/update_rc.sh"
        alias ud_wf="$cs/Shell\ Scripts/update/update_workflows.sh"
        
        # software
        alias ud_conda="conda update conda"
        alias ud_brew='brew update && brew upgrade && brew doctor'
        alias cl_brew="$cs/Shell\ Scripts/software/clean_homebrew.sh"

        # cunix
        alias ud_cunix_rc="$cs/Shell\ Scripts/cunix/update_cunix_config.sh"
        alias ud_cunix_templates="$cs/Shell\ Scripts/cunix/update_cunix_templates.sh"
        alias ud_cunix_ss="$cs/Shell\ Scripts/cunix/update_cunix_shell_scripts.sh"
        alias ud_cunix_resume="$cs/Shell\ Scripts/cunix/update_cunix_resume.sh"
        
        # download/upload
        alias dl_rc="$cs/Shell\ Scripts/config/download_rc.sh"
        alias ul_rc="$cs/Shell\ Scripts/config/upload_rc.sh"
        alias dl_wf="$cs/Shell\ Scripts/workflows/download_workflows.sh"
        alias ul_wf="$cs/Shell\ Scripts/workflows/upload_workflows.sh"
        alias dl_cunix="$cs/Shell\ Scripts/cunix/copy_cunix.sh"
        alias cp_cunix="$cs/Shell\ Scripts/cunix/copy_cunix.sh"
        
        # uninstall
        alias ui_anaconda="$cs/Shell\ Scripts/software/uninstall_anaconda.sh"

    fi

    # Read-Evaluate-Print-Loop
    alias C_repl="~/Terminal/'C REPL'/igcc-0.2/igcc"
    alias py_repl="python"
    alias java_repl="jshell"

fi

#""""""""""""""""""""""""""""
#""""" Unset Variables """"""
#""""""""""""""""""""""""""""
unset website
unset UNI
unset current_user
unset current_os
unset shell
