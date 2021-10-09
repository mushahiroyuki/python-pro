#@@range_begin(list1)
def add_sales_tax(total, tax_rate): # 売上税を追加
    return total * tax_rate # 日本の消費税とは違い、最終消費者のみに課せられる
#@@range_end(list1)

def test():
    total = 1000
    rate = 1.1 # 10%の売上税（日本の消費税とは違い、最終消費者のみに課せられる）
    grand_total = add_sales_tax(total, rate)
    print(f"合計金額={grand_total}")

if __name__ == '__main__': test()  # ほかのプログラムにimportされた場合は実行しない
# 詳細は、『Python基礎&実践プログラミング ［プロへのスキルアップ＋プロジェクトサンプル］』（インプレス）の第10章などを参照
