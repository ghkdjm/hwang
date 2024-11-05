#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
	int i, ranval, nseed;
	
	scanf("%d", &nseed);
	srand(nseed);

	printf("+----------------------+\n");
	printf("|123456|123456|12345678|\n");
	printf("+----------------------+\n");

	for (i=0; i<10; i=i+1) {
		ranval = rand()%0xFFFF;

		printf("|%-6d",ranval);
		printf("|0x%.4X",ranval);
		printf("|0o%.6o|\n",ranval);
	}
	printf("+----------------------+\n");

	return 0;
}
