#!/bin/bash
pwd: prints the content of the current directory


#!/bin/bash
cd-: go to previous directory

#!/bin/bash
ls -la ./ ../ /boot: list all files including hidden files of the current directory, parent directory and directory /boot

#!/bin/bash
file /tmp/iamafile: shows type of file of the file iamafile located in /tmp directory


ln -s /bin/ls __ls__: creates a soft link of ls file located in /bid directory into the file __ls__


cp -u *.html ../: copy all html files to parent directory if files dont exist or are newer.


mv [[:upper:]]* /tmp/u: mv all files starting with upper case to /tmp/u directory


rm *~: remove all files tthat finish with ~


mkdir -p welcome/to/holberton: Creates s directory tree including welcome to and holberton.


ls -map

ls

cd

ls -l

ls -la

ls -lna

mkdir /tmp/hoberton

mv /tmp/betty /tmp/holberton

rm /tmp/holberton/betty

rm -r /tmp/holbertonpwd: prints the absolute path of the current working directory.
