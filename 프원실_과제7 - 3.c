#include <stdio.h> 

int hexa2decimal(char hexa_str[]) {
    int i = 2;
	int result = 0;

	while (1) {
		if (hexa_str[i] == '\0') {
			return result;
		}
		else {
			if (hexa_str[i] >= '0' && hexa_str[i] <= '9') {
				result = result * 16 + (hexa_str[i] - '0');
			}
			else {
				result = result * 16 + (hexa_str[i] - 'A' + 10);
			}
			i++;
		}
	}
}

int main(void) {
	char hexa1[] = "0x1F34";
	char hexa2[] = "0x34CD56";
	char hexa3[] = "0x34FD5A";	

	printf("%s = %d\n", hexa1, hexa2decimal(hexa1));
	printf("%s = %d\n", hexa2, hexa2decimal(hexa2));
	printf("%s = %d\n", hexa3, hexa2decimal(hexa3));

	return 0;
}