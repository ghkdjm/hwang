#include <stdio.h> 

int csv_get_value(char str[]) {
    static int i = 0;
	int value = 0;

	if (str[i] == '\0') {
		return -1;
	}
	else if (str[i] == ',') {
		i++;
	}
	while (str[i] >= '0' && str[i] <= '9') {
		value = value * 10 + (str[i] - '0');
		i++;
	}
	return value;
}

int main(void) {
	int num;
	char str[]="123,456,789,305,409,123";

	while ((num=csv_get_value(str))>=0)
		printf("%d\n",num);
	return 0;
}