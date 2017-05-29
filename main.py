from command_line import DomainCmd
from controller import Controller

if __name__ == '__main__':
    con = Controller()
    cmdView = DomainCmd(con)
    cmdView.arg()
    cmdView.cmdloop()
