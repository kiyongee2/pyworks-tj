# append() - 요소 추가
a1 = [1, 2, 3, 4, 5]
a2 = []  #빈 리스트
a3 = []

# a1의 요소를 a2에 저장함
for i in a1:
    a2.append(i)
print("a2 =", a2) #a2 = [1, 2, 3, 4, 5]

# a1의 요소중 홀수만 a3에 저장
for item in a1:
    if item % 2 == 1:
        a3.append(item)
print("a3 =", a3) #a3 = [1, 3, 5]

# 빈 리스트에 자료 저장
fruit = []
fruit.append("딸기")
print(fruit) #['딸기']

# 리스트에 여러 개를 추가 - extend(리스트)
fruit.extend(["사과", "감"])
print(fruit) #['딸기', '사과', '감']

fruit.append(["배", "당근"])
print(fruit) #['딸기', '사과', '감', ['배', '당근']]