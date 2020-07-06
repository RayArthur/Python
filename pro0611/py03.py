def menu():
    print("帳號、密碼管理系統")
    print("-------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號、密碼")
    print("0. 結  束  程  式")
    print("-------------------------")

def read_data():
    with open('password.txt', 'r', encoding='utf8') as file:
        data_str = file.read()
        print(data_str, type(data_str))
        if data_str != '':
            data = eval(data_str)
            return data
        else:
            return dict()

def writer_data(msg):
    with open('password.txt', 'w', encoding='utf8') as file:
        file.write(str(data))
    print(msg)
    print()

def input_data():
    while True:
        uid = input(' 輸入 ID(按 Enter 結束)：')
        if uid == '': break
        if uid in data:
            print(uid, '帳號已存在!')
            continue
        password = input(' 輸入密碼：')
        data[uid] = password
        writer_data('新帳號建立完成!')
        break

def disp_data():
    for k,v in data.items():
        print(k, '-->', v)
    print()

def edit_data():
    while True:
        uid = input(' 輸入 ID(按 Enter 結束)：')
        if uid == '': break
        if not uid in data:
            print(uid, '帳號不存在!')
            continue
        password = input(' 輸入新密碼：')
        data[uid] = password
        writer_data('密碼更新完成!')
        break

def delete_data():
    while True:
        uid = input(' 輸入要刪除 ID(按 Enter 結束)：')
        if uid == '': break
        if not uid in data:
            print(uid, '帳號不存在!')
            continue

        confirm = input('確認刪除 '+ uid + ' (Y/N)：').upper()
        if confirm=='Y':
            del data[uid]
            writer_data('資料刪除完成!')
        else:
            print(uid, '未刪除!')
        break

### 主程式從這裡開始 ###

data = dict()

data = read_data()  # 讀取文字檔後轉換為 dict
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
    else:
        break

print("程式執行完畢！")