#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - gives data of the PyListObject
 *
 * @p: the PyObject
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t s = 0;
	int a = 0;

	if (PyList_CheckExact(p))
	{
		s = PyList_Size(p);

		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (a < s)
		{
			printf("Element %d: %s\n",
					a, Py_TYPE(PyList_GetItem(p, a))->tp_name);
			a++;
		}
	}
}
