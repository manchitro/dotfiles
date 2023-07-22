# rgrep
# Autogenerated from man page /usr/share/man/man1/rgrep.1.gz
complete -c rgrep -l help -d 'Output a usage message and exit'
complete -c rgrep -s V -l version -d 'Output the version number of  grep and exit. SS "Pattern Syntax"'
complete -c rgrep -s E -l extended-regexp -d 'Interpret  PATTERNS as extended regular expressions (EREs, see below)'
complete -c rgrep -s F -l fixed-strings -d 'Interpret  PATTERNS as fixed strings, not regular expressions'
complete -c rgrep -s G -l basic-regexp -d 'Interpret  PATTERNS as basic regular expressions (BREs, see below)'
complete -c rgrep -s P -l perl-regexp -d 'Interpret  PATTERNS as Perl-compatible regular expressions (PCREs)'
complete -c rgrep -s e -l regexp -d 'Use  PATTERNS as the patterns'
complete -c rgrep -s f -l file -d 'Obtain patterns from R FILE , one per line'
complete -c rgrep -s i -l ignore-case -d 'Ignore case distinctions in patterns and input data, so that characters that …'
complete -c rgrep -l no-ignore-case -d 'Do not ignore case distinctions in patterns and input data'
complete -c rgrep -s v -l invert-match -d 'Invert the sense of matching, to select non-matching lines'
complete -c rgrep -s w -l word-regexp -d 'Select only those lines containing matches that form whole words'
complete -c rgrep -s x -l line-regexp -d 'Select only those matches that exactly match the whole line'
complete -c rgrep -s c -l count -d 'Suppress normal output; instead print a count of matching lines for each inpu…'
complete -c rgrep -l color -l colour -d 'Surround the matched (non-empty) strings, matching lines, context lines, file…'
complete -c rgrep -s L -l files-without-match -d 'Suppress normal output; instead print the name of each input file from which …'
complete -c rgrep -s l -l files-with-matches -d 'Suppress normal output; instead print the name of each input file from which …'
complete -c rgrep -s m -l max-count -d 'Stop reading a file after  NUM matching lines'
complete -c rgrep -s o -l only-matching -d 'Print only the matched (non-empty) parts of a matching line, with each such p…'
complete -c rgrep -s q -l quiet -l silent -d 'Quiet; do not write anything to standard output'
complete -c rgrep -s s -l no-messages -d 'Suppress error messages about nonexistent or unreadable files'
complete -c rgrep -s b -l byte-offset -d 'Print the 0-based byte offset within the input file before each line of output'
complete -c rgrep -s H -l with-filename -d 'Print the file name for each match'
complete -c rgrep -s h -l no-filename -d 'Suppress the prefixing of file names on output'
complete -c rgrep -l label -d 'Display input actually coming from standard input as input coming from file R…'
complete -c rgrep -s n -l line-number -d 'Prefix each line of output with the 1-based line number within its input file'
complete -c rgrep -s T -l initial-tab -d 'Make sure that the first character of actual line content lies on a tab stop,…'
complete -c rgrep -s Z -l null -d 'Output a zero byte (the ASCII  NUL character) instead of the character that n…'
complete -c rgrep -s A -l after-context -d 'Print  NUM lines of trailing context after matching lines'
complete -c rgrep -s B -l before-context -d 'Print  NUM lines of leading context before matching lines'
complete -c rgrep -s C -l context -d 'Print  NUM lines of output context'
complete -c rgrep -l group-separator -d 'When  -A ,  -B , or  -C are in use, print  SEP instead of  -- between groups …'
complete -c rgrep -l no-group-separator -d 'When  -A ,  -B , or  -C are in use, do not print a separator between groups o…'
complete -c rgrep -s a -l text -d 'Process a binary file as if it were text; this is equivalent to the  --binary…'
complete -c rgrep -l binary-files -d 'If a file\'s data or metadata indicate that the file contains binary data, ass…'
complete -c rgrep -s D -l devices -d 'If an input file is a device, FIFO or socket, use  ACTION to process it'
complete -c rgrep -s d -l directories -d 'If an input file is a directory, use  ACTION to process it'
complete -c rgrep -l exclude -d 'Skip any command-line file with a name suffix that matches the pattern R GLOB…'
complete -c rgrep -l exclude-from -d 'Skip files whose base name matches any of the file-name globs read from  FILE…'
complete -c rgrep -l exclude-dir -d 'Skip any command-line directory with a name suffix that matches the pattern R…'
complete -c rgrep -s I -d 'Process a binary file as if it did not contain matching data; this is equival…'
complete -c rgrep -l include -d 'Search only files whose base name matches  GLOB (using wildcard matching as d…'
complete -c rgrep -s r -l recursive -d 'Read all files under each directory, recursively, following symbolic links on…'
complete -c rgrep -s R -l dereference-recursive -d 'Read all files under each directory, recursively'
complete -c rgrep -l line-buffered -d 'Use line buffering on output.  This can cause a performance penalty'
complete -c rgrep -s U -l binary -d 'Treat the file(s) as binary'
complete -c rgrep -s z -d '( --null-data ) option, and grep -P may warn of unimplemented features'
complete -c rgrep -l null-data -d 'Treat input and output data as sequences of lines, each terminated by a zero …'

