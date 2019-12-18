Map=[".#..#..#..#...#..#...###....##.#....",
".#.........#.#....#...........####.#",
"#..##.##.#....#...#.#....#..........",
"......###..#.#...............#.....#",
"......#......#....#..##....##.......",
"....................#..............#",
"..#....##...#.....#..#..........#..#",
"..#.#.....#..#..#..#.#....#.###.##.#",
".........##.#..#.......#.........#..",
".##..#..##....#.#...#.#.####.....#..",
".##....#.#....#.......#......##....#",
"..#...#.#...##......#####..#......#.",
"##..#...#.....#...###..#..........#.",
"......##..#.##..#.....#.......##..#.",
"#..##..#..#.....#.#.####........#.#.",
"#......#..........###...#..#....##..",
".......#...#....#.##.#..##......#...",
".............##.......#.#.#..#...##.",
"..#..##...#...............#..#......",
"##....#...#.#....#..#.....##..##....",
".#...##...........#..#..............",
".............#....###...#.##....#.#.",
"#..#.#..#...#....#.....#............",
"....#.###....##....##...............",
"....#..........#..#..#.......#.#....",
"#..#....##.....#............#..#....",
"...##.............#...#.....#..###..",
"...#.......#........###.##..#..##.##",
".#.##.#...##..#.#........#.....#....",
"#......#....#......#....###.#.....#.",
"......#.##......#...#.#.##.##...#...",
"..#...#.#........#....#...........#.",
"......#.##..#..#.....#......##..#...",
"..##.........#......#..##.#.#.......",
".#....#..#....###..#....##..........",
"..............#....##...#.####...##."]

quarters = {
  "--":3,
  "-+":2,
  "++":1,
  "+-":0
}

def tang(x,y):
  if y==0:
    return +99999
  return x/y

class rotor:
  def __init__(self, tan, mw, ml, width, lenght, x, y):
    self.tangs=float(tan)
    self.mw=mw
    self.ml=ml
    self.width=width
    self.lenght=lenght
    self.x=x
    self.y=y
    

  def __lt__(self, other):
    if other.mw!=self.mw or other.ml != self.ml:
      return quarters[self.mw+self.ml] < quarters[other.mw+other.ml]
    if other.tangs != self.tangs:
      return self.tangs > other.tangs
    return abs(self.width)+abs(self.lenght) < abs(other.width)+abs(other.lenght)

  def __repr__(self):
    return "x:"+str(self.x)+" y:"+str(self.y)

    
  
class asteroid:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.rotors = list()
    

  def __repr__(self):
    return "x:"+str(self.x)+" y:"+str(self.y)

asters = list()
cy = 0
for line in Map:
  cx = 0
  for point in line:
    if point=="#":
      asters.append(asteroid(cx,cy))
      if cx == 17 and  cy == 22:
        ast1=asters[-1]
    cx += 1
  cy += 1

answer=0

#blah bruteforce again I am disgusted with myself 
for ast2 in asters:
  mw = "+"
  ml = "+"
  width = ast2.x - ast1.x
  lenght = ast2.y - ast1.y
  if width < 0:
    mw = "-"
  if lenght < 0:
    ml = "-"
  tan = tang(width, lenght)
  if width==lenght==0:
    continue
  ast1.rotors.append(rotor(tan,mw,ml,width,lenght, ast2.x, ast2.y))

ast1.rotors.sort()

q = list(ast1.rotors)
index = 0
last = q.pop(0)
fin = False
destroyed = 1 
needed = 200
while not fin:
  while index < len(q):
    if q[index].tangs == last.tangs and q[index].ml == last.ml and q[index].mw == last.mw:
      index += 1
    else:
      last = q.pop(index)
      destroyed += 1

    if destroyed >= needed:
      fin=True
      break

print(last)

