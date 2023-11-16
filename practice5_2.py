this_year = int(input("現在の西暦を入力してください。>>")) 

def is_leapyear(year):
    return (year % 400 == 0 or (year % 4 == 0 and y % 100 !=0))
   
if is_leapyear(this_year):
    print(f"西暦{this_year}はうるう年です。")
else:
    print(f"西暦{this_year}はうるう年ではありません。")