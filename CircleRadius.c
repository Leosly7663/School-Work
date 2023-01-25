#include<stdio.h>
#include<math.h>

int main(void){
    // intialize the and assign the nessesary variables
    int radius=0, circumference=0, area=0;
    float pi=3.14;


    

    // get user input for radius
    printf("What is your desired radius in m \n");
    scanf("%d",&radius);

    area = pi*pow(radius,2);
    circumference = 2*pi*radius;

    printf("area = %d \n",area);
    printf("circumference = %d \n",circumference);
}