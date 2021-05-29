import numpy as np 

def function(x):

	t4 = x
	c5 = 1
	paths = []
	try:
		if c5 >= 1:
			x = x-2
			x = 4*x
			t4 = 4+t4
			paths.append(1)
		else:
			t4 = 2+6
			t4 = c5-t4
			paths.append(2)
		if x > 4:
			x = x-0
			c5 = 2+c5
			paths.append(3)
		else:
			c5 = c5-9
			c5 = c5*x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))