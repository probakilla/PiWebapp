class GitRepo(object):

    def __init__(self, name, http_addr, ssh_addr):
        self.name = name
        self.http_addr = http_addr
        self.ssh_addr = ssh_addr