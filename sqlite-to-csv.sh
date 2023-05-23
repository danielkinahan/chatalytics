# sqlite-to-csv.sh

# don't really need this script anymore, i will keep it around just for reference for now

# first install libssl-dev, tcl, gobjc++
# then install sqlcipher (built from source) https://github.com/sqlcipher/sqlcipher

#sigBase="/mnt/c/Users/DANKINAH/AppData/Roaming/Signal/";
sigBase="/mnt/c/Users/daniel/AppData/Roaming/Signal/";
key=$( /usr/bin/jq -r '."key"' ${sigBase}config.json );
#db="/mnt/c/Users/DANKINAH/AppData/Roaming/Signal/sql/db.sqlite";
db="/mnt/c/Users/daniel/AppData/Roaming/Signal/sql/db.sqlite";
clearTextMsgs="${sigBase}copy.csv";

/home/dankinah/sqlcipher/sqlcipher -readonly -list -noheader "$db" "PRAGMA key = \"x'"$key"'\";select json from messages;" > "$clearTextMsgs";