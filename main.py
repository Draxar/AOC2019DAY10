Map=[".#..#",
".....",
"#####",
"....#",
"...##"]
def tang(x,y):
  if y==0:
    return "!"
  return x/y

def cotang(x,y):
  if x==0:
    return "!"
  return y/x

class asteroid:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.ats = 0
    self.tangs = list()
    self.cotangs = list()

  def __repr__(self):
    return "x:"+str(self.x)+" y:"+str(self.y)+" ats:"+str(self.ats)

asters = list()
cy = 0
for line in Map:
  cx = 0
  for point in line:
    if point=="#":
      asters.append(asteroid(cx,cy))
    cx += 1
  cy += 1

answer=0

#blah bruteforce again
for ast1 in asters:
  for ast2 in asters:
    if ast1.x==2 and ast1.y==2:
      print("------")
      print(ast2)
    width = ast2.x - ast1.x
    lenght = ast2.y - ast1.y
    tan = tang(width, lenght)
    ctan = cotang(width, lenght)
    if ast1.x==2 and ast1.y==2:
      print("WIDTH:"+str(width)+" lenght:"+str(lenght))
      print("tan:"+str(tan)+" ctan:"+str(ctan))
    if tan==ctan=="!":
      continue
    ok = True
    for i in range(len(ast1.cotangs)):
      if str(tan) == ast1.tangs[i] and str(ctan) == ast1.cotangs[i]:
        ok = False
        break
    if ok:
      if ast1.x==2 and ast1.y==2:
        print("acc")
      ast1.tangs.append(str(tan))
      ast1.cotangs.append(str(ctan))
      ast1.ats += 1
  print(ast1)
  if answer<ast1.ats:
    answer=ast1.ats
    ansast = ast1

print(answer)
print(asters[3])
print(asters[3].cotangs)
print(asters[3].tangs)
    

