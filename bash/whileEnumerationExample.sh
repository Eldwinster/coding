#!/bin/bash
printf "Launching the directory file enumeration."
directories=('Changes' 'VIDEO' 'public')
for directory in "${directories[@]}"; do
gobuster dir -q -t 64 -x .html,.conf,.php,.js,.css \
    -u http://webenum.thm/"${directory}" \
    -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt \
    -o /home/yann/org/ref/files/tryhackme/webEnumeration/gobuster/"${directory}"dirFilesEnumeration.txt
done
sleep 1
printf "Directory file enumeration done.\n Proceeding with virtual host file enumeration"
sleep 1
vhosts=('products' 'learning')
for vhost in "${vhosts[@]}"; do
gobuster dir -q -t 64 -x .txt,.conf,.php \
    -u http://"${vhost}".webenum.thm \
    -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt \
    -o /home/yann/org/ref/files/tryhackme/webEnumeration/gobuster/"${vhost}"VhostFilesEnumeration.txt
done
