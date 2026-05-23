#!/bin/bash

### JOAN RIBOT OLIVER ###

# Assignment: Shell

curl https://raw.githubusercontent.com/swcarpentry/shell-novice/f32646f/data/shell-lesson-data.zip -O
unzip -q shell-lesson-data.zip
rm shell-lesson-data.zip

letter_freq()
{
    local file_path="$1"
    local file_name=$(basename "$file_path" .txt)

    echo "This report contains the frequencies of each letter," > "${file_name}.lfr"
    echo "ordered by descending frequency:" >> "${file_name}.lfr"
    echo "" >> "${file_name}.lfr"
    
    # Get letter frequencies
    grep -o -i '[[:alpha:]]' "$file_path" | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr > /tmp/letter_counts.tmp
    
    # Calculate total letters
    local total=$(awk '{sum+=$1} END {print sum}' /tmp/letter_counts.tmp)
    
    # Print histogram with relative frequencies
    while read count letter; do
        local percentage=$(awk "BEGIN {printf \"%.2f\", ($count/$total)*100}")
        local bar_length=$(awk "BEGIN {printf \"%.0f\", ($percentage/2)}")
        local bar=$(printf '%*s' "$bar_length" | tr ' ' '#')
        printf "%s: %6d (%5.2f%%) %s\n" "$letter" "$count" "$percentage" "$bar" >> "${file_name}.lfr"
    done < /tmp/letter_counts.tmp
    
    rm /tmp/letter_counts.tmp
    
    echo "" >> "${file_name}.lfr"
    echo "Total letters: $total" >> "${file_name}.lfr"
    
    echo "" >> "${file_name}.lfr"
    echo "Author: Joan Ribot Oliver" >> "${file_name}.lfr"
}

letter_freq "shell-lesson-data/writing/data/LittleWomen.txt"



### Citations ###
# Asier (classmate) - to check that the script works both in linux and mac
# https://askubuntu.com/questions/217893/how-to-delete-a-non-empty-directory-in-terminal
# https://stackoverflow.com/questions/3966820/bash-script-to-find-the-frequency-of-every-letter-in-a-file
# https://www.w3schools.com/bash/bash_grep.php
# https://www.geeksforgeeks.org/linux-unix/uniq-command-in-linux-with-examples/
# https://www.hostinger.com/tutorials/grep-command-in-linux?utm_campaign=Generic-Tutorials-DSA%7CNT:Se%7CLO:ES-EN&utm_medium=ppc&gad_source=1&gad_campaignid=20592453563&gbraid=0AAAAADMy-hZgBNg2KtqTUwY3-tTdl9IVI&gclid=CjwKCAjw0sfHBhB6EiwAQtv5qb9e_wfcbu0bRKlUrB6azys-5NS_wXu-o0L3DYjOGkU5qnX4OI7OqhoC7ccQAvD_BwE
# https://stackoverflow.com/questions/68527486/how-to-count-each-letters-from-a-file
# Claude SOnet 4.5 - to make the function accept a path as an argument. I couldn't find it on the internet.