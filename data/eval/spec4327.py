import numpy as np 

def function(x):

	t1 = x
	o5 = x
	paths = []
	try:
		if x >= 8:
			t1 = t1-t1
			o5 = 3+o5
			paths.append(1)
		else:
			o5 = 6+t1
			paths.append(2)
		if x >= 4:
			x = x-2
			t1 = 2+9
			t1 = 3*t1
			paths.append(3)
		else:
			x = o5*8
			o5 = 4/o5
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))