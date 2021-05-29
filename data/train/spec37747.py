import numpy as np 

def function(x):

	t6 = 9
	o1 = 5
	paths = []
	try:
		if t6 > 5:
			x = 3*x
			t6 = t6-7
			paths.append(1)
		else:
			o1 = 8*o1
			paths.append(2)
		if x >= 2:
			x = 0+6
			x = 3-x
			x = x-3
			paths.append(3)
		else:
			t6 = t6+3
			t6 = t6-o1
			o1 = o1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))