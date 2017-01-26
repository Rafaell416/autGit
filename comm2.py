import subprocess

proceso ='''
echo "Comentario :"
read  comen 
git add -A
git commit -m  "$comen"
git push -u origin master
'''
subprocess.call( proceso, shell=True)
