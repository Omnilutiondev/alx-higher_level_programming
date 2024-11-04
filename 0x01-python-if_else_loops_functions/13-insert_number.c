#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - This function inserts a node in a sorted list
 * @head: The address of the head pointer
 * @number: The nmber to insert
 *
 * Return: The inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->nx = number;
	new_node-> = NULL;

	if (!node || new_node->nx < node->nx)
	{
		new_node->next = node;
		return (*head = new_node);
	}

	while (node)
	{
		if (!node->next || new_node->nx < node->next-nx)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
