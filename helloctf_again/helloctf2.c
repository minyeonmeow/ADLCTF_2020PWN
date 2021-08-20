#include<stdio.h>

void u_cant_see_me()
{
	printf("I don't play the same trick ^.<\n");
	system("/bin/sh");	
}

int main()
{
	char buf[0x30];

	setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
	
    printf("Let's cheer for CTF again <3!\n");
	printf("CTF!!\n");
	gets(buf);

	printf("CTF %s!!!!!!!\n", buf);

	return 0;
}
