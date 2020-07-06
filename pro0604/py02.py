print('若失敗五次就會退出遊戲')

counter = 0
textSolitaire = str(input('請輸入一個字串：'))
while counter < 5:
    msg1 = '請輸入-' + textSolitaire[-1] + '-的字串：'
    keyin = str(input(msg1))
    if keyin[0] == textSolitaire[-1]:
        textSolitaire = textSolitaire + '-' + keyin
        print('上一個字串【', textSolitaire, '】')
    else:
        counter += 1
        msg2 = f'錯誤 {counter} 次,請再次輸入-{textSolitaire[-1]}-的字串' if counter!=5 else '錯誤 5 次,遊戲結束'
        print(msg2)


