import subprocess

proceso ='''
echo "Comentario :"
read  comen 
git add -A
git commit -m  "$comen"
'''
subprocess.call( proceso, shell=True)




