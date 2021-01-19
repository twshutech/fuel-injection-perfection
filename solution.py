class node:
  def __init__(self, n):
    self.pellets = n
    self.left = None
    self.right = None

  def sub_nodes(self):
    if self.pellets % 2 == 0:
      self.left = node(self.pellets // 2)
    else:
      # print 'parent',self.pellets,'has',[self.pellets + 1, self.pellets - 1]
      self.left = node(self.pellets + 1)
      self.right = node(self.pellets - 1)

def fuel_control(pellets):
  current_level = []
  foot_print = [n for row in pellets for n in row]
  for n in pellets[-1]:
    # print 'n',n
    c = node(n)
    c.sub_nodes()

    if c.left != None and c.left.pellets not in current_level and c.left.pellets not in foot_print:
      current_level.append(c.left.pellets)
    if c.right != None and c.right.pellets not in current_level and c.right.pellets not in foot_print:
      current_level.append(c.right.pellets)
  pellets.append(current_level)
  # print 'current_level',current_level
  if 1 not in current_level:
    fuel_control(pellets)
  else:
    # print 'foot_print',foot_print
    # print 'pellets',pellets,
    for raw in pellets:
      print raw
    return len(pellets)-1

def solution(n):
  global moves
  moves = []
  moves.append([int(n)])
  fuel_control(moves)
  return len(moves) -1


def ask():
  print 'Insert random integer as destination from 1.'
  destination = input()
  if destination == 0:
    return
  else:
    print 'It took ',solution(destination),'moves to reach destination', destination
    ask()
ask()
