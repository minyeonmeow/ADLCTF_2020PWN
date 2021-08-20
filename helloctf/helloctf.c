#include<stdio.h>

void u_cant_see_me()
{
	execve("/bin/sh", 0, 0);	
}


int main()
{
	char buf[0x10];
	setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
	printf("I say CTF u say HURRAHHHHH!!\n");
	printf("CTF!!\n");
	gets(buf);

	printf("CTF %s!!!!!!!\n", buf);

	return 0;
}
