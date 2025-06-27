a = input()
a_list = list(a)              # 문자열 → 리스트로 변환

a_list[1] = "a"               # 인덱스 1 수정
a_list[-2] = "a"              # 뒤에서 두 번째 문자 수정

a = ''.join(a_list)           # 다시 문자열로 결합
print(a)
