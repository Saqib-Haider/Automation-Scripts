class Space():
    def __init__(self, name, info):
        self.name= name
        self.info = info
        self.path = []

    def travel(self, direction):
        return self.path.get(direction, None)
    
    def add_path(self, path):
        self.path.update(path)