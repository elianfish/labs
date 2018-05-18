#include <iostream>
using namespace std;

void printdigitalgraphics(int x)
{
	int l,n;
	for( l=1;l<=x;l++ )
	{
		for( n=0;n<l;n++ )
		{
			printf("%d",l);
		}
		printf("\n");
	}
}

int main()
{
    printdigitalgraphics(4);
}


