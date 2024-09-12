#!/bin/bash

LOG_FILE=".scripts/monitor_extensions.log"
BASE_EXTENSIONS_FILE=".scripts/base_extensions.json"
CURRENT_EXTENSIONS_FILE="/home/codespace/.vscode-remote/extensions/extensions.json"

# Upewnij się, że katalog istnieje
mkdir -p "$(dirname "$LOG_FILE")"

echo "$(date): Skrypt monitor_extensions.sh został uruchomiony" >> "$LOG_FILE"

# Funkcja do sprawdzania zainstalowanych rozszerzeń
check_extensions() {
    echo "$(date): Sprawdzanie rozszerzeń..." >> "$LOG_FILE"

    # Sprawdź, czy plik z aktualnymi rozszerzeniami istnieje
    if [ ! -f "$CURRENT_EXTENSIONS_FILE" ]; then
        echo "$(date): Plik $CURRENT_EXTENSIONS_FILE nie istnieje" >> "$LOG_FILE"
        return
    fi

    # Wyodrębnij id z pliku base_extensions.json i umieść je w tablicy asocjacyjnej
    declare -A base_ids_map
    while IFS= read -r base_id; do
        base_ids_map["$base_id"]=1
    done < <(jq -r '.[] | .identifier.id' "$BASE_EXTENSIONS_FILE")

    # Funkcja do wczytywania aktualnych rozszerzeń
    load_current_extensions() {
        jq -r '.[] | .identifier.id' "$CURRENT_EXTENSIONS_FILE"
    }

    current_ids=$(load_current_extensions)

    # Porównaj id z obu plików iteracyjnie
    for current_id in $current_ids; do
        if [[ -z "${base_ids_map[$current_id]}" ]]; then
            path=$(jq -r --arg id "$current_id" '.[] | select(.identifier.id == $id) | .location.path' "$CURRENT_EXTENSIONS_FILE")
            if [ -n "$path" ]; then
                echo "$(date): Usuwam rozszerzenie $current_id z katalogu $path" >> "$LOG_FILE"
                rm -rf "$path"
                # Usuń wpis z extensions.json
                jq --arg id "$current_id" 'del(.[] | select(.identifier.id == $id))' "$CURRENT_EXTENSIONS_FILE" > "${CURRENT_EXTENSIONS_FILE}.tmp" && mv "${CURRENT_EXTENSIONS_FILE}.tmp" "$CURRENT_EXTENSIONS_FILE"
            fi
        fi
    done
}

# Pętla monitorująca rozszerzenia co 10 sekund
while true; do
    check_extensions
    sleep 10
done