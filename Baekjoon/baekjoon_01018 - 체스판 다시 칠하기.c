#include <stdio.h>

int main() {
    int M, N;
    scanf("%d%d", &M, &N);

    char board[M][N];
    int i, j;
    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            scanf(" %c", &board[i][j]);
        }
    }

    int x, y;
    int cnt1, cnt2;
    int min = M * N;    //가능한 가장 큰 값으로 설정

    for (x = 0; x <= M - 8; x++) {
        for (y = 0; y <= N - 8; y++) {
            cnt1 = 0;   //W로 시작
            cnt2 = 0;   //B로 시작

            for (i = x; i < x + 8; i++) {
                for (j = y; j < y + 8; j++) {
                    if (((i - x) + (j - y)) % 2 == 0) {     //합이 짝수인 칸
                        if (board[i][j] != 'W') cnt1++;
                        if (board[i][j] != 'B') cnt2++;
                    } else {                                //합이 홀수인 칸
                        if (board[i][j] != 'B') cnt1++;
                        if (board[i][j] != 'W') cnt2++;
                    }
                }
            }
            int current_min;
            if (cnt1 < cnt2)
                current_min = cnt1;
            else
                current_min = cnt2;

            if (min > current_min)
                min = current_min;
        }
    }
    printf("%d\n", min);

    return 0;
}

//Description
/*
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
*/
//Input
/*
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
B는 검은색이며, W는 흰색이다.
*/
//Output
/*
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.
*/

//Solution
/*
M, N을 입력받고, 보드를 입력받을 때에는 " %s"로 공백을 앞에 두어 줄바꿈을 무시함
처음에 min은 가능한 가장 큰 값인 M*N으로 정의함

체스판은 w로 시작하거나, B로 시작하는 두 가지의 경우의 수가 있음
즉,
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
WBWBWBWB    BWBWBWBW
BWBWBWBW    WBWBWBWB
중 하나의 모양임
두 가지 경우를 모두 확인하고, 둘 중 다시 칠하는 개수가 더 작은 경우를 저장해야함
M*N의 이차원 배열을 8*8 크기의 배열로 잘라서 모든 경우를 비교하고, 그 중 가장 작은 값을 출력해야함
이때 W로 시작하는 경우를 보면, 각각의 원소를 좌표(x,y)로 본다면 W가 위치한 곳의 두 좌표의 합(x+y)은 짝수이고 B가 위치한 곳은 홀수임
B로 시작하는 경우는 그와 반대가 됨
그러므로 각각의 8*8 크기의 배열에서 좌표의 합이 짝수인 곳과 아닌 곳을 비교하여 칠해야하는 곳의 개수를 구할 수 있음

cnt1을 W로 시작한다고 생각했을 때의 칠해야하는 개수, cnt2를 B로 시작한다고 생각했을 때의 칠해야하는 개수로 놓음
두 좌표의 합이 짝수일 때와 홀수일 때를 나누고
짝수일 때, 그 칸이 W가 아니면 cnt1에 1을 더하고 B가 아니면 cnt2에 1을 더함(if-else로 구현해도 됨)
홀수일 때는 그 반대로 함
current_min이라는 변수를 for문 안에서 정의하고, cnt1과 cnt2 중 더 작은 값으로 설정함
current_min이 min보다 작으면 min으로 설정함
반복문이 종료되면 가장 적게 칠하는 경우에 칠하는 개수가 min에 저장됨
*/
