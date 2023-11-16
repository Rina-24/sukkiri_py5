def input_scores(name):
    print(f"{name}さんの試験結果を入力してください。")
    network = int(input("ネットワークの得点？＞＞"))
    database = int(input("データベースの得点？＞＞"))
    security = int(input("セキュリティーの得点？＞＞"))
    scores = [network,database,security]
    return scores

def calc_avarage(scores):
    avg = sum(scores) / len(scores)
    print(f"平均点は{avg}です。")
    return avg

def output_result(name,avg):
    print(f"{name}さんの平均点は{avg}です。")