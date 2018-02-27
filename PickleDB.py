import pickle

class pickleDB:

    def __init__(self, pickleLoc):
        self.pickleLoc = pickleLoc
        self.cached = []

    def loadDB(self):
        try:
            with open(self.pickleLoc, 'rb') as localPickle:
                self.cached = pickle.load(localPickle)        
        except (OSError, IOError) as e:
            #new DB init
            self.saveDB()

    def saveDB(self):
        with open(self.pickleLoc, 'wb') as localPickle:
            pickle.dump(self.cached, localPickle)

    def isCached(self, key):                
        return key in self.cached

    def addToCache(self, key):        
        self.cached.append(key)        
        self.saveDB()