#!/bin/bash

# Funkcja do sprawdzania zainstalowanych rozszerzeń
check_extensions() {
    code --list-extensions > current_extensions.txt
    if ! cmp -s current_extensions.txt base_extensions.txt; then
        echo "$(date): Wykryto nowe rozszerzenia. Wykonuję akcję..." >> monitor_extensions.log
        
        # Znajdź nowe rozszerzenia, które nie są na liście wzorcowej
        new_extensions=$(comm -23 <(sort current_extensions.txt) <(sort base_extensions.txt))
        
        # Odinstaluj nowe rozszerzenia
        for extension in $new_extensions; do
            echo "$(date): Odinstalowuję rozszerzenie $extension" >> monitor_extensions.log
            code --uninstall-extension $extension
        done
        
        # Zaktualizuj plik z poprzednimi rozszerzeniami
        code --list-extensions > current_extensions.txt
    fi
}

# Pętla monitorująca rozszerzenia co 10 sekund
while true; do
    check_extensions
    sleep 10
done