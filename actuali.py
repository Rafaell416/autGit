import subprocess
re="x"
codigo = '''there_are_changes=$(git status | grep nothin)
               if  $there_are_changes == "nothing to commit, working tree cleanw" ; then
                	echo "No HAy Cambios !"
               else
	              echo "Hay Cambios "
               fi


                '''
re = subprocess.call(codigo, shell=True )



