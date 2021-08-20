#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

void init(){
	setvbuf(stdin,0,2,0);
	setvbuf(stdout,0,2,0);
	setvbuf(stderr,0,2,0);
	}


int main(){
	pid_t pid;
	int status;
	
	init();

	pid = fork();
	if (pid == -1){
		perror("fork error");
		exit(EXIT_FAILURE);
	}
	else if (pid == 0){  //child process
		char buf[0x10];
		puts("Where is my daddy QQ");
		read(0, buf, 0x30);
		printf("%s",buf); //leak canary
		exit(0);
	}
	else{
		waitpid(pid, &status, 0);
		char buf[0x10];
		puts("Could u help me find my children?");
		read(0, buf, 0x50); //not enough for rop -> stack pivot..?
		printf("%s", buf);
	}
    return 0;
}
