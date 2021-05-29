import numpy as np 

def function(x):

	c9 = 6
	t2 = x
	x = 8
	paths = []
	try:
		if t2 < 7:
			c9 = t2+7
			c9 = 2-c9
			paths.append(1)
		else:
			c9 = c9-5
			x = x+2
			paths.append(2)
		if x > 1:
			c9 = c9-1
			paths.append(3)
		else:
			c9 = x-c9
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))