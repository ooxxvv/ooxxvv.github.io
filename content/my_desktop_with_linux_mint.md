Title: My Desktop with Linux Mint


### Dropbox
 * Install & Login 


### Firefox
 * Link setting form Dropbox
````
ln -s ~/Dropbox/pData/Firefox/chrome/
````

### Synapse
 * Hotkey: alt+space
````
sudo add-apt-repository ppa:synapse-core/ppa
sudo apt-get update
sudo apt-get install synapse
ln -sf ~/Dropbox/pData/Linux/applications ~/.local/share/
````

### Mouse
 * Adjustin setting
 * Linke theme forlder
````
ln -s ~/Dropbox/pData/Linux/cursor_theme/ooxxvv-theme/ ~/.icons
ln -s ~/Dropbox/pData/Linux/cursor_theme/dummy-theme/ ~/.icons
````

### Desktop
 * Setup Icon & Wallpaper


### Font
````
sudo ln -s ~/Dropbox/BigFiles/Fonts/ /usr/share/fonts/fontfiles
sudo fc-cache -fv
````

### Fcitx
 * LightUI
````
  * ln -s ~/Dropbox/pData/fcitx ~/.config
````

### Git
 * Install


### Keepass2
 * Global HotKey: ctrl+alt+a: keepass2 --auto-type
````
sudo apt-get install xdotool
sudo add-apt-repository ppa:dlech/keepass2-plugins
sudo apt-get update
sudo apt-get install keepass2-plugin-application-indicator
ln -s ~/Dropbox/pData/Keepass/keepassx ~/.config/
````


### Duble Commander
  * doublecmd-gtk
````
  * ln -sf ~/Dropbox/pData/DoubleCommander/doublecmd ~/.config/
````

### Diodon
 * Hotkey: Ctrl+Shift+x


### vim-gtk
````
ln -s ~/Dropbox/pData/Vim/vimrc ~/.vim/vimrc
ln -s ~/Dropbox/pData/Vim/colors ~/.vim/colors
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/vundle
:PluginInstall
````

### YCM
````
   * sudo apt-get install build-essential cmake
   * sudo apt-get install python-dev
   * cd ~/.vim/bundle/YouCompleteMe
   * ./install.sh --clang-completer
````


### Ctags
````
sudo apt-get install exuberant-ctags
````

### Goldendict
 * Hotkey: ctrl+alt+z

### zsh
````
chsh -s /bin/zsh
wget --no-check-certificate http://install.ohmyz.sh -O - | sh
ln -sf ~/Dropbox/pData/zsh/.zshrc ~/.zshrc
````


### Vbox
 * Download form offical site
 * Install Extension Pack 


### Thunderbird
````
ln -s ~/Dropbox/pData/Thunderbird/chrome
ln -sf ~/Dropbox/pData/Thunderbird/abook.mab
ln -sf ~/Dropbox/pData/Thunderbird/key3.db
ln -sf ~/Dropbox/pData/Thunderbird/prefs.js
ln -sf ~/Dropbox/pData/Thunderbird/signons.sqlite 
````


### Pip
````
apt-get install python-pip
````


### Pyenv & Pyenv-virtualenv
````
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
git clone git://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
sudo pip install virtualenv
````


### Pyenv for zsh
````
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec $SHELL
````

