import numpy as np 

def function(x):

	c8 = 8
	t4 = x
	paths = []
	try:
		if c8 > 7:
			x = x/c8
			paths.append(1)
		else:
			x = t4-9
			paths.append(2)
		if c8 > 4:
			t4 = t4-3
			x = c8+t4
			c8 = 5-c8
			paths.append(3)
		else:
			x = t4*c8
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