// Lab 2
// Prepared by: Spencer Ploeger
// ENGG*1410, F22
// This program contains some compile and runtime errors

// Use the debugging tools listed in the Lab 2 document (print, gdb, assertions) to find and fix the errors
// Deliverables:
// - Fix the program and demo it to a TA. Be prepared to show at least 2 debudding techniques
// - Write a brief lab report and submit it to the correct dropbox before the end of the lab
// - Your lab report needs to discuss the debudding techniques you used, as well as some of the errors you fixed. Where they compile or run time?
// Report can be very brief and informal, a page or less is okay.

#include <stdio.h>
#include <math.h>
#include <assert.h>

int main(void){
    char welcomePrompt[100] = "Enter an amount: "; // the welcome prompt
    char answerMsg[100] = "With tax added: "; // the message printed after tax is calculated

    float taxPercent = 0.13; // what percent tax to use


    float amount1, amount2, amount3;

    assert(taxPercent < 1);

    amount1 = 50;
    amount2 = 20;


    printf("%s", welcomePrompt);
    scanf("%f", &amount3);

    float taxAmount = amount3 * (taxPercent);
    float totalAmount = amount3 + taxAmount;

    printf("%s", answerMsg);
    printf("$%.2f\n", totalAmount);

}
