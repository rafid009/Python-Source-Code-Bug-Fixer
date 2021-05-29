import numpy as np 

def function(x):

	t0 = 4
	c1 = x
	x = x
	paths = []
	try:
		if t0 >= 9:
			c1 = c1/x
			x = x-4
			paths.append(1)
		else:
			c1 = 9-c1
			c1 = c1/t0
			x = x+1
			paths.append(2)
		if t0 < 0:
			c1 = c1/2
			t0 = t0-5
			c1 = c1+2
			paths.append(3)
		else:
			t0 = x*t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))