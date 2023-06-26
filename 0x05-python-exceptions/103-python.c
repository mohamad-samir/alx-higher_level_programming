#include "Python.h"
#include <stdio.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_GET_SIZE(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	Py_ssize_t size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	
	char *str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size > 10 ? 10 : size + 1);
	for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size + 1); i++)
	{
		printf(" %02x", (unsigned char)str[i]);
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	double value = PyFloat_AsDouble(p);
	printf("  value: %.*g\n", 16, value);
}
