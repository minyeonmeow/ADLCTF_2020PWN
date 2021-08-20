#include<stdio.h>
#include<stdlib.h>

void lucky(){
    unsigned long random = rand() % 1000; //random value between 0-999
    
    unsigned long bet;
    unsigned long lucky_number;

    printf("Place your bets (minimum is $100) : ");
    scanf("%d", bet); //wrong usage
    fflush(stdin);

    printf("Guess your number (0-999) : ");
    scanf("%d", lucky_number); //wrong usage

    if (lucky_number == random)
    {
        printf("Gotcha!!\n");
        execve("/bin/sh", 0, 0);
    }
    else{
        printf("You GOT nothing QQ\n");
        exit(0);
    }
}

void welcome(){
    char name[48];
    printf("Welcome to lucky lucky system.\n");
    printf("You have to guess the right number to win the game.\n");
    printf("Who are you ?");
    scanf("%48s", name); 
    printf("Hello %s, let's start the game!\n", name);
}

int main(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    welcome();
    lucky();

    return 0;
}
