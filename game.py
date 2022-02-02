from datetime import datetime

States = {
  "UNKNOWN": 0,
  "GAME_OPEN": 1,
  "METAMASK": 2,
  "LOADING": 3,
  "GAME_SELECT": 4,
  "TREASURE": 5,
  "HERO_TAB": 6,
  "HERO_LIST": 7,
}

class Game:
  def init(self, id = 0, frame = (0, 0, 0, 0)):
    self.id = id
    self.runtime = datetime.now()
    self.frame = frame
    self.status = States["UNKNOWN"]

  def setFrame(self, frame):
    self.frame = frame

  def findGame(self):
    return

  def startGame(self):
    return

  def clickTreasure(self):
    return

  def clickWork(self):
    return

  def clickRest(self):
    return

  def findState(self):
    return

game1 = Game()
game1.init(id = 1)

game2 = Game()
game2.init(id = 2)

print(game1.id, game1.status)
print(game2.id, game2.status)

