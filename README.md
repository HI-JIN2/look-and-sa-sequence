# 개미수열 (Look and Say Sequence)
## 개요
python - 비교적 문자열을 다루기 쉬워서 선정
```
- tests
  - test_main.py
- main.py
```

## 실행 방법 (macOS 기준)
### 콘솔 입력
1. 가상환경 활성화
`source .venv/bin/activate`
2. 의존성 설치
`pip install -r requirements-dev.txt`
2. `python main.py`
3. 콘솔에 n 입력
    <img width="396" height="65" alt="스크린샷 2026-04-25 오후 10 33 54" src="https://github.com/user-attachments/assets/60d12a75-9ad7-490e-b74c-ad8223fb7734" />

### 테스트 실행
`pytest`

## 구현 아이디어
1. 개미수열 구현 [0418ef](https://github.com/HI-JIN2/look-and-sa-sequence/commit/0418ef1f02e9108e452cba07817294828fec6629)  
    숫자의 개수 + 해당 숫자를 문자열에 추가하는 방식으로 각 단계 개미수열을 구함
2. 리스트로 개선 [e353a7](https://github.com/HI-JIN2/look-and-sa-sequence/commit/e353a73b46020bc8a9e6c6b823012933384647b2)  
    시간 복잡도가 걱정 되어 각 단계의 개미수열을 저장하는 arr을 str에서 list로 변경함


## 개선점
이중 반복문이 아쉬움   
재귀나 이전 단계를 저장하는 DP를 사용해볼 수도 있을 것 같음
