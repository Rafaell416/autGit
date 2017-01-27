#!/usr/local/bin/python
import subprocess, time
hosts = ('8.8.8.8', 'kernel.org', 'yahoo.com')
def ping(host):
  ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
    stdout=open('/dev/null', 'w'),
    stderr=open('/dev/null', 'w'))
  return ret == 0
def net_is_up():
  print "[%s] Verificando Internet..." % time.strftime("%Y-%m-%d %H:%M:%S")
  xstatus = 1
  githut='''git push -u origin master'''
  proceso ='''
      echo "Comentario :"
      read  comen 
      git add -A
      git commit -m  "$comen"
      '''
  for h in hosts:
    if ping(h):
      final = proceso  + githut
      subprocess.call( final, shell=True)
      print "[%s] Se Enviara a el prepositorio Remoto!" % time.strftime("%Y-%m-%d %H:%M:%S")
      xstatus = 0
      break
  if xstatus:
    subprocess.call( proceso, shell=True)
    print "[%s] No Se Enviara Al repositorio Remoto :(" % time.strftime("%Y-%m-%d %H:%M:%S")
  return xstatus
quit(net_is_up())