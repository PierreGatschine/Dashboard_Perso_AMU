# Optimiser iTerm2 avec des plugins et extensions

Même si iTerm2 ne dispose pas d'un gestionnaire de plugins officiel, il s'intègre parfaitement à l'écosystème Zsh/Oh My Zsh et à divers utilitaires CLI. Cette fiche récapitule les outils recommandés pour macOS 13 (Ventura) tout en indiquant les ajustements utiles si vous devez encore maintenir macOS 12.

## Compatibilité macOS 13 (Ventura)

macOS 13 est encore supporté activement par Apple et Homebrew : la plate‑forme est classée *Tier 2* par Homebrew, ce qui signifie que les rapports de bugs sont acceptés et que les formules critiques restent maintenues. Avant d'ajouter de nouveaux plugins ou extensions :

1. **Appliquez les mises à jour système** : `softwareupdate --install --all`.
2. **Actualisez Homebrew** : `brew update && brew upgrade && brew cleanup`.
3. **Installez les dépendances de base** : police Nerd Font (ex. `brew install --cask font-meslo-lg-nerd-font`), `git`, `curl`, et `openssl@3` si nécessaire.
4. **Vérifiez l'architecture** (`arm64` vs `x86_64`) avec `uname -m` afin de pointer les chemins Homebrew (`/opt/homebrew` sur Apple Silicon, `/usr/local` sur Intel).

> 💡 Vous migrez depuis macOS 12 ? Gardez l'annexe [« Gérer les avertissements Homebrew »](#annexe--gérer-les-avertissements-homebrew) pour identifier les formules obsolètes encore présentes sur votre système.

## Plugins Zsh incontournables (compatibles macOS 13)

