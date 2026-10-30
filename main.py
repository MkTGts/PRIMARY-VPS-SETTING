import subprocess


class Commands:
    'this class for bash scripts and commands'
    def __init__(self):
        pass


    def _primary_installer(self):
        return f"""
# updating apt
apt update && apt upgrade -y  
echo -e "THE APT UPDATE WAS SUCCESSFUL"

# installing primaty utils
apt install mc htop nano curl wget net-tools dnsutils telnet git nmap ufw -y  
echo -e "THE UTILS UPDATE WAS SUCCESSFUL"
"""


    def _users(self, username):
        return f"""
# add a user and permissions
adduser {username}
usermod -aG sudo {username}
"""


    def _set_ufw(self):
       return f"""
# update ufw
apt update && apt install -y ufw
echo -e "UFW WAS UPDATED SUCCESSFULY"

# set opened ports
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 3096/tcp
echo -e "ALLOW PORTS SETTED SUCCESSFULY"

# set default rules
ufw default deny incoming
ufw default allow outgoing
echo -e "DEFAULT RULES SETTED SUCCESSFULY"

# enable ufw
ufw --force enable
echo -e "UFW ENABLED SUCCESSFULY"
"""
    
    def run_command(self, bash_command):
        subprocess.run(
        bash_command,
        shell=True,
        executable='/bin/bash',
        capture_output=True,
        text=True
        )


class Shower:
    'this class for showing user interface'
    def __init__(self):
        pass

    def hello(self):
        print(
                    """Choose an option:
                    1 - Install primary utilits
                    2 - Add a user
                    3 - Install SSH rules (-)
                    4 - Set UFW rules
                    q - quit
                """)


    def install_primary(self):
        print('1')


    def add_user(self):
        print('2')


    def install_ssh(self):
        print('3')


    def set_ufw(self):
        print('4')


    def _quit(self):
        print("Bye")


class Runner:
    'this class for start and execution'
    def __init__(self, user_said:str):
        self.commands = Commands()
        self.shower = Shower()
        self.user_said = user_said


    def install_primary(self):
        try:
            self.commands._primary_installer()
            self.shower.install_primary()
        except:
            pass


    def add_user(self):
        try:
            self.shower.add_user()
        except:
            pass


    def install_ssh(self):
        try:
            self.shower.install_ssh()
        except:
            pass


    def set_ufw(self):
        try:
            self.shower.set_ufw()
        except:
            pass


    def _quit(self):
        self.shower._quit()
        exit()


    def __call__(self):
        if self.user_said == "q":
            self._quit()
        elif self.user_said == "1":
            self.install_primary()
        elif self.user_said == "2":
            self.add_user()
        elif self.user_said == "3":
            self.install_ssh()
        elif self.user_said == "4":
            self.set_ufw()
        else:
            print(f"Operator {self.user_said} isn't exist. Try again.")



def main():
    while True:
        user_said = str(input("Choose the option: "))
        _runner = Runner(user_said=user_said)
        _runner()



if __name__ == "__main__":
    main()