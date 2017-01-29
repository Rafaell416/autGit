import subprocess

re = subprocess.call('there_are_changes=$(git status | grep nothin);echo $there_are_changes', shell=True )
print (re)

if re == 0:
	print "No Hay Cambios En El Proyecto";
else:
	print "Hay Cambios En El Proyecto";

	