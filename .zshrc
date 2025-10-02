# ~/.zshrc — configuration optimisée pour iTerm2 et Oh My Zsh
# Inspirée des recommandations de docs/iterm2_plugins.md

## Options du shell ---------------------------------------------------------
setopt auto_cd auto_pushd pushd_ignore_dups
setopt prompt_subst
setopt append_history extended_history hist_ignore_all_dups hist_reduce_blanks share_history
setopt extended_glob null_glob

## Chemins ------------------------------------------------------------------
typeset -gU path PATH fpath FPATH

if command -v brew >/dev/null 2>&1; then
  HOMEBREW_PREFIX="${HOMEBREW_PREFIX:-$(brew --prefix)}"
  path=(
    $HOMEBREW_PREFIX/bin
    $HOMEBREW_PREFIX/sbin
    $path
  )
  fpath=(
    $HOMEBREW_PREFIX/share/zsh/site-functions
    $fpath
  )
fi

path=(
  /usr/local/sbin
  "$HOME/.local/bin"
  "$HOME/.gem/bin"
  $path
)

export GEM_HOME="${GEM_HOME:-$HOME/.gem}"

## Node Version Manager -----------------------------------------------------
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
  # shellcheck source=/dev/null
  . "$NVM_DIR/nvm.sh"
fi

## Oh My Zsh ----------------------------------------------------------------
export ZSH="$HOME/.oh-my-zsh"

typeset -a plugins
plugins=(
  git
  bundler
  dotenv
  rake
  rbenv
  ruby
)

typeset -a missing_components
missing_components=()

# Toujours définir un thème par défaut reconnu par Oh My Zsh
ZSH_THEME="robbyrussell"

set_powerlevel10k_theme() {
  local p10k_dir
  for p10k_dir in "${ZSH_CUSTOM:-$ZSH/custom}/themes/powerlevel10k" "$ZSH/themes/powerlevel10k"; do
    if [[ -d $p10k_dir ]]; then
      ZSH_THEME="powerlevel10k/powerlevel10k"
      return
    fi
  done
  missing_components+=("thème powerlevel10k")
}

set_powerlevel10k_theme

add_optional_plugin() {
  local plugin="$1"
  local custom_dir="${ZSH_CUSTOM:-$ZSH/custom}/plugins/$plugin"
  local builtin_dir="$ZSH/plugins/$plugin"
  if [[ -d $custom_dir || -d $builtin_dir ]]; then
    plugins+=("$plugin")
  else
    missing_components+=("$plugin")
  fi
}

add_optional_plugin zsh-autosuggestions
add_optional_plugin zsh-syntax-highlighting
add_optional_plugin zsh-history-substring-search

if command -v fzf >/dev/null 2>&1 || [[ -d ${HOMEBREW_PREFIX:-}/opt/fzf ]]; then
  add_optional_plugin fzf
else
  missing_components+=("fzf (binaire)")
fi

# Options Oh My Zsh
DISABLE_AUTO_UPDATE="true"
DISABLE_UPDATE_PROMPT="true"
DISABLE_MAGIC_FUNCTIONS="true"
DISABLE_AUTO_TITLE="true"

source "$ZSH/oh-my-zsh.sh"

if (( ${#missing_components[@]} )); then
  (
    IFS=', '
    print -P "%F{yellow}[oh-my-zsh]%f Plugins, thèmes ou dépendances manquants : ${missing_components[*]}. Consultez docs/iterm2_plugins.md pour les installer."
  )
fi

## Prompt -------------------------------------------------------------------
POWERLEVEL10K_MODE="nerdfont-complete"
POWERLEVEL10K_PROMPT_CHAR_ON_HOST="$"
POWERLEVEL10K_RIGHT_PROMPT_ADD_NEWLINE=true
POWERLEVEL10K_LEFT_PROMPT_ADD_NEWLINE=false
DEFAULT_USER="$USER"

if [[ -r "${ZDOTDIR:-$HOME}/.p10k.zsh" ]]; then
  source "${ZDOTDIR:-$HOME}/.p10k.zsh"
else
  if [[ $ZSH_THEME == "powerlevel10k/powerlevel10k" ]]; then
    if command -v p10k >/dev/null 2>&1; then
      print -P "%F{yellow}Powerlevel10k est installé mais pas encore configuré. Lancez 'p10k configure' pour générer ~/.p10k.zsh.%f"
    else
      print -P "%F{yellow}Installez le thème Powerlevel10k pour accéder à la commande 'p10k configure'.%f"
    fi
  fi
fi

## Complétion ----------------------------------------------------------------
autoload -U +X compinit && compinit -C
autoload -U +X bashcompinit && bashcompinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}' 'r:|=*' 'l:|=* r:|=*'

## Couleurs ------------------------------------------------------------------
autoload -U colors && colors

## Raccourcis d'historique ---------------------------------------------------
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

## Outils complémentaires ---------------------------------------------------
if command -v thefuck >/dev/null 2>&1; then
  eval "$(thefuck --alias)"
fi

if command -v zoxide >/dev/null 2>&1; then
  eval "$(zoxide init zsh)"
elif command -v autojump >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    autojump_profile="$(brew --prefix)/etc/profile.d/autojump.sh"
    [ -r "$autojump_profile" ] && source "$autojump_profile"
  fi
fi

if command -v direnv >/dev/null 2>&1; then
  eval "$(direnv hook zsh)"
fi

if [[ -n ${HOMEBREW_PREFIX:-} ]]; then
  fzf_shell="$HOMEBREW_PREFIX/opt/fzf/shell"
  if [[ -d $fzf_shell ]]; then
    for script in "$fzf_shell"/key-bindings.zsh "$fzf_shell"/completion.zsh; do
      [[ -r $script ]] && source "$script"
    done
  fi
  if [[ -d "$HOMEBREW_PREFIX/etc/profile.d" ]]; then
    for script in "$HOMEBREW_PREFIX"/etc/profile.d/*.sh; do
      [[ -f $script && -r $script ]] || continue
      source "$script"
    done
  fi
fi

## Historique ---------------------------------------------------------------
HISTFILE="$HOME/.zsh_history"
HISTSIZE=100000
SAVEHIST=100000

## Éditeur & variables ------------------------------------------------------
export EDITOR="${EDITOR:-nvim}"
export VISUAL="${VISUAL:-$EDITOR}"
export LANG="${LANG:-fr_FR.UTF-8}"

if [[ $- == *i* ]]; then
  export EDITOR="code --wait"
fi

## Alias --------------------------------------------------------------------
alias vim="nvim"
alias grep="grep --color=auto"
alias less="less -R"
alias c="clear"
alias zshconfig="code ~/.zshrc"

if command -v eza >/dev/null 2>&1; then
  alias ls="eza"
  alias ll="eza -l --icons --git"
else
  alias ll="ls -la"
fi

if command -v batcat >/dev/null 2>&1; then
  alias cat="batcat"
elif command -v bat >/dev/null 2>&1; then
  alias cat="bat"
fi

## Fichiers locaux ----------------------------------------------------------
for extra_config in "$HOME/.zshrc.local" "$HOME/.aliases"; do
  [ -r "$extra_config" ] && source "$extra_config"
done

## Clés API -----------------------------------------------------------------
# Décommentez uniquement après avoir stocké vos secrets de manière sécurisée.
# export OPENAI_API_KEY="votre-cle-api"
