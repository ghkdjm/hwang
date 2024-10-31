#include <stdio.h>
/**
* @brief : Get the minimum number of cells to repaint from the given m*n board to make a 8*8 chess board 
* @return: The minimum number of cells to repaint from the given m*n board (>=0)
         : return -1 if m < 8 or n < 8.
* @param : m - # of rows, n - # of columns, 
           board - consists of m*n cells, board[i][j] == 0(painted in black)/1(painted in white)
*/
int min_num_cell_to_repaint(int m, int n, int board[m][n]) {
	int x, y, i, j;
	int cnt1, cnt2;
	int min = m*n;

	for (x=0; x<m-7; x++) {
		for (y=0; y<n-7; y++) {
			cnt1 = 0;
			cnt2 = 0;
			
			for (i=x; i<x+8; i++) {
				for (j=y; j<y+8; j++) {
					if (((i-x)+(j-y))%2 == 0) {
						if (board[i][j] != 1) cnt1++;
                        if (board[i][j] != 0) cnt2++;
					}
					else {
						if (board[i][j] != 0) cnt1++;
                        if (board[i][j] != 1) cnt2++;
					}
				}
			}

			int c_min;
            if (cnt1 < cnt2)
                c_min = cnt1;
            else
                c_min = cnt2;

            if (c_min < min)
                min = c_min;
		}
	}

	return min;
}

int main(void) {
	int board1[8][8] = { {1,0,1,0,1,0,1,0},
						 {0,1,0,1,0,1,0,1},
						 {1,0,1,0,1,0,1,0},
						 {0,1,0,0,0,1,0,1},
						 {1,0,1,0,1,0,1,0},
						 {0,1,0,1,0,1,0,1},
						 {1,0,1,0,1,0,1,0},
						 {0,1,0,1,0,1,0,1}   
					   };
	int board2[10][13] = { {0,0,0,0,0,0,0,0,1,0,1,0,1},
						   {0,0,0,0,0,0,0,0,0,1,0,1,0},
						   {0,0,0,0,0,0,0,0,1,0,1,0,1},
						   {0,0,0,0,0,0,0,0,0,1,0,1,0},
						   {0,0,0,0,0,0,0,0,1,0,1,0,1},
						   {0,0,0,0,0,0,0,0,0,1,0,1,0},
						   {0,0,0,0,0,0,0,0,1,0,1,0,1},
						   {0,0,0,0,0,0,0,0,0,1,0,1,0},
						   {1,1,1,1,1,1,1,1,1,1,0,1,0},
						   {1,1,1,1,1,1,1,1,1,1,0,1,0}
					     };
	// The values of board3 are hidden on purpose
	int board3[11][13] = { {0,0,0,0,0,0,0,0,1,0,1,0,1},
					     };

	int option, n_repaint;

	scanf("%d", &option);

	switch (option) {
		case 1 :
			n_repaint = min_num_cell_to_repaint(8,8,board1);
			break;
		case 2 :
			n_repaint = min_num_cell_to_repaint(10,13,board2);
			break;
		default :
			n_repaint = min_num_cell_to_repaint(11,13,board3);
			break;
	}
	printf("%d\n", n_repaint);
	return 0;
}