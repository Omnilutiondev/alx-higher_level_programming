/*
 * File: 103-python.c
 * Auth: IKENNA JOHN AGU
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - This function Prints basic info about Python lists.
 * @p: The PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, idx;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (idx = 0; idx < size; idx++)
	{
		type = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %ld: %s\n", idx, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[idx]);
	}
}

/**
 * print_python_bytes - This function prints basic info about Python byte objects.
 * @p: The PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, idx;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (idx = 0; idx < size; idx++)
	{
		printf("%02hhx", bytes->ob_sval[idx]);
		if (idx == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - This function Prints basic info about Python float objects.
 * @p: The PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
