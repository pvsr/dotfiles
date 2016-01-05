ZSH=/usr/share/oh-my-zsh/
ZSH_THEME="jreese"
HYPHEN_INSENSITIVE="true"
DISABLE_AUTO_UPDATE="true"
ENABLE_CORRECTION="true"
DISABLE_UNTRACKED_FILES_DIRTY="true"

plugins=(archlinux autojump common-aliases git sudo systemd vi-mode)

export BROWSER="qutebrowser"
export EDITOR="et"
export PATH=$HOME/bin:/usr/local/bin:$HOME/.cabal/bin:$PATH

alias et='emacsclient -t -a "" "$@"'
alias em='emacsclient -c -n -a "" "$@"'

ZSH_CACHE_DIR=$HOME/.oh-my-zsh-cache
if [[ ! -d $ZSH_CACHE_DIR ]]; then
  mkdir $ZSH_CACHE_DIR
fi

source $ZSH/oh-my-zsh.sh

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
