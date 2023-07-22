# par2
# Autogenerated from man page /usr/share/man/man1/par2.1.gz
complete -c par2 -s h -d 'Show this help'
complete -c par2 -s V -d 'Show version'
complete -c par2 -o VV -d 'Show version and copyright'
complete -c par2 -s a -d 'Set the main PAR2 archive name; required on create, optional for verify and r…'
complete -c par2 -o 'b<n>' -d 'Set the Block\\(hyCount'
complete -c par2 -o 's<n>' -d 'RB "Set the Block\\(hySize (don\'t use both " "-b" " and " "-s" ")"'
complete -c par2 -o 'r<n>' -d 'Level of redundancy (percentage)'
complete -c par2 -o 'r<c><n>' -d 'Redundancy target size, <c>=g(iga),m(ega),k(ilo) bytes'
complete -c par2 -o 'c<n>' -d 'RB "Recovery block count (don\'t use both " "-r" " and " "-c" ")"'
complete -c par2 -o 'f<n>' -d 'First Recovery\\(hyBlock\\(hyNumber'
complete -c par2 -s u -d 'Uniform recovery file sizes'
complete -c par2 -s l -d 'RB "Limit size of recovery files (don\'t use both " "-u" " and " "-l" ")"'
complete -c par2 -o 'n<n>' -d 'RB "Number of recovery files (don\'t use both " "-n" " and " "-l" ")"'
complete -c par2 -o 'm<n>' -d 'Memory (in MB) to use'
complete -c par2 -o 't<n>' -d 'RB "Number of threads used for main processing (auto-detected)"'
complete -c par2 -o 'T<n>' -d 'RB "Number of files hashed in parallel (during file verification and creation…'
complete -c par2 -s v -d 'Be more verbose'
complete -c par2 -s q -d 'RB "Be more quiet (" "-qq" " gives silence)"'
complete -c par2 -s p -d 'Purge backup files and par files on successful recovery or when no recovery i…'
complete -c par2 -s R -d 'Recurse into subdirectories (only useful on create)'
complete -c par2 -s N -d 'data skipping (find badly mispositioned data blocks)'
complete -c par2 -o 'S<n>' -d 'Skip leaway (distance +/- from expected block position)'
complete -c par2 -o 'B<path>' -d 'Set the basepath to use as reference for the datafiles'

