#include <stdio.h> 

int main() {
    unsigned int a, b, c;

    while (1) {
        scanf("%d %d %d", &a, &b, &c);

        if (a == 0 && b == 0 && c == 0) break;

        if (c > a && c > b) {
            if (a*a + b*b == c*c) printf("right\n");
            else printf("wrong\n");
        }
        else if (b > a && b > c) {
            if (a*a + c*c == b*b) printf("right\n");
            else printf("wrong\n");
        }
        else {
            if (b*b + c*c == a*a) printf("right\n");
            else printf("wrong\n");
        }
    }

    return 0;
}

//Description
/*
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
*/
//Input
/*
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다.
각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.
*/
//Output
/*
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
*/

//Solution
/*
양의 정수 a, b, c를 한 줄에 입력받음
이때, a, b, c 중 가장 큰 값이 직각삼각형의 빗변이므로 a가 가장 큰 경우, b가 가장 큰 경우, c가 가장 큰 경우로 나눔
각각의 경우에 다른 두 수의 제곱의 합이 가장 큰 수의 제곱과 같으면 right를, 아니라면 wrong을 출력함

이때, while문을 이용해 참인 경우에 계속 반복하여 입력을 받고,
0 0 0을 입력받으면 break를 통해 반복문을 종료함
*/