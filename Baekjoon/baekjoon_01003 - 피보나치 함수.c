#include <stdio.h>

void fib_cnt(int n, int cnt[]) {
    if (n == 0) return;

    int temp = cnt[1];
    cnt[1] = cnt[0] + cnt[1];
    cnt[0] = temp;

    fib_cnt(n-1, cnt);
}

int main() {
    int T;
    scanf("%d", &T);

    for (int i=0; i<T; i++) {
        int N;
        int cnt[2] = {1, 0};
        scanf("%d", &N);

        fib_cnt(N, cnt);

        printf("%d %d\n", cnt[0], cnt[1]);
    }
    return 0;
}

//Description
/*
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
*/
//Input
/*
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
*/
//Output
/*
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.
*/

//Solution
/*
입력을 받았을 때 출력값을 보면
--------------------------------
    |   0       1
--------------------------------
0   |   1       0
1   |   0       1
2   |   1       1
3   |   1       2
4   |   2       3
5   |   3       5
6   |   5       8
.   |   .       .
.   |   .       .
.   |   .       .
--------------------------------
과 같음
N을 입력받았을 때, N-1의 출력값에서 1의 개수가 N에서의 0의 개수가 되고, 두 수의 합이 1의 개수가 되는 것을 볼 수 있음

이를 이용해 cnt라는 배열을 {1, 0}으로 정의하고, fib_cnt 함수를 정의해 0이 될 때 까지 재귀로 실행되도록 함
앞에서 말한 알고리즘에 따라 0이면 그대로 반환하고, 그렇지 않으면 cnt[0]을 cnt[1]로, cnt[1]을 cnt[0] + cnt[1]로 저장함
마지막에 cnt를 출력함
*/