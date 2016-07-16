import command

class Manager(object):
  commandStack = []
  def __init__(self):
    self.data = [18, 93, 9]
    self.commands = ['q', 'p', 'u', 'i', 'r', 's']
    print 'Commands:', self.commands
  def run(self):
    while True:
      cmd = raw_input("Type a command: ") 
      if cmd == "q" or cmd == "exit": 
        cmd = command.QuitCommand()
        cmd.execute(self.data)
      elif cmd == "p": 
        cmd = command.PrintCommand()
        cmd.execute(self.data)
      elif cmd == "u":
        cmd = command.UndoCommand()
        cmd.execute(self.data)
      elif cmd == "i":
        cmd = command.InsertCommand()
        cmd.execute(self.data)
        self.commandStack.append( cmd )
      elif cmd == "r":
        cmd = command.RemoveCommand()
        cmd.execute(self.data)
        self.commandStack.append( cmd )
      elif cmd == "s":
        cmd = command.SortCommand()
        cmd.execute(self.data)
        self.commandStack.append( cmd )
      else:
        print cmd, 'is not a valid command'
        print 'Valid commands:', self.commands
