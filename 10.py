# a := 1 '왈러스' 라고 읽는다. (3.8 이상에서 사용가능 )
# 가져오는 값이 0인지 아닌지의 경우에서 많이 사용함
# 스위치문 대타로 사용가능 
# do while 대타로 사용가능 ( while ele := elements.get() :)

f = {
	'a': 10,
	'b': 2,
	'c': 3,
}

if f_c := f.get('a',0): # a가 있으면 진행, 없으면 0
	# 'a' 키가 존재함 
	print('y i have a')
else:
	# 'a'키가 없음 
	print('no')


# 조금 더 깔끔한 식 (스위치를 표현할 경우 : 물론, 문자열로 표현할 수 있겠다. )
if (count := fresh_fruit.get('a',0)) > = 2:
	print('a가 2개 있다.')
elif (count := fresh_fruit.get('b',0)) > = 4:
	print('b가 4개 이상 있다. ')
else:
	pass
