read -r -d '' FILE_CONTENT << 'HEREDOC'
BEGIN
#!/bin/bash

declare -a devices=("XHC" "RP05" "RP09" "RP13" "AWAC") # <<<--- ADD YOUR DEVICES HERE!
for device in "${devices[@]}"; do
    if grep -qw ^$device.*enabled "/proc/acpi/wakeup"; then
        echo "$device" > "/proc/acpi/wakeup"
    fi
done

END
HEREDOC
echo -n "${FILE_CONTENT:6:-3}" > "/usr/local/bin/disable-devices-as-wakeup.bash"

