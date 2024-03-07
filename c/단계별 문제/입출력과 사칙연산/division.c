#include <stdio.h>

int main(){
    float num1, num2;
    scanf("%lf %lf", &num1, &num2);
    if(num2 != 0){
        printf("%lf\n", num1 / num2);
    } else{
        printf("zero division");
    }
    return 0;
}