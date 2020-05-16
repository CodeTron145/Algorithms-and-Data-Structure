#include <stdbool.h>
#include <stdio.h>


#define MAX 1000

int tab[MAX], p = 0, k = 0;

bool pop_back()
{
    if(p==k)
        return 0;

    ++p;
    return 1;
}

bool push_back(int element)
{
    if(k==MAX)
        return 1;

    tab[k++] = element;
    return 1;
}

unsigned int size()
{
    return k-p; //liczba elementów w kolejce
}

int first()
{
    if(p==k) //jesli kolejka jest pusta
        return 1;

    return tab[p];
}

int last()
{
    if(p==k) //jesli kolejka jest pusta
        return 0;

    return tab[k-1];
}
int main()
{
    printf("Dodaję element do kolejki: %d\n", 20);
    push_back(20);
    printf("Dodaję element do kolejki: %d\n", 230);
    push_back(230);
    printf("Dodaję element do kolejki: %d\n", 32);
    push_back(32);
    printf("Dodaję element do kolejki: %d\n", 245);
    push_back(245);
    printf("Dodaję element do kolejki: %d\n", 230);
    push_back(230);
    printf("Dodaję element do kolejki: %d\n", 3);
    push_back(3);

    int element = first();
    printf("Pierwszy element w kolejce: %d\n", element);

    element = last();
    printf("Ostatni element w kolejce: %d\n", element);

    printf("Usuwam element z kolejki");
    pop_back();
    element = first();
    printf("Pierwszy element w kolejce: %d \n", element);

    element = last();
    printf("Ostatni element w kolejce: %d\n", element);
}