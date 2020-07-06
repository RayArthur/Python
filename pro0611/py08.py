file = None

try:
    file = open('aqi-1.json', 'r', encoding='utf8')
    print(file.read())
except FileNotFoundError:
    print('找不到檔案!')
except PermissionError:
    print('沒有存取權限!')
except IOError:
    print('其他I/O錯誤!')
except:
    print('其他例外!')
finally:
    if file != None:
        file.close()
        print('close()')