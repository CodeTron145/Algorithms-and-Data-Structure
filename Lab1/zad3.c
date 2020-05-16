//
// Created by valera on 23.03.2020.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct ListElement {
    int data;
    struct ListElement * previous;
    struct ListElement * next;
} ListElement_type;

void show(ListElement_type *head);
void find(ListElement_type *head, int position);
int list_size(ListElement_type *head);
void push(ListElement_type **head, int number);
void push_by_index(ListElement_type **head, int number, int position);
void merge(ListElement_type **head1, ListElement_type **head2);
void pop(ListElement_type **head);
void pop_by_index(ListElement_type **head, int position);

int main()
{
    ListElement_type *head1;
    (ListElement_type *) malloc(sizeof(ListElement_type));
    head1 = NULL;

    ListElement_type *head2;
    (ListElement_type *) malloc(sizeof(ListElement_type));
    head2 = NULL;

    double time_spent = 0.0;

    for(int i = 0; i < 1000; i++) {
        push(&head1, rand() % 100);
        push(&head2, rand() % 100);
    }

    printf("Zobaczmy jak działa merge()\n");
    merge(&head1, &head2);
    show(head1);
    show(head2);

    printf("Dodawanie elementu\n");
    push(&head1, 61);
    show(head1);

    printf("Dodawanie elementu względnie indeksu\n");
    push_by_index(&head1, 75, 0);
    push_by_index(&head1, 95, 0);
    show(head1);

    printf("Usunięcie elementu z tyłu\n");
    pop(&head1);
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

void push(ListElement_type **head, int number)
{
    if(*head==NULL)
    {
        *head = (ListElement_type *)malloc(sizeof(ListElement_type));
        (*head)->data = number;
        (*head)->previous = (*head);
        (*head)->next = (*head);
    }else
    {
        ListElement_type *current=*head;

        while (current->next != *head) {
            current = current->next;
        }

        current->next = (ListElement_type *)malloc(sizeof(ListElement_type));
        current->next->data = number;
        current->next->previous=current;
        current->next->next = (*head);
        (*head)->previous = current->next;
    }
}

void push_by_index(ListElement_type **head, int number, int position)
{
    if(position == 0)
    {
        ListElement_type *current;
        ListElement_type *tmp;
        tmp = (*head)->previous;
        current = (ListElement_type *)malloc(sizeof(ListElement_type));
        current->data = number;
        current->next = (*head);
        current->previous = tmp;
        tmp->next = current;
        (*head)->previous = current;
        (*head) = current;
    }
    else if(position==list_size(*head)) push(head, number);
    else {
        ListElement_type *current;
        ListElement_type *tmp;

        int i = 0;
        while (current->next != NULL && i < position - 1) {
            current = current->next;
            i++;
        }

        tmp = current->next;
        current->next = (ListElement_type *) malloc(sizeof(ListElement_type));
        current->next->data = number;
        current->next->previous = current;
        tmp->previous = current->next;
        current->next->next = tmp;
    }
}

void pop(ListElement_type **head)
{

    if((*head)->next == (*head))
    {
        *head=NULL;
    }else
    {
        ListElement_type *current=*head;
        while (current->next->next != (*head)) {
            current = current->next;
        }
        free(current->next);
        current->next=(*head);
        (*head)->previous = current;
    }
}


void pop_by_index(ListElement_type **head, int position)
{
    if (position == 0)
    {
        ListElement_type *tmp;
        tmp=(*head)->next;
        tmp->previous = (*head)->previous;
        (*head)->previous->next = tmp;
        free(*head);
        *head=tmp;
    }
    if(position==list_size(*head)) pop(head);
    else {
        ListElement_type *current = *head;
        ListElement_type *tmp;

        int i = 0;
        while (current->next != (*head) && i < position - 1) {
            current = current->next;
            i++;
        }

        tmp = current->next;
        current->next = tmp->next;
        current->next->previous = current;
        free(tmp);
    }
}

void show(ListElement_type *head)
{
    printf("\n");
    if(head==NULL) printf("List is empty");
    else {
        ListElement_type *current=head;
        do {
            printf("%i", current->data);
            printf("\n");
            current = current->next;
        }while (current != head);
    }
}

void find(ListElement_type *head, int position)
{
    ListElement_type *current = head;

    if(position < list_size(head)/2)
    {
        int i = 0;
        while (current->next != head && i < position-1)
        {
            current = current->next;
            i++;
        }

        current = current->next;
        printf("\n");
        printf("%i", current->data);
    }
    else
    {
        int i = list_size(head);
        while (current->previous != NULL && i > position+1)
        {
            current = current->previous;
            i--;
        }

        current = current->previous;
        printf("\n");
        printf("%i", current->data);
    }
}


void merge(ListElement_type **head1, ListElement_type **head2)
{
    ListElement_type *current = *head2;
    ListElement_type *next;

    while (current->next != (*head2))
    {
        push(head1, current->data);
        next = current->next;
        free(current);
        current = next;
    }

    if (current->next == (*head2))
    {
        push(head1, current->data);
        free(current);
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
        }while (current != head);
    }
    return counter;
}
