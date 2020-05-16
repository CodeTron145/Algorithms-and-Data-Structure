#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct ListElement {
    int data;
    struct ListElement * next;
} ListElement_type;


void show(ListElement_type *head);
void find(ListElement_type *head, int position);
void merge(ListElement_type **head1, ListElement_type **head2);
int list_size(ListElement_type *head);
void push_front(ListElement_type **head, int number);
void push_back(ListElement_type **head, int number);
void push_by_index(ListElement_type **head, int number, int position);
void pop_front(ListElement_type **head);
void pop_back(ListElement_type **head);
void pop_by_index(ListElement_type **head, int position);

int main() {
    ListElement_type *head1;
    head1 = (ListElement_type *) malloc(sizeof(ListElement_type));
    head1 = NULL;

    ListElement_type *head2;
    head2 = (ListElement_type *) malloc(sizeof(ListElement_type));
    head2 = NULL;

    double time_spent = 0.0;

    for (int i = 0; i < 10; i++)
    {
        push_back(&head1, rand() % 100);
        push_back(&head2, rand() % 100);
    }

    printf("Zobaczmy jak działa merge()\n");
    merge(&head1, &head2);
    show(head1);
    show(head2);
    
    printf("Dodawanie elementu z przodu\n");
    push_front(&head1, 65);
    show(head1);

    printf("Dodawanie elementu względnie indeksu\n");
    push_by_index(&head1, 75, 0);
    push_by_index(&head1, 95, 0);
    show(head1);

    printf("Usunięcie elementu z przodu\n");
    pop_front(&head1);
    show(head1);

    printf("Usunięcie elementu z tyłu\n");
    pop_back(&head1);
    show(head1);

    printf("Usunięcie elementu względnie indeksu\n");
    pop_by_index(&head1, 1);
    show(head1);

    printf("Funkcja wyszukiwania elementu w liście\n");
    clock_t begin = clock();
    find(head1, 3);
    clock_t end = clock();

    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Czas działania funkcji %f sekund\n", time_spent);

    return 0;
}

void push_front(ListElement_type **head, int number)
{

    ListElement_type *current;
    current=(ListElement_type *)malloc(sizeof(ListElement_type));

    current->data=number;
    current->next=(*head);
    *head=current;

}

void push_back(ListElement_type **head, int number)
{
    if(*head==NULL)
    {
        *head = (ListElement_type *)malloc(sizeof(ListElement_type));
        (*head)->data = number;
        (*head)->next = NULL;
    }else
    {
        ListElement_type *current=*head;

        while (current->next != NULL) {
            current = current->next;
        }

        current->next = (ListElement_type *)malloc(sizeof(ListElement_type));
        current->next->data = number;
        current->next->next = NULL;
    }
}

void push_by_index(ListElement_type **head, int number, int position)
{
    if(position==0) push_front(head, number);
    else
    {
        if(position==list_size(*head)) push_back(head, number);
        else
        {
            ListElement_type *current=*head;
            ListElement_type *tmp;

            int i=0;
            while (current->next != NULL && i<position-1) {
                current = current->next;
                i++;
            }

            tmp=current->next;
            current->next=(ListElement_type *)malloc(sizeof(ListElement_type));
            current->next->data=number;
            current->next->next=tmp;
        }
    }


}

void pop_front(ListElement_type **head)
{
    ListElement_type * tmp=NULL;

    if (*head!=NULL) {
        tmp=(*head)->next;
        free(*head);
        *head=tmp;
    }

}

void pop_back(ListElement_type **head)
{

    if((*head)->next==NULL)
    {
        *head=NULL;
    }else
    {
        ListElement_type *current=*head;
        while (current->next->next!= NULL) {
            current = current->next;
        }
        free(current->next);
        current->next=NULL;
    }
}


void pop_by_index(ListElement_type **head, int position)
{
    if(position==0) pop_front(head);
    else
    {
        ListElement_type *current=*head;
        ListElement_type *tmp;

        int i=0;
        while (current->next != NULL && i<position-1) {
            current=current->next;
            i++;
        }

        tmp = current->next;
        current->next = tmp->next;
        free(tmp);
    }


}

void show(ListElement_type *head)
{
    printf("\n");
    if(head==NULL) printf("List is empty");
    else
    {
        ListElement_type *current=head;
        do {
            printf("%i", current->data);
            printf("\n");
            current = current->next;
        }while (current != NULL);//może current->next???
    }
}

void find(ListElement_type *head, int position)
{
    ListElement_type *current = head;

    int i = 0;
    while(current->next != NULL && i < position-1)
    {
        current = current->next;
        i++;
    }
    printf("\n");
    printf("%i\n", current->next->data);
}

void merge(ListElement_type **head1, ListElement_type **head2)
{
    ListElement_type *current = *head2;
    ListElement_type *next;

    while (current != NULL)
    {
        push_back(head1, current->data);
        next = current->next;
        free(current);
        current = next;
    }

    *head2 = NULL;
}

int list_size(ListElement_type *head)
{
    int counter=0;
    if(head==NULL) return counter;
    else
    {
        ListElement_type *current=head;
        do {
            counter++;
            current = current->next;
        }while (current != NULL);
    }
    return counter;
}