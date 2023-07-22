# bup-meta
# Autogenerated from man page /usr/share/man/man1/bup-meta.1.gz
complete -c bup-meta -s c -l create -d 'Create a metadata archive for the specified \\f[I]path\\f[R]s'
complete -c bup-meta -s t -l list -d 'Display information about the metadata in an archive'
complete -c bup-meta -s x -l extract -d 'Extract a metadata archive'
complete -c bup-meta -l start-extract -d 'Build a filesystem tree matching the paths stored in a metadata archive'
complete -c bup-meta -l finish-extract -d 'Finish applying the metadata stored in an archive to the filesystem'
complete -c bup-meta -l edit -d 'Edit metadata archives'
complete -c bup-meta -s f -l file -d 'Read the metadata archive from \\f[I]filename\\f[R] or write it to \\f[I]filenam…'
complete -c bup-meta -s R -l recurse -d 'Recursively descend into subdirectories during \\f[V]--create\\f[R]'
complete -c bup-meta -l xdev -l one-file-system -d 'don\\[cq]t cross filesystem boundaries \\[en] though as with tar and rsync, the…'
complete -c bup-meta -l numeric-ids -d 'Apply numeric IDs (user, group, etc'
complete -c bup-meta -l symlinks -d 'Record symbolic link targets when creating an archive, or restore symbolic li…'
complete -c bup-meta -l paths -d 'Record pathnames when creating an archive.  This option is enabled by default'
complete -c bup-meta -l set-uid -d 'Set the metadata uid to the integer \\f[I]uid\\f[R] during \\f[V]--edit\\f[R]'
complete -c bup-meta -l set-gid -d 'Set the metadata gid to the integer \\f[I]gid\\f[R] during \\f[V]--edit\\f[R]'
complete -c bup-meta -l set-user -d 'Set the metadata user to \\f[I]user\\f[R] during \\f[V]--edit\\f[R]'
complete -c bup-meta -l unset-user -d 'Remove the metadata user during \\f[V]--edit\\f[R]'
complete -c bup-meta -l set-group -d 'Set the metadata user to \\f[I]group\\f[R] during \\f[V]--edit\\f[R]'
complete -c bup-meta -l unset-group -d 'Remove the metadata group during \\f[V]--edit\\f[R]'
complete -c bup-meta -s v -l verbose -d 'Be more verbose (can be used more than once)'
complete -c bup-meta -s q -l quiet -d 'Be quiet.  EXAMPLES # Create a metadata archive for /etc'

