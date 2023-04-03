import os
print('''\033[1;36;40mWifi_Hack Installer By Ahsanullah
Your Device Must Be Rooted
If Any Question,
Contact Me On 014033232... i'm kidding
FB:Sorry boro FB Nai \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/MDAhsanullah/ahsanwifihack")

os.system("cd ..;chmod +x ahsanwifihack/ahsanwifihack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python ahsanwifihack/ahsanwifihack.py -i wlan0 -K")
