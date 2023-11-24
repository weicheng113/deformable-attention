### pyenv setup

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install 3.11.6

### manage multiple pythons

pyenv shell 3.10.13
pyenv shell 3.11.6

pyenv versions

### activate environment

Linux/MacOs:
source .venv/bin/activate
deactivate

Windows:
.\.venv\Scripts\Activate.ps1
