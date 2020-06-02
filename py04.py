# https://wellness.hpa.gov.tw/App_Prog/Weight_Calculate.aspx
# https://depart.femh.org.tw/dietary/3OPD/BMI.htm

'''
標準體重，其計算公式：
男性： （身高cm－80）×70﹪
女性： （身高cm－70）×60﹪
身體質量指數（Body Mass Index，縮寫為BMI），其計算公式：
    BMI = 體重 (kg) / 身高 (m2)


    BMI ＜ 18.5      體重過輕
    18.5≦BMI＜24     正常範圍
    24≦BMI＜27       過重
    27≦BMI＜30       輕度肥胖
    30≦BMI＜35      中度肥胖
    BMI≧35          重度肥胖　
'''
gender = int(input('性別 1)男 2)女：'))

if (gender == 1) or (gender == 2):
    height = float(input('身高(cm)：'))
    weight = float(input('體重(kg)：'))
    # 身高輸入範圍限制130公分~250公分
    # 體重輸入範圍限制2公斤~400公斤
    if (130 <= height <= 250) and (2 <= weight <= 400):
        if gender == 1:
            sw = (height - 80) * 0.7
        else:
            sw = (height - 70) * 0.6

        bmi = weight / (height/100)**2

        if bmi >= 35:
            result = '重度肥胖'
        elif bmi >= 30:
            result = '中度肥胖'
        elif bmi >= 27:
            result = '輕度肥胖'
        elif bmi >= 24:
            result = '過重'
        elif bmi >= 18.5:
            result = '標準'
        else:
            result = '體重過輕'

        print(f'''性別：{'男' if gender==1 else '女'}     身高：{height}cm     體重：{weight}kg
------------------------------------------
理想體重：{sw:.2f}kg
BMI：{bmi:.2f}
判別：{result}''')
    else:
         print('身高輸入範圍限制130公分~250公分\n體重輸入範圍限制2公斤~400公斤\n請依範圍輸入!')

else:
    print('請重新執行，輸入正確性別')