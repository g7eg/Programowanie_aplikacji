#!/bin/bash

LOG_FILE=".scripts/monitor_extensions.log"
CURRENT_EXTENSIONS_FILE=".scripts/current_extensions.txt"
BASE_EXTENSIONS_FILE=".scripts/base_extensions.txt"

echo "$(date): Skrypt monitor_extensions.sh został uruchomiony" >> $LOG_FILE

# Funkcja do sprawdzania zainstalowanych rozszerzeń
check_extensions() {
    echo "$(date): Sprawdzanie rozszerzeń..." >> $LOG_FILE
    # Generowanie listy zainstalowanych rozszerzeń i usuwanie niechcianej linii
    code --list-extensions | grep -v 'Rozszerzenia zainstalowane w lokalizacji Codespaces:' | sort > $CURRENT_EXTENSIONS_FILE
    
    if ! cmp -s $CURRENT_EXTENSIONS_FILE $BASE_EXTENSIONS_FILE; then
        echo "$(date): Wykryto nowe rozszerzenia. Wykonuję akcję..." >> $LOG_FILE
        
        # Znajdź nowe rozszerzenia, które nie są na liście wzorcowej
        new_extensions=$(comm -23 $CURRENT_EXTENSIONS_FILE $BASE_EXTENSIONS_FILE)
        
        # Odinstaluj nowe rozszerzenia
        for extension in $new_extensions; do
            echo "$(date): Odinstalowuję rozszerzenie $extension" >> $LOG_FILE
            code --uninstall-extension $extension
        done
        
        # Zaktualizuj plik z poprzednimi rozszerzeniami
        code --list-extensions | grep -v 'Rozszerzenia zainstalowane w lokalizacji Codespaces:' | sort > $CURRENT_EXTENSIONS_FILE
    fi
}

# Pętla monitorująca rozszerzenia co 10 sekund
while true; do
    check_extensions
    sleep 10
done