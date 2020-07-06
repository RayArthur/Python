import os

class tryopenfile:

    def openfile(self, filename):
        self.file = open(filename, 'w')
        self.file.close()
        pass


if __name__ == '__main__':

    filename = 'data.txt'

    test = tryopenfile()
    test.openfile(filename)

    os.remove(filename)
    print('刪除成功')


