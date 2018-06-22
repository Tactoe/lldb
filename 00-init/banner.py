from subprocess import call as run
from os import environ as env

user=env['USER']
run(["figlet", "-f" "shadow", user])
