import sqlite3

def menu():
    print("帳號、密碼管理系統")
    print("-------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號、密碼")
    print("5. 建立資料表")
    print("0. 結  束  程  式")
    print("-------------------------")


def create_table():
    sql = '''CREATE TABLE IF NOT EXISTS user_table(
    'id' TEXT  PRIMARY KEY NOT NULL,
    'password' TEXT NOT NULL)'''

    cursor.execute(sql)

def input_data():
    while True:
        uid = input(' 輸入 ID(按 Enter 結束)：')
        if uid == '': break
        cursor = conn.execute('SELECT * FROM user_table WHERE id="{}"'.format(uid))
        row = cursor.fetchone()
        if row != None:
            print(uid, '帳號已存在!')
            continue
        password = input(' 輸入密碼：')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_table VALUES("{}","{}")'.format(uid, password))
        conn.commit()
        print('新帳號建立完成!')
        print()
        break

def disp_data():
    cursor = conn.execute('SELECT * FROM user_table')
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], '-->', row[1])
    print()

def edit_data():
    while True:
        uid = input(' 輸入 ID(按 Enter 結束)：')
        if uid == '': break
        cursor = conn.execute('SELECT * FROM user_table WHERE id="{}"'.format(uid))
        row = cursor.fetchone()
        if row == None:
            print(uid, '帳號不存在!')
            continue
        password = input(' 輸入新密碼：')
        conn.execute('UPDATE user_table SET password="{}" WHERE id="{}"'.format(password, uid))
        conn.commit()
        print('密碼更新完成!')
        print()
        break


def delete_data():
    while True:
        uid = input(' 輸入要刪除 ID(按 Enter 結束)：')
        if uid == '': break
        cursor = conn.execute('SELECT * FROM user_table WHERE id="{}"'.format(uid))
        row = cursor.fetchone()
        if row == None:
            print(uid, '帳號不存在!')
            continue

        confirm = input('確認刪除 '+ uid + ' (Y/N)：').upper()
        if confirm=='Y':
            conn.execute('DELETE FROM user_table WHERE id="{}"'.format(uid))
            conn.commit()
            print('資料刪除完成!')
        else:
            print(uid, '未刪除!')
        break

### 主程式從這裡開始 ###

conn = sqlite3.connect('account.db')
cursor = conn.cursor()

while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice == 1:
        input_data()
    elif choice == 2:
        disp_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        create_table()
    else:
        conn.close()
        break

print("程式執行完畢！")