Catching all opened files by script
++++++++++++++++++++++++++++++++++++++++++++++++++++

Occasionally you need to know all the files accessed by some script. A motivating example is if you want to package a minimal set of files that are needed to run a command. For example One of the dataset scripts I use needed the LIGO O3 calibration repository, which is quite large. Only a handful of files are accessed to create a calibration, so I want just those files. In my case, I pulled many folders from the SVN - about 300MB of them. I didn't want to push those files into git, but I was able to by finding just the files needed to run the script using strace.


On linux you can do this using the "strace" command to indicate every single file that a process has opened. You can then filter out files from that listing. strace does slow down programs considerably, but it can be useful.

> strace -e openat -o calibration_files.txt pytest -- T_LHO_FDL_stage1.py 

now all opened files, including a ton from the filesystem, are listed in calibration_files.txt. You can then filter these using sed

> sed -e '/calibrationSVN/!d' calibration_files.txt -i

and finally a few regexes in vim/emacs can extract just the filenames. One can then use that list of files from git add
