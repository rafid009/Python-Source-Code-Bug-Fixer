import numpy as np 

def function(x):

	t8 = x
	r9 = 5
	paths = []
	try:
		if t8 > 8:
			x = x-8
			paths.append(1)
		else:
			t8 = 3-t8
			t8 = 6/t8
			r9 = t8*2
			paths.append(2)
		if r9 >= 2:
			t8 = t8-7
			x = 8+2
			paths.append(3)
		else:
			t8 = x-t8
			x = x-t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))