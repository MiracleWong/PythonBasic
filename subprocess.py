# import subprocess
# child1 = subprocess.Popen(["ls","-l"], stdout=PIPE)
# child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=PIPE)
# out = child2.communicate()
# print(out)
import commands
cmm = `cat result.txt | grep "^--- before:" | awk -F ': ' '{print $2}'`
output = commands.getstatusoutput(cmm)  
print  output 