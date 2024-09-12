#!/bin/bash

# echo "$(date): Skrypt run_monitor_extensions.sh został uruchomiony" >> /tmp/postStartCommand.log

# Zapisz aktualną ścieżkę katalogów w logach
# echo "$(date): Aktualna ścieżka katalogów: $(pwd)" >> /tmp/postStartCommand.log

# Załaduj zmienne środowiskowe
source ~/.bashrc || source ~/.profile || source ~/.bash_profile

# Ponownie załaduj listę komend w terminalu
# hash -r

# Znajdź ścieżkę do polecenia `code`
# CODE_PATH=$(which code)
# CODE_PATH='/vscode/bin/linux-x64/4849ca9bdf9666755eb463db297b69e5385090e3/bin/remote-cli/code'

# Zapisz sciezki do CODE
# echo "$(date): Ścieżka do code: $CODE_PATH" >> /tmp/postStartCommand.log

# Sprawdź, czy `code` jest zainstalowane
# if [ -z "$CODE_PATH" ]; then
#     echo "$(date): run_monitor - code or code-insiders is not installed" >> /tmp/postStartCommand.log
#     exit 1
# fi

# # Dodaj ścieżkę do `code` do zmiennej PATH
# export PATH=$(dirname "$CODE_PATH"):$PATH

# Uruchomienie skryptu monitor_extensions.sh w tle
echo "$(date): Uruchamiam monitor_extensions.sh" >> /tmp/postStartCommand.log
bash -c .scripts/monitor_extensions.sh >> .scripts/monitor_extensions.log 2>&1 