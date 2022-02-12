import os

commit_message = input("Unesi sta si promenio: ")
os.system("git add .")
os.system("git commit -m '"+commit_message+"'")
os.system("git push")

