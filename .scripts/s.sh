#!/bin/bash

# code new_file.txt
# CODE_PATH=$(which code)
# echo "$CODE_PATH"



# Lista potencjalnych lokalizacji
locations=(
    "$HOME/.vscode-server/extensions"
    "$HOME/.vscode-remote/extensions"
    "$HOME/.vscode/extensions"
    "$HOME/.vscode-server-insiders/extensions"
)

# Sprawdź każdą lokalizację
for location in "${locations[@]}"; do
    if [ -d "$location" ]; then
        echo "Rozszerzenia znalezione w: $location"
        ls "$location"
    else
        echo "Lokalizacja nie istnieje: $location"
    fi
done