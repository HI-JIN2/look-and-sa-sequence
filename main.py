def solution(n):

    result = "1"

    for i in range(1,n):
        before = result[0]
        cnt = 0

        arr = "" #이번에 새로 만들
        for idx,s in enumerate(result):
            #s의 개수 + s


            if s == before: #이전과 같으면 cnt +=1
                # print("같",s)
                cnt += 1
            else:
                # print("달",s)
                arr += str(cnt) + (str(before)) #이전거 붙여야한다

                cnt =1 #리셋
                before = s

        arr += str(cnt) + (str(s)) #마지막 거는 안들어가서 따로 붙여줌
        result = arr

        # print(i, result)

    # 2. 가운데 두 자리수만 리턴한다
    n = len(result)
    idx = n//2
    result = list(result)
    return int("".join(result[idx-1:idx+1]))

if __name__ == '__main__':
    print(solution(5))
    print(solution(8))