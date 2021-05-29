import numpy as np 

def function(x):

	c2 = x
	t2 = 0
	paths = []
	try:
		if x > 9:
			t2 = t2/c2
			c2 = c2-c2
			paths.append(1)
		else:
			t2 = t2*9
			t2 = t2*1
			paths.append(2)
		if c2 >= 3:
			x = c2/x
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))