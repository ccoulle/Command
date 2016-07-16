import manager

class Command(object):
  def __init__(self, n):
    self.name = n
  def execute(self, data): pass
  def undo(self): pass
  def __repr__(self):
    return self.name

class UndoCommand(Command):
  def __init__(self):
    Command.__init__(self, "Undo")
  def execute(self, data):
    if len(manager.Manager.commandStack) > 0:
      cmd = manager.Manager.commandStack[-1]
      manager.Manager.commandStack.pop()
      cmd.undo(data)

class InsertCommand(Command):
  def __init__(self):
    Command.__init__(self, "Insert")
    self.number = int(raw_input("Type number to Insert: "))
  def undo(self, data):
    data.remove(self.number)
  def execute(self, data):
    print "inserting: ", self.number
    data.append(self.number)

class SortCommand(Command):
  def __init__(self):
    Command.__init__(self, "Sort")
  def undo(self, data):
    data[:] = self.tempList
  def execute(self, data):
    self.tempList = data[:]
    data.sort()

class PrintCommand(Command):
  def __init__(self):
    Command.__init__(self, "Print")
  def execute(self, data):
    print "The list is: "
    for x in data: print x, "\t",
    print

class QuitCommand(Command):
  def __init__(self):
    Command.__init__(self, "Quit")
  def execute(self, data):
    import sys; sys.exit()
    answer = raw_input("So you really, really want this (y/n): ")
    if answer == 'y': 
      import sys; sys.exit()
      print "Terminating..."

class RemoveCommand(Command):
  def __init__(self):
    Command.__init__(self, "Remove")
    self.number = int(raw_input("Type number to remove: "))
  def undo(self, data):
    data.insert(self.index, self.number)
  def execute(self, data):
    self.index = data.index(self.number)
    print "Removing: ", self.number
    data.remove(self.number)

