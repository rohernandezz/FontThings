#Opens last file in all subfolders of the directory where the script is run from

echo -n -e "\033]0;Opener\007"

cd "$(dirname "$0")"

for dir in */;
	do cd "$dir";
	ls| tail -1 |xargs open; cd ..;
	done 

osascript -e 'tell application "Terminal" to close (every window whose name contains "Opener")' &
