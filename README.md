# Project on Mapping esports data
- First install a virtual environment.
- I used `virtualenv` to create environment

# Creating Virtual Environment with virtualenv
- Go to terminal and type
- `virtualenv env_name`
- To activate type
- source env_name/bin/activate

# Creating Virtual Environment with pyenv
- Make sure you have Homebrew and zsh installed on Mac
- Now go to the terminal and type 
- `brew install pyenv`
- After installation go to github repo `https://github.com/pyenv/pyenv#basic-github-checkout`
- Go to terminal and type `nano .zshrc` if zsh is installed or otherwise follow bashrc
## Pyenv setup
- Copy paste these commands
- `export PYENV_ROOT="$HOME/.pyenv"`
- `command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"`
- `eval "$(pyenv init -)"`

Once this is done, press control-X and Y and then enter to save the file

## Restart your shell
`exec "$SHELL"`

## Installing Pyenv virtualenv
`brew install pyenv-virtualenv`

## Pyenv virtualenv setup in zsh
Go to Repo for reference: `https://github.com/pyenv/pyenv-virtualenv`
- Paste  `eval "$(pyenv virtualenv-init -)"` at the end.
- save the file and restart the shell with `exec "$SHELL"`

Now both pyenv and pyenv virtualenv are installed.

## Setting the pyenv python version as default
- Check `pyenv versions`
- If only system is output then you need to setup new python
- I am using `3.9.10`
- To install `pyenv install 3.9.10`
- To set it as default `pyenv global 3.9.10`

## Creating new environment with pyenv 3.9.10 version
- `pyenv virtualenv 3.9.10 env-name` This is using 3.9.10
- If the version is set as global then you can directly create environment with
- `pyenv virtualenv env-name`

## List existing venvs
- `pyenv virtualenvs`

## Activate virtual env
- `pyenv env-name activate`
## Deactivate virtual env
- `pyenv deactivate`