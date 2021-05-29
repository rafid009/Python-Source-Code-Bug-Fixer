import numpy as np 

def function(x):

	t2 = 7
	c3 = 6
	x = x
	paths = []
	try:
		if t2 < 4:
			c3 = c3*6
			c3 = 6+4
			c3 = c3-1
			paths.append(1)
		else:
			x = 6*x
			c3 = t2/c3
			paths.append(2)
		if x <= 1:
			x = x/5
			t2 = 4-1
			c3 = 7+0
			paths.append(3)
		else:
			x = 4+7
			t2 = 9-7
			x = x+0
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