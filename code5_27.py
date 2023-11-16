def eat(breakfast,lunch,dinner="カレー",*dessert):
    print(f"朝は{breakfast}をたべました。")
    print(f"昼は{lunch}をたべました。")
    print(f"晩は{dinner}をたべました。")
    for d in dessert:
       print(f"おやつに{d}を食べました。")

eat("トースト","パスタ","カレー",("アイス","チョコ","パフェ"))
