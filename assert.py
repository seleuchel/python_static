
# assert
# --------------------------------------------------

def test(t):
	assert type(t) is str, '이상한 값!'

k_l = ['a','b','c',1]

for i in k_l:
	test(i)

# AssertionError: 이상한 값!

