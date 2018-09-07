%{
#include<stdio.h>
%}

%%

%%
int main()
{
	FILE *fp;
	fp=fopen("concatnatedEexpression.txt","r");
	yyin=fp;
	yylex();
	fclose(fp);
	return 0;
}
