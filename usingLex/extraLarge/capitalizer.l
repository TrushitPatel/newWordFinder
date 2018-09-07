%{
#include<stdio.h>
FILE *out;
%}
%%
[a-z] {fprintf(out,"%c",yytext[0]-32);}
[A-Z] {fprintf(out,"%c",yytext[0]);}
[ \t\n-'"/] {fprintf(out,"%c",yytext[0]);}
%%
int main()
{
	FILE *fp;
	fp=fopen("data.txt","r");
	out=fopen("commonWords.txt","w");
	yyin=fp;
	yylex();
	fclose(fp);
	fclose(out);
	return 0;
}


