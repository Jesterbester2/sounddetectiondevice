import os
import glob


class CleanUp:

    def __init__(self, directory):
        self.directory = directory
        self.files = []

    def findfiles(self):
        os.chdir(self.directory)
        for file in glob.glob('*.txt'):
            self.files.append(file)

    def deleteallfiles(self):
        for file in self.files:
            os.remove(self.directory + "/" + file)
