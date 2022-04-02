# 키가 있는 경우, 없는 경우를 처리할 때,
# 2번 딕셔너리에 접근하는 것은 비효율적이야
# get 메소드의 두 번째 인자를 이용하자
# get ( 키, 0 )하면, 키에 대한 값이 없을 때 0을 반환한다. 

# 딕셔너리에 키에 맞는 값이 없는 경우

count = counters.get(key,0)
counters[key] = count + 1

# 이런 식으로 표현하는 것이 가장 깔끔하다. 

# 10번하고 같이 사용하면 더 편하다.
if (names := votes.get(key)) is None:
	votes[key] = names = [] # none (키가 없으면, 이것을 처리)

names.append(who)

# 아니면, 딕셔너리의 setdefault 메소드를 사용
names = votes.setdefault(key, []) # 키가 없으면, []가 자동으로 대입
names.append(who)

# 근데, 이것은 setdefault의 동작을 나타낼 수가 없대!!! ... 읽기 쉬운코드...읽기 쉬운코드..
# 그리고 얕은 복사로 default 값이 사용된대.. (독립성을 보장하기 어려움)
