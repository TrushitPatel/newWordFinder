%{
#include<stdio.h>
int counter=0;
FILE *out1,*out2,*out3,*out4;
%}
%%
.* {				
	if(counter<25000)
		{fprintf(out1,"%s",yytext);counter++;}
	else if(counter<50000)
		{fprintf(out2,"%s",yytext);counter++;}
	else if(counter<75000)
		{fprintf(out3,"%s",yytext);counter++;}
	else
		{fprintf(out4,"%s",yytext);counter++;}
	}

%%
int main()
{
	FILE *fp;
	fp=fopen("concatedWords.txt","r");
	out1=fopen("merged1.txt","w");
	out2=fopen("merged2.txt","w");
	out3=fopen("merged3.txt","w");
	out4=fopen("merged4.txt","w");
	yyin=fp;
	yylex();
	fclose(fp);
	fclose(out1);
	fclose(out2);
	fclose(out3);
	fclose(out4);
	return 0;
}
