#Opens all files in 0_UFO Folder

echo -n -e "\033]0;Opener\007"

cd "$(dirname "$0")"

cd 0_UFO

for file in */;
	do open -a "RoboFont" $file ;
	done 

osascript -e 'tell application "Terminal" to close (every window whose name contains "Opener")' &