#include <stdio.h> 

int main(void) {
	unsigned int b, e, i;
	unsigned int x, y, sum=0;

	scanf("%d%d", &b, &e);
	scanf("%d%d", &x, &y);

	for (i=b; i<=e; i++) {
		if (!(i%x)||!(i%y)) {
			sum += i;
			printf("%d ", i);
		}
	}

	printf("\nsum == %d\n", sum);
	return 0;
}
