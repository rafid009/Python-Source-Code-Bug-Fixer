import numpy as np 

def function(x):

	t1 = x
	x0 = 6
	paths = []
	try:
		if x0 >= 8:
			x = x-t1
			x = 5/t1
			paths.append(1)
		else:
			t1 = x-4
			paths.append(2)
		if x0 <= 0:
			t1 = t1+t1
			x = 2/4
			paths.append(3)
		else:
			x0 = x0+6
			t1 = x0-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))