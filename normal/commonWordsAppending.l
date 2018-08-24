%{
#include<stdio.h>
FILE *out;
%}
%%
.* {fprintf(out,"\" %s \"|",yytext);}
%%
int main()
{
	FILE *fp;
	fp=fopen("capitalizedCommonWords.txt","r");
	out=fopen("concatedWords.txt","w");
	yyin=fp;
	yylex();
	fclose(fp);
	return 0;
}


