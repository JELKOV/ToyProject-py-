# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 
# 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 
# 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.


# 그리디 알고리즘 
## 사람들 몸무게 정렬

### 몸무게가 가벼운 사람 + 무거운사람 묶어준다 -> 몸무게 리스트 오름차순 정렬
### 리스트의 앞 / 리스트의 뒤
def solution(사람들, 제한무게):
    # 구명보트 개수
    보트_수 = 0
    
    # 사람들의 몸무게를 오름차순으로 정렬
    사람들.sort()

    # 가장 가벼운 사람과 가장 무거운 사람을 가리키는 포인터
    가벼운_사람 = 0
    무거운_사람 = len(사람들) - 1

    # 모든 사람이 구출될 때까지 반복
    while 가벼운_사람 <= 무거운_사람:
        # 두 사람이 함께 탈 수 있는 경우
        if 사람들[가벼운_사람] + 사람들[무거운_사람] <= 제한무게:
            가벼운_사람 += 1  # 가벼운 사람 태움

        # 무거운 사람은 항상 태움
        무거운_사람 -= 1
        보트_수 += 1  # 보트 하나 사용
    
    return 보트_수
