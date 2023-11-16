num = 5

# 値渡し
def add_num(num):
    num += 5
print(num)

  # 実行結果は5になる



# 参照渡し
scores = [1,1,2]

def add_scores(scores):
    scores[0] += 5

add_scores(scores)
print(scores)

# 実行結果は[6,1,2]