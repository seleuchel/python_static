# 반환값이 많으면 실수하기도 쉬워짐 
# 가독성도 저하됨
# 최대 3개 까지만 사용할 수 있도록 하고 
# 여러 값을 반환해야한다면, 객체 사용합시다. (작은 클래서 or namedtuple)

## namedtuple
from collections import namedtuple

Food = namedtuple('food',['title','price'])
dissert = Food('오늘 저녁 디저트',2100)
print(dissert.title, dissert.price) # 이런 식으로 표현할 수 있다. 

# 간단한 객체처럼
# 인덱싱 가능, 수정은 불가능

