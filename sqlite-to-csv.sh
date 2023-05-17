# sqlite-to-csv.sh

# need sqlcipher (built from source), libssl-dev, tcl, gobjc++

# From https://unix.stackexchange.com/a/505009/413853
sigBase="/mnt/c/Users/DANKINAH/AppData/Roaming/Signal/";
key=$( /usr/bin/jq -r '."key"' ${sigBase}config.json );
db="/mnt/c/Users/DANKINAH/AppData/Roaming/Signal/sql/db.sqlite";
clearTextMsgs="${sigBase}backup-desktop.csv";

/home/dankinah/sqlcipher/sqlcipher -list -noheader "$db" "PRAGMA key = \"x'"$key"'\";select json from messages;" > "$clearTextMsgs";