#!bin/bash

# Script para a automatização da instalação do Docker e do VSCode.

sudo apt install git -y
echo "Digite seu email"
read email
echo "Digite seu nome"
read name
git config --global user.name "${name}"
git config --global user.email $email

# Settar os alias
if [ -e bash_aliases ]
then
  cp bash_aliases ~/.bash_aliases
fi 

# Instalar a font Roboto Mono, usada no VSCODE
curl https://www.wfonts.com/download/data/2016/05/18/roboto-mono/roboto-mono.zip --output roboto-mono.zip
mkdir ~/.fonts
mv roboto-mono.zip ~/.fonts
unzip ~/.fonts/roboto-mono.zip -d ~/.fonts
rm ~/.fonts/roboto-mono.zip
fc-cache -f

# Docker.
printf "\n\n\e[33;1mInstalação do Docker:\e[m\n\n"
printf "\n\n\e[33;1mPrimeiro passo: Obtendo Dependências.\e[m\n\n"

sudo apt-get update
yes | sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

printf "\n\n\e[33;1mSegundo passo: instalando Docker Community Edition.\e[m\n\n"

sudo apt-get update
yes | sudo apt-get install docker-ce
printf "\e[33;1m"
    docker -v
printf "\e[m"

printf "\n\n\e[33;1mTerceiro passo: Rodar o hello-world pra checar se está tudo certo.\e[m\n\n"

sudo docker run hello-world

printf "\n\n\e[33;1mDocker Pronto!\e[m\n\n"

# VS Code.
printf "\n\n\e[33;1mInstalação do VS Code:\e[m\n\n"
printf "\n\n\e[33;1mPrimeiro passo: Instalação do VS Code.\e[m\n\n"

    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
    yes | sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

    yes | sudo apt-get install apt-transport-https
    sudo apt-get update
    yes | sudo apt-get install code

printf "\n\n\e[33;1mSegundo passo: Instalação de Extensões.\e[m\n\n"

    # Extensões Gerais
    code --install-extension wesbos.theme-cobalt2
    code --install-extension ms-vsliveshare.vsliveshare
    code --install-extension eamodio.gitlens
    code --install-extension peterjausovec.vscode-docker
    code --install-extension canna.box-comment
    code --install-extension jolaleye.horizon-theme-vscode

    # Rails
    code --install-extension bung87.rails
    code --install-extension bung87.vscode-gemfile
    code --install-extension rebornix.ruby

    # Ionic
    code --install-extension eg2.tslint
    
    # Configurações do Usuário.
    printf ('{"window.menuBarVisibility": "toggle", "workbench.colorTheme": "Horizon", "editor.fontFamily": "\'Roboto Mono\', \'Ubuntu Mono\', \'monospace\'"}' > ~/.config/Code/User/settings.json

printf "\n\n\e[33;1mVS Code Pronto!\e[m\n\n"

printf "\n\n\e[33;Fim! {IN}\e[m\n\n"
