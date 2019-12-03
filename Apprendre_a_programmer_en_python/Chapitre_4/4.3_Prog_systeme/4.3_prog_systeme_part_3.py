import os

# 3.1 Fonction system & popen
print("---------------------")
cmd = os.popen("ls")
print(cmd)
lu =cmd.read()
print(lu)