| Plugin | Source | Bénéfices principaux |
| --- | --- | --- |
| `zsh-autosuggestions` | [zsh-users/zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions) | Affiche des suggestions basées sur l'historique au fur et à mesure de la frappe. |
| `zsh-syntax-highlighting` | [zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting) | Coloration syntaxique avant exécution pour repérer les erreurs. |
| `zsh-history-substring-search` | [zsh-users/zsh-history-substring-search](https://github.com/zsh-users/zsh-history-substring-search) | Recherche dans l'historique à partir d'un fragment de commande. |
| `powerlevel10k` (thème) | [romkatv/powerlevel10k](https://github.com/romkatv/powerlevel10k) | Invite ultra-rapide, personnalisable et riche en informations. |

### Installation rapide avec Oh My Zsh

```bash
# Autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Syntax highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# History substring search
git clone https://github.com/zsh-users/zsh-history-substring-search \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search

# Thème Powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k
```

Ajoutez ensuite les plugins dans la ligne `plugins=(...)` de votre `.zshrc`, par exemple :

```zsh
plugins=(git bundler dotenv rake rbenv ruby \
  zsh-autosuggestions zsh-syntax-highlighting zsh-history-substring-search)
ZSH_THEME="powerlevel10k/powerlevel10k"
```

> ℹ️ **Astuce** : si votre `.zshrc` affiche un message comme `[oh-my-zsh] Plugins, thèmes ou dépendances manquants`, c'est qu'un composant n'est pas encore installé (plugin, thème Powerlevel10k, binaire `fzf`, etc.). Clonez le dépôt correspondant dans `${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/` ou `${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/`, installez l'outil requis (ex. `brew install fzf`) puis relancez votre terminal.

## Outils complémentaires utiles dans iTerm2 (macOS 13)

| Outil | Description | Installation |
| --- | --- | --- |
| `fzf` | Fuzzy finder pour rechercher fichiers, commandes et historique. | `brew install fzf` puis `$(brew --prefix)/opt/fzf/install` |
| `autojump` ou `zoxide` | Navigation ultra-rapide entre dossiers fréquents. | `brew install autojump` ou `brew install zoxide` |
| `thefuck` | Suggère une correction après une commande erronée. | `brew install thefuck` et ajouter `eval "$(thefuck --alias)"` au `.zshrc`. |
| `bat` | Version améliorée de `cat` avec coloration. | `brew install bat` puis alias `alias cat="bat"` si souhaité. |
| `eza` (successeur de `exa`) | `ls` moderne avec couleurs, icônes et arbres. | `brew install eza` puis `alias ls="eza"` ou `alias ll="eza -l --icons"`. |
| `fd` | Recherche de fichiers rapide, compatible avec `ripgrep`. | `brew install fd` |
| `direnv` | Charge/décharge automatiquement les variables d'environnement par dossier. | `brew install direnv` puis ajouter `eval "$(direnv hook zsh)"` au `.zshrc`. |
| `starship` (alternative prompt) | Invite multiplateforme rapide. | `brew install starship` puis ajouter `eval "$(starship init zsh)"` si vous préférez remplacer Powerlevel10k. |

## Configurer Powerlevel10k pas à pas

1. **Installer une police Nerd Font** (ex. [MesloLGS NF](https://github.com/ryanoasis/nerd-fonts/releases)) et la sélectionner dans iTerm2 `Preferences > Profiles > Text`.
2. **Ouvrir un nouveau terminal** : au premier lancement du thème `powerlevel10k`, l'assistant interactif apparaît.
3. **Répondre aux questions** :
   - Si les symboles affichés ressemblent aux exemples demandés (diamant, cadenas, etc.), répondez `y`.
   - Si un symbole est cassé ou remplacé par un carré, répondez `n` afin que l'assistant choisisse une alternative compatible.
4. **Valider la configuration** : à la fin, l'assistant propose d'écrire le fichier `~/.p10k.zsh`. Acceptez pour que votre prompt reste identique à chaque session.
5. **Relancer le shell** : la configuration sauvegardée est automatiquement chargée par `.zshrc`. Vous pouvez relancer l'assistant à tout moment avec `p10k configure`.

> ❗️ La commande `p10k` est fournie par le thème Powerlevel10k. Si le terminal indique `zsh: command not found: p10k`, vérifiez que le dépôt a bien été cloné dans `${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k` puis relancez votre session.

## Intégrations spécifiques iTerm2

- **iTerm2 Shell Integration** : menu `iTerm2 > Install Shell Integration` pour obtenir la barre d'état, les badges et le copier-coller amélioré.
- **Profiles dynamiques** : importer/exporter vos profils dans `~/Library/Application Support/iTerm2/DynamicProfiles/` pour partager des presets.
- **Triggers & Notifications** : configurer des déclencheurs dans `Preferences > Profiles > Advanced` pour colorer ou notifier des événements (ex. fin de build).
- **Hotkey Window** : activer `Preferences > Keys > Hotkey` pour ouvrir un terminal flottant façon Quake.
- **Integration avec Shortcuts** : sur macOS 13, utilisez l'app Raccourcis pour lancer un profil iTerm2 via des automatisations système.

## Bonnes pratiques pour macOS 13

1. **Mettre à jour régulièrement** les plugins (`omz update` ou `git pull` sur chaque dépôt cloné).
2. **Tester les performances** : certains plugins peuvent ralentir le prompt si l'on en charge trop. Supprimez ceux que vous n'utilisez pas.
3. **Sauvegarder votre configuration** (dotfiles) pour la partager facilement entre machines Ventura et futures versions.
4. **Profiler votre shell** avec `zmodload zsh/zprof` au début de la session, puis `zprof` pour identifier les plugins lents.
5. **Vérifier les autorisations système** dans `Réglages Système > Confidentialité & Sécurité` si un outil (ex. `thefuck` ou `direnv`) nécessite l'accès à vos dossiers de développement.

En combinant ces plugins Zsh, utilitaires CLI et fonctionnalités natives, iTerm2 devient un environnement productif, ergonomique et personnalisé sur macOS 13.

## Annexe : gérer les avertissements Homebrew

Il est fréquent que l'installation de nombreux plugins passe par Homebrew. Si des avertissements similaires à ceux ci-dessous apparaissent lors d'une mise à jour, voici comment les traiter :

```
Warning: Some installed formulae are deprecated or disabled.
  git-flow-avh icu4c@75 icu4c@76 mysql@5.7 openssl@1.1 protobuf@21 spidermonkey@115

Warning: You have unlinked kegs in your Cellar.
  certifi
```

1. **Identifier un remplaçant supporté** :
   - `git-flow-avh` → remplacer par `brew install git-flow` (version officielle) ou envisager `brew install git-town` selon vos usages.
   - `icu4c@75` / `icu4c@76` → désinstaller les anciennes versions (`brew uninstall --ignore-dependencies icu4c@75`) puis installer `brew install icu4c`.
   - `mysql@5.7` → migrer vers `brew install mysql@8.0` ou `brew install mysql` si vous pouvez mettre à niveau vos bases.
   - `openssl@1.1` → utiliser `brew install openssl@3` et reconfigurer les projets dépendants.
   - `protobuf@21` → installer `brew install protobuf` (version courante) et recompiler les projets qui l'utilisent.
   - `spidermonkey@115` → passer à `brew install spidermonkey` (version en cours de support).
2. **Lier les kegs détachés** : exécutez `brew link certifi` pour rendre la bibliothèque accessible aux logiciels qui en dépendent.
3. **Mettre à jour régulièrement** : `brew update && brew upgrade` puis `brew cleanup` pour retirer les artefacts obsolètes.
4. **Consulter la fiche de support** : sur macOS 12 (Monterey), Homebrew est en *Tier 3* ; évitez d'ouvrir des issues tant que vous n'avez pas vérifié <https://docs.brew.sh/Support-Tiers> et envisagez une mise à jour vers une version macOS plus récente.

Ces actions garantissent que les plugins iTerm2 dépendant de Homebrew restent compatibles et performants, même lorsque vous migrez de macOS 12 vers macOS 13.
