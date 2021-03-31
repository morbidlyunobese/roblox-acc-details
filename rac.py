version = 1.0

# CREDS TO idiocrasy FOR "HELPING" WITH THE LAST ONLINE |||  github.com/idiocrasy 


import requests, colored, time, os, json, RbxAPI, ctypes, subprocess, random, progressbar
from colored import fg



main = fg('168')
red = fg('1')
white = fg('15')

def bar():
    for i in progressbar.progressbar(range(10)):
        time.sleep(.4)
bar()

subprocess.Popen("cls",shell=True)
time.sleep(1)

Rac = f'[{white}{main}RAC{white}] '
error = f'[{red}ERROR{white}] '

ctypes.windll.kernel32.SetConsoleTitleW(f'R.A.C | v{version} | xq#4300')

print(f'''

{white}                                    ███████████        █████████        █████████ 
                                   ░░███░░░░░███      ███░░░░░███      ███░░░░░███
                                    ░███    ░███     ░███    ░███     ███     ░░░ 
                                    ░██████████      ░███████████    ░███         
{main}                                    ░███░░░░░███     ░███░░░░░███    ░███         
                                    ░███    ░███     ░███    ░███    ░░███     ███
                                    █████   █████ ██ █████   █████ ██ ░░█████████ 
                                    ░░░░░   ░░░░░ ░░ ░░░░░   ░░░░░ ░░   ░░░░░░░░░                       ''')
print(f'                                                         {white}W.{main}I{white}.{white}P                                                  ')

# Input !
name = input(f'    {Rac} Username > {main}')

# Acount Info !
namereq = requests.get(f'https://api.roblox.com/users/get-by-username?username={name}')

rapreq = requests.get(f'https://accountsettings.roblox.com/v1/inventory-privacy?username={name}')
info = namereq.json()
getid = info['Id']

idlook = requests.get(f'https://users.roblox.com/v1/users/{getid}')
info2 = idlook.json()
banstatus = info2['isBanned']

try:
    userrap = RbxAPI.User(getid).rap

except Exception as Lolgr:
    print(f' ')

lastreq = requests.get(f'https://api.roblox.com/users/{getid}/onlinestatus')
lastjson = lastreq.json()
lastonline = lastjson['LastOnline']

# PP Generator !

pp = ""
size = random.randint(1,12)

for _i in range(0, size):
    pp += "="


print(f'       {white} {Rac} Username > ' + info2['name'])
print(f'        {Rac} ID > {getid}')
print(f'        {Rac} Display_Name > ' + info2['displayName'])

try:
    print(f'        {Rac} Rap > {userrap}')

except Exception as RapError:
    print(f'        {Rac} Rap > 0 RAP Or User Invetory Is Closed')
if banstatus == False:
    print(f'        {Rac} Banned > No')

elif banstatus == True:
    print(f'        {Rac} Banned > Yes')

else:
    print("         How...?")

print(f'        {Rac} Description > ' + info2['description'])

if pp >= '========':
    print(f'        {Rac} PP Size: 8{pp}D | Monstrous')

elif pp >= '====' and pp <= '=======':
    print(f'        {Rac} PP Size: 8{pp}D | Average')

else:
    print(f'        {Rac} PP Size: 8{pp}D | Micro')

print(f'        {Rac} Creation Date > ' + info2['created'])
print(f'        {Rac} Last Online > {lastonline}')


print('\n')




print(f'        {Rac} This Program Will Re-Run In 10 Seconds.')

time.sleep(10)
subprocess.Popen("cls",shell=True).communicate()
os.system("python rac.py")
