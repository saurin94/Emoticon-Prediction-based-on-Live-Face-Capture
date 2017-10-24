import subprocess
cmd = "python imageDetection.py"
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
print  "hello"