# 8, 9 

# rang 보다는 enumerate
from random import randint

flavor_list = ['a','b','c','d','e','f']
for i in flavor_list:
	print(f'{i} hello')

# 여기서 헷갈리는 내용 
# enumerate
# 쉽게 ) iterable 가능한 요소의 인덱스와 요소를 같이 반환한다! (튜플로) 
# 인덱스 번호와 컬렉션의 원서를 tuple 형태로 반환 

enu = enumerate(flavor_list) # 2번째 인자는 어디서부터 수를 셀지 결정이 가능함 
for m, n in enu:
	print(m, n) # 0, a  / 1, b / 

# iterator 
# iterator : 반복가능한 객체 (list, dict, set, str, bytes, tuple, rnage)
# 값을 차례대로 거낼 수 있음 (iter()) __iter__
# 다 나오면 StopIteration 예외 발생 
# __next__()로 호출 가능함 


# generator
# iterator 를 생성해주는 함수. 함수 안에 yield 키워드를 사용함
# 함수의 내부 로컬 변수를 통해 내부 상태가 유지됨 
# 무한한 순서가 있는 객체를 모델링 가능 
# 자연스러운 스트림 처리를 파이프라인 구성 가능 

# yield키워드를 사용해 generator 만들기 가능 
# 암시적으로 return 이 호출 (yield 까지 호출됨)

def test_generator():
	yield 1
	yield 2
	yield 3

g = test_generator() # 이렇게 지정을 하고 불러야 매번 다른 값이 출력됨 

print(next(g))
print(next(g))
print(next(g))
print(next(g))

k = test_generator()

for kk in k: # iterable 하므로 호출가능함 
	print(kk)


# other 

def test_generator1():
	a = ['a','b','c']
	yield from a

c = test_generator1()
print(next(c)) # a
print(next(c)) # b
print(next(c)) # c
# print(next(c)) => stop iteration err

# zip
# iterable 한 객체를 인수로 받으며 동일한 개수로 이루어진 자료형을 묶어서 iterabtor로변환 
a = zip([1,2,3],['a','b','c'])
print(next(a)) # 1 a
print(next(a)) # 2 b
print(next(a)) # 3 c 
# 이런 식으로 같이 출력되니까(길이가 같은 것은 ) 그래서 zip이 유용함 
# zip은 둘 중 하나가 끝나면 출력도 끝난다
# 없는 것을 사용하고 싶으면, zip_longest (itertools의)를 사용할 수 있다. 


