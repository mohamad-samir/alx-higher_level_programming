#include "Python.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_string - prints information about a python string
 * @p: pointer to the string object, checks to see it is string
 */

void print_python_string(PyObject *p)
{
	int u;
	ssize_t len = 0;
	char *unicode = "compact unicode object";
	char *ascii = "compact ascii";
	char *str = NULL, *encoding = NULL;
	PyObject *str_ob = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = (ssize_t)PyUnicode_GET_LENGTH(p);

	str_ob = PyUnicode_AsUTF8String(p);
	str = PyBytes_AsString(str_ob);

	for (u = 0; u < len; u++)
	{
		if (str[u] < 0)
		{
			encoding = unicode;
			break;
		}
	}
	if (encoding == NULL)
		encoding = ascii;

	printf("  type: %s\n", encoding);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", str);
}