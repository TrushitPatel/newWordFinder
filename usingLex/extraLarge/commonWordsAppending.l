%{
#include<stdio.h>
FILE *out;
%}
%%
.* {fprintf(out,"\" %s \"|\n",yytext);}
%%
int main()
{
	FILE *fp;
	fp=fopen("commonWords.txt","r");
	out=fopen("concatedWords.txt","w");
	yyin=fp;
	yylex();
	fclose(fp);
	fclose(out);
	return 0;
}


