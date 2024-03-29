# bup-save
# Autogenerated from man page /usr/share/man/man1/bup-save.1.gz
complete -c bup-save -s r -l remote -d 'save the backup set to the given remote server'
complete -c bup-save -s t -l tree -d 'after creating the backup set, print out the git tree id of the resulting bac…'
complete -c bup-save -s c -l commit -d 'after creating the backup set, print out the git commit id of the resulting b…'
complete -c bup-save -s n -l name -d 'after creating the backup set, create a git branch named \\f[I]name\\f[R] so th…'
complete -c bup-save -s d -l date -d 'specify the date of the backup, in seconds since the epoch, instead of the cu…'
complete -c bup-save -s f -l indexfile -d 'use a different index filename instead of \\f[V]$BUP_DIR/bupindex\\f[R]'
complete -c bup-save -s v -l verbose -d 'increase verbosity (can be used more than once)'
complete -c bup-save -s q -l quiet -d 'disable progress messages'
complete -c bup-save -l smaller -d 'don\\[cq]t back up files >= \\f[I]maxsize\\f[R] bytes'
complete -c bup-save -l bwlimit -d 'don\\[cq]t transmit more than \\f[I]bytes/sec\\f[R] bytes per second to the serv…'
complete -c bup-save -l strip -d 'strips the path that is given from all files and directories. RS '
complete -c bup-save -l strip-path -d 'strips the given path prefix \\f[I]path-prefix\\f[R] from all files and directo…'
complete -c bup-save -l graft -d 'a graft point \\f[I]old_path\\f[R]=\\f[I]new_path\\f[R] (can be used more than on…'
complete -c bup-save -s '#' -l compress -d 'set the compression level to # (a value from 0-9, where 9 is the highest and …'

