import subprocess
child1 = subprocess.Popen(["ls","-l"], stdout=PIPE)
child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=PIPE)
out = child2.communicate()
print(out)