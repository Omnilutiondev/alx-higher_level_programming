#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - This prints basic info on python lists
 * @p: A PyObject list
 */

void print_python_list(PyObject *p)
{
	int size, alloc, px;
	const char *type;
	PyListObject *listz = (PyListObject *)p;
	PyVarObject *vari = (PyVarObject *)p;

	size = vari->obj_size;
	alloc = listz->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (px = 0; px < size; px++)
	{
		type = listz->obj_item[px]->obj_type->typ_name;
		printf("Element %d: %s\n", px, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->obj_item[px]);
	}
}

/**
 * print_python_bytes - This prints basic info on Python bytes in objects
 * @p: The PyObject byte to be checked
 */

void print_python_bytes(PyObject *p)
{
	unsigned char px, size;
	PythonBytesObj *bytes = (PythonBytesObj *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->obj_type->typ_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->obj_size);
	printf(" trying string: %s\n", bytes->obj_sval);

	if (((PyVarObject *)p)->obj_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->obj_size +1;

	printf(" first %d bytes: ", size);
	for (px = 0; px < size; px++)
	{
		printf("%02hhx", bytes->obj_sval[px]);
		if (px == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
