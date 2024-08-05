for _ in range(T := int(input())):
    R, S = input().split()
    P = str()
    for char in S:
        P += char * int(R)
    print(P)

#Description
'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''
#Input
'''
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
'''
#Output
'''
각 테스트 케이스에 대해 P를 출력한다.
'''

#Solution
'''
R, S를 모두 str로 입력받음
빈 str인 P를 만들고 입력받은 S를 for 문을 통해 순회하며 각 단어에 R을 곱하여 P에 추가함
이때, 처음에 R을 str으로 입력을 받았기에 int()를 통해 자료형을 바꿔서 곱해야함
'''