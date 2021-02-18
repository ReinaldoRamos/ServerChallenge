#!/bin/bash

repos=( 
    ".Devtools/"
)

pullRepoGit(){

    echo ""
    echo "Getting latest for" ${#repos[@]} "repositories using pull --rebase"

    for repo in "${repos[@]}"
    do
        echo ""
        echo "****** Getting latest for" ${repo} "******"
        cd "${repo}"
        git=$(git status)
        if [[ $git =~ "nothing to commit" ]];
        then
            echo "Repositorie is up to date."
        elif [ $? == 0 ]
        then
            echo $git
        else
            echo "não atualizado"
            exit 1
        fi
    done
}

findFiles(){

    files=(
        "controllers"
        "model"
        "routes"
        "templates"
    )
    for repo in "challenge/app/"
    do
        cd "${repo}"
        for file in "${files[@]}"
        do
            if [ -e "$file" ]; 
            then
                echo "$file ok"
            else
                echo "$file doesn't exist"
                exit 1
            fi
        done
    done
}

testAPI(){
    URL="http://0.0.0.0:8080/ping"
    testURL=$(curl -s $URL);
    if [[ $testURL == "pong" ]];
    then
        echo "API OK"
    else
        echo "API is not ok"
        exit 1
    fi
}

testMySql(){
    DBEXISTS=$( mysql -u"$DB_USER" -p"$DB_PASS" -h"$DB_HOST" )
    if ! $DBEXISTS ;then
        echo "Connection fail"
    else
        echo "Connection Ok"
        exit 1
    fi
}

testDB(){
    DBEXISTS=$( mysql -u"$DB_USER" -p"$DB_PASS" -h"$DB_HOST" -e "SHOW DATABASES LIKE '"$DB_NAME"';" | grep "$DB_NAME" > /dev/null; echo "$?")
    if [ $DBEXISTS -eq 0 ];then
        echo "$DBNAME Ok"
    else
        echo "database fail"
        exit 1
    fi
}

echo "***** verifing if Git is up to date *****"
pullRepoGit
echo "***** verifing important files and directories is ok *****"
findFiles
echo "***** testing API *****"
testAPI
echo "***** testing Connection MySql *****"
testDB
echo "***** testing Data Base *****"
testDB