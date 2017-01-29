import subprocess
comm = 'if git status; then echo "1"; else echo "0"; fi'
ret = subprocess.call( comm, shell=True)

print(ret);
