import subprocess
re="x"
print (re)
re = subprocess.call('there_are_changes=$(git status | grep nothin);echo $there_are_changes', shell=True )
print (re)


if re == '0':
	print "Hay Cambios En El Proyecto";
else:
	print "NO Hay Cambios En El Proyecto";

