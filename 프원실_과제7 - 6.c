#include <stdio.h>
#include <math.h>

double findroot_exhaustive(double x, double epsilon);	
double findroot_bisection(double x, double epsilon);

/**
* @brief : Find an approximation to the square root of a non-negative number using the Newton's method. 
* @return: An approximation to the square root. The square of it should be in the range [x-epsilon, x+epsilon].
          -1 if it can't find an answer.
* @param : x - target number, epsilon - the allowed difference 
*/
double findroot_newton(double x, double epsilon) {
	double ans = x / 2.0;
	int numGuesses = 0;
	
	double diff = fabs(ans * ans - x);
	
	while (diff >= epsilon && numGuesses < 1000) {
		ans = (ans + x/ans)/2.0;
		diff = fabs(ans * ans -x);
		numGuesses = numGuesses + 1;
	}
	
	printf("# of Guesses = %d\n", numGuesses);
	if (ans * ans <= x + epsilon && ans * ans >= x - epsilon) {
		return ans;
	}
	else {
		return -1;
	}
}

int main(void) {
	double x;
	double epsilon = 0.001;

	scanf("%lf",&x);
	
	if (x > 0) {
		printf("[EXHAUSTIVE] sqrt(%lf) ~= %.20lf\n",x,findroot_exhaustive(x,epsilon));
		printf("[BISECTION ] sqrt(%lf) ~= %.20lf\n",x,findroot_bisection(x,epsilon));
		printf("[  NEWTON  ] sqrt(%lf) ~= %.20lf\n",x,findroot_newton(x,epsilon));
		printf("[  MATH.H  ] sqrt(%lf) ~= %.20lf\n",x,sqrt(x));
	}	

	return 0;
} 

