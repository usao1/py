# 演算子とprintの基本
ten=10
five=5
if ten > five :
    print( str(ten) + "は" + str(five) + "より大きい")

if five < ten :
    print( str(five) + "は、%sより小さい" % ten)

if five != ten :
    print( "%sは、%sではない" % (five,ten))

if five == ten :
    print( "%sは、%sだ" % (five,ten)) # 出力されない
