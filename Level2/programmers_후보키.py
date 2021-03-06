from itertools import combinations


def solution(relation):
    answer = 0

    new_relation = list(map(list, zip(*relation)))
    # [['100', '200', '300', '400', '500', '600'],
    # ['ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'],
    # ['music', 'math', 'computer', 'computer', 'music', 'music'],
    #  ['2', '2', '3', '4', '3', '2']]

    subkeyCount = 0  # 후보키의 수
    subkeyNode = []
    for i in range(len(new_relation)):
        if len(new_relation[i]) == len(list(set(new_relation[i]))):
            subkeyCount += 1
            subkeyNode.append(i)

    return subkeyCount


def main():
    print(solution([
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]))


main()

# 하나의 속성이 유일키 -> 후보키 가능
# 하나의 속성만으로 유일키 -> 이걸 포함한 조합은 후보키가 될 수 없다. -> 왜냐하면 하나의 속성을 제외해도 유일성이 안꺠지기 때문에 최소성 만족 X
# 유일키가 아닌 조합이 유일성을 만족하면 -> 후보키


def solution(relation):

    answer = 0
    # 모든 컬럼의 조합 리스트
    all = list()
    # 유일성 만족하는 조합 리스트
    uniqeIndex = []
    if len(relation) > 0:
        # 컬럼의 개수
        colSize = len(relation[0])
        # 로우의 개수
        rowSize = len(relation)
        # 모든 컬럼의 조합 구하기 (Set형태)
        for i in range(1, colSize + 1):
            # append는 런타임에러가 뜸 append와 extend 비교하여 알아둘 것
            all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
        # 조합들의 유일성 검증
        for comb in all:
            # set에 추가하여 사이즈 비교로 검증
            vaildSet = set()
            # 조합에 해당되는 로우를 하나의 str로 합쳐서 set에 넣음
            for row in range(rowSize):
                temp = ''
                for col in comb:
                    temp += relation[row][col]
                vaildSet.add(temp)
        # 유일성 확인하여 리스트에 추가
        if len(vaildSet) == rowSize:
            uniqeIndex.append(comb)
    # 최소성 검증
    # 삭제대상 Set (최소성 위배)
    delSet = set()
    # 부분집합 여부 확인
    for stdMinElem in uniqeIndex:
        for idx, compMinElem in enumerate(uniqeIndex):
            # 부분집합이면서 자기 자신이 아니라면 상위집합을 삭제 대상에 추가
            if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                delSet.add(uniqeIndex.index(compMinElem))
    # 유일성 - 최소성 위배
    answer = len(uniqeIndex)-len(delSet)
    return answer
