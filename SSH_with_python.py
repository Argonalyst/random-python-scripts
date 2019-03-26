# -*- coding: utf-8 -*-

from paramiko import SSHClient
import paramiko

k = paramiko.RSAKey.from_private_key_file("path_to_encrypted_key", password='password_encrypted_key')
 
class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname='ip_address', username='username', pkey = k)
 
    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print stdout.read()
 
if __name__ == '__main__':
    ssh = SSH()
    ssh.exec_cmd("ls")