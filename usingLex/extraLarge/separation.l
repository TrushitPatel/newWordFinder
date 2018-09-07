%{
#include<stdio.h>
FILE *outFrequency,*outWord;
%}

%%
[0-9]* {fprintf(outFrequency,"%s\n",yytext);}
[a-zA-Z]* {fprintf(outWord,"%s\n",yytext);}
%%
int main()
{
	FILE *fp;
	fp=fopen("commonGoogleForum.txt","r");
	outFrequency=fopen("freq.txt","w");
	outWord=fopen("word.txt","w");
	yyin=fp;
	yylex();
	fclose(fp);
	return 0;
}


