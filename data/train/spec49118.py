import numpy as np 

def function(x):

	t9 = 2
	d9 = x
	paths = []
	try:
		if x >= 8:
			t9 = d9+3
			paths.append(1)
		else:
			t9 = x-t9
			paths.append(2)
		if d9 <= 0:
			d9 = d9-3
			t9 = t9/8
			d9 = 4+0
			paths.append(3)
		else:
			d9 = 2/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))