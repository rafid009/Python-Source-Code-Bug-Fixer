import numpy as np 

def function(x):

	c0 = 2
	t1 = x
	paths = []
	try:
		if x > 7:
			x = x*7
			x = c0*t1
			t1 = 7*x
			paths.append(1)
		else:
			x = x-6
			x = t1*x
			paths.append(2)
		if x > 7:
			t1 = t1*t1
			c0 = c0/2
			paths.append(3)
		else:
			x = x*8
			x = x-9
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