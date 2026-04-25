def solution(n):
    result = "1"

    for _ in range(1, n):
        before = result[0]
        cnt = 0

        arr = []  # 이번에 새로 만들
        for s in result:
            # s의 개수 + s

            if s == before:  # 이전과 같으면 cnt +=1
                # print("같",s)
                cnt += 1
            else:
                # print("달",s)
                arr.append(str(cnt))
                arr.append(before)  # 이전거 붙여야한다

                cnt = 1  # 리셋
                before = s

        arr.append(str(cnt))
        arr.append(before)

        result = "".join(arr)
        # print(result)

    mid = len(result) // 2
    return int(result[mid - 1:mid + 1]) #문제 요구사항: 가운데 두 자리 수를 리턴


if __name__ == "__main__":
    n = int(input().strip())
    print(solution(n))