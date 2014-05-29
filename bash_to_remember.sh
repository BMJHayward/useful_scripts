# bash to remember

# some useful scripts at http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html

$ sudo !! #type this with nothing else to re-do previous command as a sudo command

$ python -m SimpleHTTPServer # start server with webpage at port 8000

$ mtr google.com # may need to install this. gives you same data as ping and traceroute commands

'ctrl+x+e' 'ctrl+e' or 'ctrl+x' to launch distro terminal-based text editor

$ nl filename.txt # gives you numbered lines when displaying text files

$ shuf # shuffles display of lines/files/folders when using 'ls' command

$ ss # display socket statistics. similar to netstat command

$ last #show history of last logged in users

$ curl ifconfig.me # need curl package installed 1st. shows your external IP address

$ tree # shows current directory structure in tree format

$ pstree # shows processes and child processes in tree structure

$ <space character> <command> # <command> is not logged in history if preceded by <space>

$ stat <filename> | <filesystem_name> # displays status information

$ mount | column -t # lists mounted filesystems

'ctrl+l' clears terminal

$ screen ./script_name.sh # ctrl+a to attach to process 'd' to de-attach

$ file <filename> # gives file type

$ id # prints user and group ids to terminal

$ ^foo^bar # replace foo with bar. re-run last command. handy with long commands, saves typing whole thing again when spelling mistake

$ > file_name.txt # flush contents of file. saves recreating file if you need empty file with same name.

$ <commands_to_execute> <switches> <files/folders> | at <time> # works like cron tasks. 'at' command schedules tasks for you

$ du -h --max-depth=1 # outputs size of sub-folders in human readable form

$ expr (mathematical expression) # treats input as maths equation

$ look 'target string' # looks up dictionary for target string. includes as substring

$ yes "message to print continuously" # prints given string until you interrupt it

$ factor <number> #outputs all factors of given number

$ ping -i 60 -a www.google.com # gives a sound when ping successful

$ tac <filename> # streams file backwards. opposite to cat command

$ strace <command> # debugging tool. stack trace given command

$ <command>; disown -a && exit # disown lets command run in background so you can exit terminal

$ $ getconf LONG_BIT # shows if a 32 or 64 bit machine

$ while sleep 1;do tput sc;tput cup 0 $(($(tput cols)-29));date;tput rc;done & # display date&time in top of terminal

$ tree | convert label:@- /home/brendan/Pictures/tree.png # outputs tree command as png image in /images folder

$ watch -t -nl "data +%T|figlet" # figlet shows animated digital clock in terminal

$ host www.google.com # host looks up DNS
$ dig www.google.com # dig DNS lookup

$ dstat # shows stats on system resources

$ bind -p # show all shortcuts available in BASH shell

$ touch /forcefsck # creates empty folder under root, forces system to perform file system check on next boot

$ lsb_release # print distro info

$ nc -zv localhost 80 # check if port 80 is open

$ curl ipinfo.io # outputs geographical location of IP address

$ find . -user root # shows root owned files in current directory. can check any user other than root

$ <package manager install command> build-dep <target_package> # 'build-dep builds dependencies. easier installation

$ lsof -iTCP:80 -sTCP:LISTEN # displays all processes using port 80

$ find -size +100M # find lists anything > 100M in current directory

$ pdftk <pdf1> <pdf2> <pdfn> output output.pdf #merges pdf files together

$ ps -LF -u avi # displays processes and threads of user 'avi' switches L and F give list and full format

$ Startx -:1 # starts more X sessions, saves you logging in and out. ctrl+F7 -F12 for X sessions