def input_msg(msg):
    return int(input(f"{msg}を入力してください。＞＞"))
     
def calc_payment(amount,people):
    dnum = amount / people # 総額を人数で割り、割り勘額をだす。
    pay = (dnum // 100) * 100 
    if dnum > pay:          # 割り勘額より、payが小さいとき（100円未満を切り捨てていた場合）
        pay = pay + 100     # 100円を足して補完する
    payorg = amount - pay * (people -1) # 幹事の支払額＝総額 - （補完した割り勘額×幹事以外の総人数）
    return [int(pay),int(payorg)]


def show_payment(pay,payorg,people):
    print("***支払額***")
    print(f"1人あたり{pay}円、({people-1}人)、幹事は{payorg}円です。")


# 計算データの入力
amount = input_msg("支払総額")  # amountに支払総額が入力される。（int型）
people = int(input_msg("参加人数を入力してくさい。")) # peopleに参加人数が入力される（int型）


# 割り勘の計算
[pay,payorg] = calc_payment(amount,people)

# 結果の表示
show_payment(pay,payorg,people)