%{
#include<stdio.h>
FILE *out;
%}
%%
.* {fprintf(out,"%s",yytext);}
%%
int main()
{
	FILE *fp;
	fp=fopen("concatedWords.txt","r");
	out=fopen("finalProgram.l","w");
	yyin=fp;
	fprintf(out,"%s","\%{\n#include<stdio.h>\nFILE *out;\n\%}\ntag <[^><]*>\nnumber [0-9]*[.,:->]*\nother [-]*\ndoubleNewLine \\n\\n\nsingleNewLine \\n\n\%\%\n{tag} {}\n{number} {}\n{other} {}\n[\"].*[\"] {}\n{doubleNewLine} {}\n{singleNewLine} {}\n");
	yylex();
	fprintf(out,"%s"," {unput(yytext[yyleng-1]);}\n\n\%\%\nint main()\n{\n\tFILE *fp;\n\tfp=fopen(\"capitalizedData.txt\",\"r\");\n\tout=fopen(\"output.txt\",\"w\");\n\tyyin=fp;\n\tyylex();\n\tfclose(fp);\n\tfclose(out);\n\treturn 0;\n}");
	fclose(fp);
	fclose(out);
	return 0;
}


