import numpy as np 

def function(x):

	n8 = 9
	t1 = x
	paths = []
	try:
		if t1 < 8:
			n8 = n8-n8
			x = n8/8
			paths.append(1)
		else:
			x = x-2
			t1 = t1-4
			paths.append(2)
		if n8 >= 9:
			n8 = n8-8
			t1 = n8/n8
			x = 1/x
			paths.append(3)
		else:
			n8 = n8/8
			x = 5-x
			x = t1-x
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